from .asyncClient import AsyncClient
from .consts import *


class AsyncEarningAPI(AsyncClient):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com', debug=True):
        AsyncClient.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    async def get_offers(self,productId = '',protocolType = '',ccy = ''):
        params = {
            'productId':productId,
            'protocolType':protocolType,
            'ccy':ccy
        }
        return await self._request_with_params(GET,STACK_DEFI_OFFERS,params)

    async def purchase(self, productId='', investData=[], term='', tag=''):

        params = {
            'productId': productId,
            'investData': investData
        }
        if term != '':
            params['term'] = term
        if tag != '':
            params['tag'] = tag
        return await self._request_with_params(POST, STACK_DEFI_PURCHASE, params)

    async def redeem(self,ordId = '',protocolType = '',allowEarlyRedeem = ''):
        params = {
            'ordId':ordId,
            'protocolType':protocolType,
            'allowEarlyRedeem':allowEarlyRedeem
        }
        return await self._request_with_params(POST,STACK_DEFI_REDEEM,params)

    async def cancel(self,ordId = '',protocolType = ''):
        params = {
            'ordId':ordId,
            'protocolType':protocolType
        }
        return await self._request_with_params(POST,STACK_DEFI_CANCEL,params)

    async def get_activity_orders(self,productId = '',protocolType = '',ccy = '',state = ''):
        params = {
            'productId':productId,
            'protocolType':protocolType,
            'ccy':ccy,
            'state':state
        }
        return await self._request_with_params(GET,STACK_DEFI_ORDERS_ACTIVITY,params)

    async def get_orders_history(self,productId = '',protocolType = '',ccy = '',after = '',before = '',limit = ''):
        params = {
            'productId':productId,
            'protocolType':protocolType,
            'ccy':ccy,
            'after':after,
            'before':before,
            'limit':limit
        }
        return await self._request_with_params(GET,STACK_DEFI_ORDERS_HISTORY,params)

    # - Get saving balance
    async def get_saving_balance(self, ccy=''):
        params = {
            'ccy': ccy
        }
        return await self._request_with_params(GET, GET_SAVING_BALANCE, params)

    # - Savings purchase/redemption
    async def savings_purchase_redemption(self, ccy='', amt='', side='', rate=''):

        params = {
            'ccy': ccy,
            'amt': amt,
            'side': side,
            'rate': rate
        }
        return await self._request_with_params(POST, SAVING_PURCHASE_REDEMPTION, params)

    # - Set lending rate
    async def set_lending_rate(self, ccy='', rate=''):
        params = {
            'ccy': ccy,
            'rate': rate
        }
        return await self._request_with_params(POST, SET_LENDING_RATE, params)

    # - Get lending history
    async def get_lending_history(self, ccy='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return await self._request_with_params(GET, GET_LENDING_HISTORY, params)

    # - Get public borrow info (public)
    async def get_public_borrow_info(self, ccy=''):
        params = {
            'ccy': ccy
        }
        return await self._request_with_params(GET, GET_PUBLIC_BORROW_INFO, params)

    # - Get public borrow history (public)
    async def get_public_borrow_history(self, ccy='', after='', before='', limit=''):
        params = {
            'ccy': ccy,
            'after': after,
            'before': before,
            'limit': limit
        }
        return await self._request_with_params(GET, GET_PUBLIC_BORROW_HISTORY, params)
