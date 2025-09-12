import asyncio

from okx_async.websocket.WsPublicAsync import WsPublicAsync


def publicCallback(message):
    print("publicCallback", message)


async def main():

    url = "wss://ws.okx.com:8443/ws/v5/public"
    ws = WsPublicAsync(url=url)
    await ws.start()
    #arg = {"channel": "tickers", "instId": "XCH-USDT"}
    args = [{"channel": "books", "instId": "XCH-USDT"}]
    print("------------------------------------------subscribe---------------------------------------------")
    await ws.subscribe(args, publicCallback)
    await asyncio.sleep(30)
    print("-----------------------------------------unsubscribe--------------------------------------------")
    await ws.unsubscribe(args, publicCallback)
    await asyncio.sleep(5)

if __name__ == '__main__':
    asyncio.run(main())
