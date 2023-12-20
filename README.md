# Synthetix V3 Perps Order Keeper

This project is a sample order keeper for Synthetix Perps V3 using the [Python SDK](https://github.com/Synthetixio/python-sdk) and [Project Template](https://github.com/Synthetixio/project-template-python) from Synthetix, and [Silverback](https://github.com/ApeWorX/silverback) from Apeworx.

## Getting Started

1. Before you begin, ensure you have:
* A RPC endpoint like [Infura](https://infura.io/) or [Alchemy](https://www.alchemy.com/)
* A wallet address **and** the private key for that address
* Installed Python 3.8 or greater
    * Run `python --version` in your terminal to check

2. Download this repository to a preferred location on your computer. Here's how:

```bash
git clone https://github.com/Synthetixio/sample-v3-keeper.git
cd sample-v3-keeper
```

3. Set up the required packages in a virtual environment:

```bash
python3 -m venv env
source env/bin/activate

pip install --upgrade pip
pip install -r requirements.txt
```

Then install `ape` plugins:

```bash
ape plugins install .
```

4. Make a copy of the .env.example file, name it .env, and then enter the details for your RPC and wallet.

In order to subscribe to events using Silverback, you will also need a connection to [Alchemy](https://www.alchemy.com/). You can sign up for a free account and create a new project to get an API key, then add it to your `.env` file:

```bash
WEB3_ALCHEMY_API_KEY=<your-api-key>
```

5. Run the keeper:

```bash
silverback run main:app --network base:goerli:alchemy --runner silverback.runner:WebsocketRunner
```

You should see logs at each block that the keeper is running:
```bash
INFO: block[block=0x485d5517129207ddacb0ab8f61639103ebf860c187175f656232b50bbb63f685] - 0.000s (0.0%)
INFO: block[block=0x8bcbf1811722031fde5b5fcf510a8ef87a230eaae2b890ba9ca17be8a8ffc94d] - Started
2023-10-20 14:28:14,161 - Synthetix - INFO - Received block number 11320038
INFO: block[block=0x8bcbf1811722031fde5b5fcf510a8ef87a230eaae2b890ba9ca17be8a8ffc94d] - 0.000s (0.0%)
INFO: block[block=0x50aa19fde7ec10c69b51625430848c2f625b298d95e91b37e750e34039221816] - Started
2023-10-20 14:28:14,362 - Synthetix - INFO - Received block number 11320039
INFO: block[block=0x50aa19fde7ec10c69b51625430848c2f625b298d95e91b37e750e34039221816] - 0.000s (0.0%)
```

Additionally, when an `OrderCommitted` event happens the logs are displayed and an order settlement is triggered:

```bash
INFO: block[block=0xce2a1bbc1ba1df3138d9182888ac04bdab15a633fe945eca928b3e0f8d34dcbd] - Started
2023-10-20 14:28:22,135 - Synthetix - INFO - Received block number 11320042
INFO: 0x9863Dae3f4b5F4Ffe3A841a21565d57F2BA10E87/event/OrderCommitted[txn=0x4f220ae82677e80de01f041e92fe6de19d9b19bf16d8d582129308906c857e59,log_index=32] - Started
Perps order committed: OrderCommitted(marketId=100 accountId=100 trackingCode=0x4b57454e54410000000000000000000000000000000000000000000000000000 orderType=0 sizeDelta=62200000000000000 acceptablePrice=1623332565317468836725 settlementTime=1697833717 expirationTime=1697833777 sender=0x43C92D390D3ED89716e4a0776d8Aea1fB965D55D)
2023-10-20 14:28:22,139 - Synthetix - INFO - Settling order for 100 for market ETH
```

## Status Check

You can check the status of the connected account by running the following:

```bash
python status.py
```

This will run a short status script to print your balances and perps account info. It can be used to check that your account and RPC are connected properly without running the Silverback app.