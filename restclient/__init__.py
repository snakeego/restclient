from .client import RestClient
from .response import RestResponse, ErrorResponse
from .exceptions import RestQueryError

__all__ = ['RestClient', 'RestResponse', 'ErrorResponse', 'RestQueryError']
__version__ = "1.2.0"
__doc__ = "Client for various HTTP REST API"
