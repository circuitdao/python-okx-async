from .asyncClient import AsyncClient
from .consts import *


class AsyncNDBrokerAPI(AsyncClient):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com', debug=True):
        AsyncClient.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    #GET /api/v5/broker/nd/info
    async def get_broker_info(self):
        return await self._request_without_params(GET, BROKER_INFO)

    #POST /api/v5/broker/nd/create-subaccount
    async def create_subaccount(self,subAcct = '',label = ''):
        params = {
            'subAcct':subAcct,
            'label':label
        }
        return await self._request_with_params(POST,CREATE_SUBACCOUNT,params)

    async def delete_subaccount(self,subAcct = ''):
        params = {
            'subAcct':subAcct
        }
        return await self._request_with_params(POST,DELETE_SUBACCOUNT,params)

    async def get_subaccount_info(self,subAcct = '',page = '',limit = ''):
        params = {
            'subAcct':subAcct,
            'page':page,
            'limit':limit
        }
        return await self._request_with_params(GET,SUBACCOUNT_INFO,params)

    async def create_subaccount_apikey(self,subAcct = '',label='',passphrase='',ip='',perm=''):
        params = {
            'subAcct':subAcct,
            'label':label,
            'passphrase':passphrase,
            'ip':ip,
            'perm':perm
        }
        return await self._request_with_params(POST,ND_CREAET_APIKEY,params)

    async def get_subaccount_apikey(self,subAcct = '',apiKey = ''):
        params = {
            'subAcct':subAcct,
            'apiKey':apiKey
        }
        return await self._request_with_params(GET,ND_SELECT_APIKEY,params)

    async def reset_subaccount_apikey(self,subAcct = '',apiKey = '',label='',perm = '',ip = ''):
        params = {
            'subAcct':subAcct,
            'apiKey':apiKey,
            'label':label,
            'perm':perm,
            'ip':ip
        }
        return await self._request_with_params(POST,ND_MODIFY_APIKEY,params)

    async def delete_subaccount_apikey(self,subAcct = '',apiKey = ''):
        params = {
            'subAcct':subAcct,
            'apiKey':apiKey
        }
        return await self._request_with_params(POST,ND_DELETE_APIKEY,params)

    async def set_subaccount_level(self,subAcct = '',acctLv = ''):
        params = {
            'subAcct':subAcct,
            'acctLv':acctLv
        }
        return await self._request_with_params(POST,SET_SUBACCOUNT_LEVEL,params)

    async def set_subaccount_fee_rate(self,subAcct = '',instType = '',chgType = '',chgTaker = '',chgMaker = '',effDate = ''):
        params = {
            'subAcct':subAcct,
            'instType':instType,
            'chgType':chgType,
            'chgTaker':chgTaker,
            'chgMaker':chgMaker,
            'effDate':effDate
        }
        return await self._request_with_params(POST,SET_SUBACCOUNT_FEE_REAT,params)

    async def create_subaccount_deposit_address(self,subAcct = '',ccy = '',chain = '',addrType = '', to =''):
        params = {
            'subAcct':subAcct,
            'ccy':ccy,
            'chain':chain,
            'addrType':addrType,
            'to':to
        }
        return await self._request_with_params(POST,SUBACCOUNT_DEPOSIT_ADDRESS,params)

    async def reset_subaccount_deposit_address(self,subAcct = '',ccy = '',chain = '',addr = '',to = ''):
        params = {
            'subAcct':subAcct,
            'ccy':ccy,
            'chain':chain,
            'addr':addr,
            'to':to
        }
        return await self._request_with_params(POST,MODIFY_SUBACCOUNT_DEPOSIT_ADDRESS,params)

    async def get_subaccount_deposit_address(self,subAcct = '',ccy = ''):
        params = {
            'subAcct':subAcct,
            'ccy':ccy
        }
        return await self._request_with_params(GET,GET_SUBACCOUNT_DEPOSIT,params)

    async def get_subaccount_deposit_history(self,subAcct = '',ccy = '',txId = '',state = '',after = '',before = '',limit = ''):
        params = {
            'subAcct':subAcct,
            'ccy':ccy,
            'txId':txId,
            'state':state,
            'after':after,
            'before':before,
            'limit':limit
        }
        return await self._request_with_params(GET,SUBACCOUNT_DEPOSIT_HISTORY,params)

    async def get_rebate_daily(self,subAcct = '',begin = '',end = '',page = '',limit = ''):
        params = {
            'subAcct':subAcct,
            'begin':begin,
            'end':end,
            'page':page,
            'limit':limit
        }
        return await self._request_with_params(GET,REBATE_DAILY,params)

    async def get_rebate_details_download_link(self,type ='',begin = '',end = ''):
        params ={
            'type':type,
            'begin':begin,
            'end':end
        }
        return await self._request_with_params(GET,GET_REBATE_PER_ORDERS,params)



    async def generate_rebate_details_download_link(self,begin = '',end = ''):
        params = {
            'begin':begin,
            'end':end
        }
        return await self._request_with_params(POST,REBATE_PER_ORDERS,params)

