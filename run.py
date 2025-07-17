from cubewise_pulser import config_ini
from cubewise_pulser.mcp_server import create_app
from cubewise_pulser.utils.config_schema import MCPServerConfig


def run_mcp():
    create_app().run(**MCPServerConfig.load_from_config(config_ini).to_dict())


if __name__ == '__main__':
    run_mcp()
