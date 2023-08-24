from .asyncClient import AsyncClient
from .consts import *


class AsyncConvertAPI(AsyncClient):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com', debug=True):
        AsyncClient.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    async def get_currencies(self):
        params = {}
        return await self._request_with_params(GET, GET_CURRENCIES, params)

    async def get_currency_pair(self, fromCcy='', toCcy=''):
        params = {"fromCcy": fromCcy, 'toCcy': toCcy}
        return await self._request_with_params(GET, GET_CURRENCY_PAIR, params)

    async def estimate_quote(self, baseCcy = '', quoteCcy = '', side = '', rfqSz = '', rfqSzCcy = '', clQReqId = '',tag=''):
        params = {'baseCcy': baseCcy, 'quoteCcy': quoteCcy, 'side':side, 'rfqSz':rfqSz, 'rfqSzCcy':rfqSzCcy, 'clQReqId':clQReqId,'tag':tag}
        return await self._request_with_params(POST, ESTIMATE_QUOTE, params)

    async def convert_trade(self, quoteId = '', baseCcy = '', quoteCcy = '', side = '', sz = '', szCcy = '', clTReqId = '',tag=''):
        params = {'quoteId': quoteId, 'baseCcy': baseCcy, 'quoteCcy':quoteCcy, 'side':side, 'sz':sz, 'szCcy':szCcy, 'clTReqId':clTReqId,'tag':tag}
        return await self._request_with_params(POST, CONVERT_TRADE, params)

    async def get_convert_history(self, after = '', before = '', limit = '',tag=''):
        params = {'after': after, 'before': before, 'limit':limit,'tag':tag}
        return await self._request_with_params(GET, CONVERT_HISTORY, params)
