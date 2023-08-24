from .asyncClient import AsyncClient
from .consts import *


class AsyncStatusAPI(AsyncClient):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com', debug=True):
        AsyncClient.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    async def status(self, state=''):
        params = {'state': state}
        return await self._request_with_params(GET, STATUS, params)
