# About
```python-okx-async``` is an unofficial Python wrapper for the [OKX exchange v5 API](https://www.okx.com/okx-api) that comes with async support.
The wrapper is an extension of the [```python-okx```](https://github.com/okxapi/python-okx) package, which supports synchronous REST requests and websocket streams.

# Installation
To install the package, run
```
pip install python-okx-async
```

# Quick start

### Create an OKX account
- If you don't already have an OKX account, register for one on https://www.okx.com/account/register

### Create API credentials
- Log into your OK account and select ```API keys``` in the user menu
- Click the ```+ Create V5 API key``` button
- Follow the instructions to create API credentials (key, passhprase, secret)

### Save API credentials
- If there isn't a ```.env``` file in your home directory, create one and make sure it can only be read and written to by you.
```
touch ~/.env
chmod 600 ~/.env
```
- Add the following lines to the ```.env``` file, replacing the text to the right of the equal signs with the credentials created above. Note that the credentials should NOT be enclosed in quotation marks.
```
OKX_API_KEY=<key>
OKX_API_PASSPHRASE=<passphrase>
OKX_API_SECRET=<secret>
```
API credentials are stored in a ```.env``` file for security reasons. It is not advisable to include API credentials directly in source code or to provide them as command line arguments.

### Run examples
Import and instantiate the API wrapper class ```AsyncTradeAPI```, which is used for order placement, as follows
```
import os
from dotenv import load_dotenv
from okx_async.AsyncTrade import AsyncTradeAPI

load_dotenv()

tradeAPI = AsyncTradeAPI(os.getenv("OKX_API_KEY"), os.getenv("OKX_API_SECRET"), os.getenv("OKX_API_PASSPHRASE"), flag="0", debug=False)
```
The other API classes can be instantiated similarly. Note that by default ```flag="1"```, which is the OKX demo environment, and ```debug=True```.

The ```example_order_book.py``` script included in the Github repository prints the order book for the XCH-USDT spot market to a depth of 20 levels.

Also make sure to check out the documentation of ```python-okx```, and the additional [examples](https://github.com/okxapi/python-okx/example) included in that repository.
