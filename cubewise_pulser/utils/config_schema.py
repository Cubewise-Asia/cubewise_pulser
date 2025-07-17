from opensearchpy import OpenSearch


class OpenSearchConfig:
    host: str
    port: str

    @classmethod
    def load_from_config(cls, config: 'ConfigParser'):
        assert 'opensearch' in config.sections(), 'opensearch section not found in config'
        config_class = cls()
        config_class.host = config['opensearch']['host']
        config_class.port = config['opensearch']['port']
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


class MCPServerConfig:
    name: str
    host: str
    port: str
    instruction: str
    sse_path: str

    @classmethod
    def load_from_config(cls, config: 'ConfigParser'):
        section_name = 'mcp-server'
        assert 'section_name' in config.sections(), 'mcp-server not found in config'
        config_class = cls()
        section = config[section_name]
        config_class.name = section['name']
        config_class.host = section['host']
        config_class.port = section['port']
        config_class.instruction = section['instruction']
        config_class.sse_path = section['sse_path']

    def to_dict(self):
        return {
            "host": self.host,
            "name": self.name,
            "port": self.port,
            "instruction": self.instruction,
            "sse_path": self.sse_path
        }
