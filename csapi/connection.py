"""Manages the connection to CubeServer.
"""

# Try to import configuration file
try:
    import client_config
except ImportError:
    pass

from collections import namedtuple
from json import dumps

GameStatus = namedtuple("GameStatus",
                        ['time',
                         'score',
                         'CubeServer_version']
                        )

HTTPResponse = namedtuple("HTTPResponse",
                          ['code', 'body']
                          )


def conf_if_exists(key: str):
    """Returns the config value if client_config is imported, else None"""
    if 'client_config' not in globals():
        return None
    return getattr(client_config, key)


class ConnectionConfig:
    """The configuration of the connection to the server"""
    TIMEOUT: int = 10
    if 'client_config' in globals():
        AP_SSID: str = client_config.CONF_AP_SSID
        AP_PASSWORD: str = client_config.CONF_AP_PASSWORD if hasattr(
            client_config, "CONF_AP_PASSWORD") else ""
        API_HOST: str = client_config.CONF_API_HOST
        API_PORT: int = client_config.API_PORT
    else:
        AP_SSID: str = "CubeServer-API"
        AP_PASSWORD: str = ""
        API_HOST: str = "api.local"
        API_PORT: int = 8081
