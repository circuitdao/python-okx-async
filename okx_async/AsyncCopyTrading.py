from .asyncClient import AsyncClient
from .consts import *


class AsyncCopyTradingAPI(AsyncClient):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1',
                 domain='https://www.okx.com', debug=True):
        AsyncClient.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    # Get existing leading positions
    async def get_existing_leading_positions(self, instId=''):
        params = {
            'instId': instId
        }
        return await self._request_with_params(GET, GET_EXISTING_LEADING_POSITIONS, params)

    # Get leading position history
    async def get_leading_position_history(self, instId='', after='', before='', limit=''):
        params = {
            'instId': instId,
            'after': after,
            'before': before,
            'limit': limit
        }
        return await self._request_with_params(GET, GET_LEADING_POSITIONS_HISTORY, params)

    # Place leading stop order
    async def place_leading_stop_order(self, subPosId='', tpTriggerPx='', slTriggerPx='', tpTriggerPxType='', slTriggerPxType=''):
        params = {
            'subPosId': subPosId,
            'tpTriggerPx': tpTriggerPx,
            'slTriggerPx': slTriggerPx,
            'tpTriggerPxType': tpTriggerPxType,
            'slTriggerPxType': slTriggerPxType
        }
        return await self._request_with_params(POST, PLACE_LEADING_STOP_ORDER, params)

    # Close leading position
    async def close_leading_position(self, subPosId=''):
        params = {
            'subPosId': subPosId
        }
        return await self._request_with_params(POST, CLOSE_LEADING_POSITIONS, params)

    # Get leading instruments
    async def get_leading_instruments(self):
        return await self._request_without_params(GET, GET_LEADING_POSITIONS)

    # Amend leading instruments
    async def amend_leading_instruments(self, instId=''):
        params = {
            'instId': instId
        }
        return await self._request_with_params(POST, AMEND_EXISTING_LEADING_POSITIONS, params)

    # Get profit sharing details
    async def get_profit_sharing_details(self, after='', before='', limit=''):
        params = {
            'after': after,
            'before': before,
            'limit': limit
        }
        return await self._request_with_params(GET, GET_PROFIT_SHARING_DETAILS, params)

    # Get total profit sharing
    async def get_total_profit_sharing(self):
        return await self._request_without_params(GET, GET_TOTAL_PROFIT_SHARING)

    # Get unrealized profit sharing details
    async def get_unrealized_profit_sharing_details(self):
        return await self._request_without_params(GET, GET_UNREALIZED_PROFIT_SHARING_DETAILS)
