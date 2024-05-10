import os
from dotenv import load_dotenv
from synthetix import Synthetix

# load environment variables
load_dotenv(override=True)

# initialize the client
snx = Synthetix(
    provider_rpc=os.environ.get("PROVIDER_RPC"),
    private_key=os.environ.get("PRIVATE_KEY"),
)

snx.perps.get_account_ids()

# get sUSD balance
eth_balance = snx.get_eth_balance()
usd_balance = snx.get_susd_balance()

# print information about the current state
print(
    f"""
Address: {snx.address}
ETH balance: {eth_balance['eth']}
WETH balance: {eth_balance['weth']}
sUSD balance: {usd_balance['balance']}

Perps accounts: {', '.join(map(str, snx.perps.account_ids))}
Perps default account: {snx.perps.default_account_id}
Perps markets: {', '.join(snx.perps.markets_by_name)}
"""
)
