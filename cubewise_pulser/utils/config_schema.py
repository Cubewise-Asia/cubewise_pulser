from dataclasses import dataclass

from opensearchpy import OpenSearch


@dataclass(frozen=True)
class OpenSearchConfig:
    host: str
    port: str

    @classmethod
    def load_from_config(cls, config: 'ConfigParser'):
        assert 'opensearch' in config.sections(), 'opensearch section not found in config'
        config_class = cls(**config['opensearch'])
        return config_class

    def to_dict(self):
        return {
            'hosts': [{
                "host": self.host,
                "port": self.port
            }],
            'http_compress': True,
            'use_ssl': False,
            'verify_certs': False,
            'ssl_assert_hostname': False,
            'ssl_show_warn': False
        }


@dataclass(frozen=True)
class MCPServerConfig:
    host: str
    port: str
    path: str
    transport: str
    log_level: str

    @classmethod
    def load_from_config(cls, config: 'ConfigParser'):
        section_name = 'mcp-server'
        assert section_name in config.sections(), 'mcp-server not found in config'
        config_class = cls(**config[section_name])
        return config_class

    def to_dict(self):
        return {
            "host": self.host,
            "port": int(self.port),
            "path": self.path,
            'transport': self.transport,
            'log_level': self.log_level,
        }


@dataclass(frozen=True)
class PathConfig:
    project_root: str
    tool_yaml: str

    @classmethod
    def load_from_config(cls, config: 'ConfigParser'):
        section_name = 'path'
        assert section_name in config.sections(), 'path not found in config'
        return cls(**config[section_name])
