import os
import logging
import socket
import sys
import multiprocessing
import win32serviceutil
import win32service
import win32event
import servicemanager

from run import main


class Service(win32serviceutil.ServiceFramework):
    _svc_name_ = "cubewise-service"
    _svc_display_name_ = "Cubewise Service"
    _svc_description_ = "Cubewise Service"

    def __init__(self, *args):
        win32serviceutil.ServiceFramework.__init__(self, *args)
        self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
        socket.setdefaulttimeout(5)
        self.stop_requested = False

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
        win32event.SetEvent(self.hWaitStop)
        self.ReportServiceStatus(win32service.SERVICE_STOPPED)
        logging.info('Stopped service ...')
        self.stop_requested = True

    def SvcDoRun(self):
        servicemanager.LogMsg(servicemanager.EVENTLOG_INFORMATION_TYPE, servicemanager.PYS_SERVICE_STARTED,
                              (self._svc_name_, ''))

        main()


if __name__ == '__main__':
    multiprocessing.freeze_support()
    args = sys.argv

    if len(args) == 1:
        servicemanager.Initialize()
        servicemanager.PrepareToHostSingle(Service)
        servicemanager.StartServiceCtrlDispatcher()
    else:
        win32serviceutil.HandleCommandLine(Service)
