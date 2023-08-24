from .asyncClient import AsyncClient
from .consts import *


class AsyncSpreadAPI(AsyncClient):

    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com', debug=True):
        AsyncClient.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    # Place Order
    async def place_order(self, sprdId='', clOrdId='', tag='', side='', ordType='', sz='', px=''):
        params = {'sprdId': sprdId, 'clOrdId': clOrdId, 'tag': tag, 'side': side, 'ordType': ordType, 'sz': sz,
                  'px': px}
        return await self._request_with_params(POST, SPREAD_PLACE_ORDER, params)

    # Cancel Order
    async def cancel_order(self,ordId='', clOrdId=''):
        params = {'ordId': ordId, 'clOrdId': clOrdId}
        return await self._request_with_params(POST, SPREAD_CANAEL_ORDER, params)

    # Cancel All orders
    async def cancel_all_orders(self, sprdId=''):
        params = {'sprdId': sprdId}
        return await self._request_with_params(POST, SPREAD_CANAEL_ALL_ORDERS, params)

    # Get order details
    async def get_order_details(self, ordId='', clOrdId=''):
        params = {'ordId': ordId, 'clOrdId': clOrdId}
        return await self._request_with_params(GET, SPREAD_GET_ORDER_DETAILS, params)

    # Get active orders
    async def get_active_orders(self, sprdId='', ordType='', state='', beginId='', endId='', limit=''):
        params = {'sprdId': sprdId, 'ordType': ordType, 'state': state, 'beginId': beginId, 'endId': endId, 'limit': limit}
        return await self._request_with_params(GET, SPREAD_GET_ACTIVE_ORDERS, params)

    # Get orders (last 7 days)
    async def get_orders(self, sprdId='', ordType='', state='', beginId='', endId='', begin='', end='', limit=''):
        params = {'sprdId': sprdId, 'ordType': ordType, 'state': state, 'beginId': beginId, 'endId': endId,
                  'begin': begin, 'end': end, 'limit': limit}
        return await self._request_with_params(GET, SPREAD_GET_ORDERS, params)

    # Get trades (last 7 days)
    async def get_trades(self, sprdId='', tradeId='', ordId='', beginId='', endId='', begin='', end='', limit=''):
        params = {'sprdId': sprdId, 'tradeId': tradeId, 'ordId': ordId, 'beginId': beginId, 'endId': endId,
                  'begin': begin, 'end': end, 'limit': limit}
        return await self._request_with_params(GET, SPREAD_GET_TRADES, params)

    # Get Spreads (Public)
    async def get_spreads(self, baseCcy='',instId='', sprdId='', state=''):
        params = {'baseCcy': baseCcy, 'instId': instId, 'sprdId': sprdId, 'state': state}
        return await self._request_with_params(GET, SPREAD_GET_SPREADS, params)

    # Get order book (Public)
    async def get_order_book(self, sprdId='', sz=''):
        params = {'sprdId': sprdId, 'sz': sz}
        return await self._request_with_params(GET, SPREAD_GET_ORDER_BOOK, params)

    # Get ticker (Public)
    async def get_ticker(self, sprdId=''):
        params = {'sprdId': sprdId}
        return await self._request_with_params(GET, SPREAD_GET_TICKER, params)

    # Get public trades (Public)
    async def get_public_trades(self, sprdId=''):
        params = {'sprdId': sprdId}
        return await self._request_with_params(GET, SPREAD_GET_PUBLIC_TRADES, params)

