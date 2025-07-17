from cubewise_pulser import config_ini
from cubewise_pulser.utils.config_schema import MCPServerConfig
from fastmcp import FastMCP

mcp_config = MCPServerConfig.load_from_config(config_ini)

mcp_server = FastMCP(**mcp_config.to_dict())
