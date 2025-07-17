import yaml
from cubewise_pulser import config_ini
from cubewise_pulser.route.pulse_opensearch import mcp as opensearch_mcp
from cubewise_pulser.utils.config_schema import MCPServerConfig, PathConfig
from fastmcp import FastMCP

mcp_config = MCPServerConfig.load_from_config(config_ini)
path_config = PathConfig.load_from_config(config_ini)

with open(path_config.tool_yaml, 'r') as stream:
    tool_config = yaml.safe_load(stream)


def create_app():
    mcp = FastMCP(**tool_config['mcp-server'])
    mcp.mount(opensearch_mcp, 'pulse')
    return mcp
