import os
import asyncio
from dotenv import load_dotenv # 'pip install python-dotenv' to install this package
from pprint import pprint

from okx_async.AsyncMarketData import AsyncMarketAPI


async def print_order_book(instId, sz):

      load_dotenv()

      marketDataAPI = AsyncMarketAPI(os.getenv("OKX_API_KEY"),
                                     os.getenv("OKX_API_SECRET"),
                                     os.getenv("OKX_API_PASSPHRASE"),
                                     flag="0",
                                     debug=False)

      order_book = await marketDataAPI.get_orderbook(instId, depth)
      pprint(order_book)


if __name__ == '__main__':
   market = "XCH-USDT"
   depth = 20

   asyncio.run(print_order_book(market, depth))
