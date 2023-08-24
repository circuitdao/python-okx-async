from .asyncClient import AsyncClient
from .consts import *


class AsyncBlockTradingAPI(AsyncClient):
    def __init__(self, api_key='-1', api_secret_key='-1', passphrase='-1', use_server_time=False, flag='1', domain='https://www.okx.com', debug=True):
        AsyncClient.__init__(self, api_key, api_secret_key, passphrase, use_server_time, flag, domain, debug)

    async def counterparties(self):
        params = {}
        return await self._request_with_params(GET, COUNTERPARTIES, params)

    async def create_rfq(self, counterparties=[], anonymous='false', clRfqId='', tag='', allowPartialExecution='false',
                         legs=[]):
        params = {'counterparties': counterparties, 'anonymous': anonymous, 'clRfqId': clRfqId, 'tag': tag,
                  'allowPartialExecution': allowPartialExecution, 'legs': legs}
        return await self._request_with_params(POST, CREATE_RFQ, params)

    async def cancel_rfq(self, rfqId = '', clRfqId = ''):
        params = {'rfqId': rfqId, 'clRfqId': clRfqId}
        return await self._request_with_params(POST, CANCEL_RFQ, params)

    async def cancel_batch_rfqs(self, rfqIds=[], clRfqIds=[]):
        params = {'rfqIds': rfqIds, 'clRfqIds': clRfqIds}
        return await self._request_with_params(POST, CANCEL_BATCH_RFQS, params)

    async def cancel_all_rfqs(self):
        params = {}
        return await self._request_with_params(POST, CANCEL_ALL_RSQS, params)

    async def execute_quote(self, rfqId='', quoteId='', legs=[]):
        params = {'rfqId': rfqId, 'quoteId': quoteId, 'legs': legs}
        return await self._request_with_params(POST, EXECUTE_QUOTE, params)

    async def create_quote(self, rfqId='', clQuoteId='', tag='', quoteSide='', legs=[], anonymous=False, expiresIn=''):
        params = {'rfqId': rfqId, 'clQuoteId': clQuoteId, 'tag': tag, 'quoteSide': quoteSide, 'legs': legs,
                  'anonymous': anonymous, 'expiresIn': expiresIn}
        return await self._request_with_params(POST, CREATE_QUOTE, params)

    async def cancel_quote(self, quoteId  = '', clQuoteId = ''):
        params = {'quoteId': quoteId, 'clQuoteId': clQuoteId}
        return await self._request_with_params(POST, CANCEL_QUOTE, params)

    async def cancel_batch_quotes(self, quoteIds='', clQuoteIds=''):
        params = {'quoteIds': quoteIds, 'clQuoteIds': clQuoteIds}
        return await self._request_with_params(POST, CANCEL_BATCH_QUOTES, params)

    async def cancel_all_quotes(self):
        params = {}
        return await self._request_with_params(POST, CANCEL_ALL_QUOTES, params)

    async def get_rfqs(self, rfqId = '', clRfqId = '',  state = '', beginId = '', endId = '', limit = ''):
        params = {'rfqId': rfqId, 'clRfqId': clRfqId, 'state': state, 'beginId': beginId, 'endId': endId, 'limit':limit}
        return await self._request_with_params(GET, GET_RFQS, params)

    async def get_quotes(self, rfqId = '', clRfqId = '', quoteId = '', clQuoteId = '', state = '', beginId = '', endId = '', limit = ''):
        params = {'rfqId': rfqId, 'clRfqId': clRfqId, 'quoteId':quoteId,'clQuoteId':clQuoteId, 'state': state, 'beginId': beginId, 'endId': endId, 'limit':limit}
        return await self._request_with_params(GET, GET_QUOTES, params)

    async def get_trades(self, rfqId='', clRfqId='', quoteId='', clQuoteId='', state='', beginId='', endId='', beginTs='',
                         endTs='', limit=''):
        params = {'rfqId': rfqId, 'clRfqId': clRfqId, 'quoteId': quoteId, 'clQuoteId': clQuoteId, 'state': state,
                  'beginId': beginId, 'endId': endId, 'beginTs': beginTs, 'endTs': endTs, 'limit': limit}
        return await self._request_with_params(GET, GET_RFQ_TRADES, params)

    async def get_public_trades(self, beginId = '', endId = '', limit = ''):
        params = {'beginId': beginId, 'endId': endId, 'limit': limit}
        return await self._request_with_params(GET, GET_PUBLIC_TRADES, params)

    async def reset_mmp(self):
        return await self._request_without_params(POST, MMP_RESET)

    async def set_marker_instrument(self,params = []):

        return await self._request_with_params(POST, MARKER_INSTRUMENT_SETTING, params)

    #Get Quote products
    async def get_quote_products(self):
        return await self._request_without_params(GET, MARKER_INSTRUMENT_SETTING)
