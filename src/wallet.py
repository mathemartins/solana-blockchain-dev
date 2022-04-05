import base58
import asyncio
import solana
from solana.rpc.api import Client
from solana.keypair import Keypair
from solana.rpc.websocket_api import connect

client = Client("https://api.testnet.solana.com")

# Subscribing to solana event on a wallet
async with connect("wss://api.testnet.solana.com") as websocket:
    # Create a Test Wallet
    wallet = Keypair()
    # Subscribe to the Test wallet to listen for events
    await websocket.account_subscribe(wallet.public_key)
    # Capture response from account subscription
    first_resp = await websocket.recv()
    print("Subscription successful with id {}, listening for events \n".format(first_resp.result))
    updated_account_info = await websocket.recv()
    print(updated_account_info)

"""
The base currency for solana is LAMPORTS
1000000000 LAMPORTS = 1 sol
"""

wallet = Keypair()

# Input Airdrop amount in LAMPORTS
client.request_airdrop(wallet.public_key, 1000000000)

# Airdrops 1 SOL


"""
Get a solana keypair
"""
keypair = Keypair()

"""
How to restore a Keypair from a secret
"""
secret_key = [
    174, 47, 154, 16, 202, 193, 206, 113, 199, 190, 53, 133, 169, 175, 31, 56, 222, 53, 138,
    189, 224, 216, 117, 173, 10, 149, 53, 45, 73, 251, 237, 246, 15, 185, 186, 82, 177, 240,
    148, 69, 241, 227, 167, 80, 141, 89, 240, 121, 121, 35, 172, 247, 68, 251, 226, 218, 48,
    63, 176, 109, 168, 89, 238, 135,
]

keypair = Keypair.from_secret_key(bytes(secret_key))

"""
How to restore a Keypair from a base58
"""
b58_string = "5MaiiCavjCmn9Hs1o3eznqDEhRwxo7pXiAYez7keQUviUkauRiTMD8DrESdrNjN8zd9mTmVhRvBJeg5vhyvgrAhG"
keypair = Keypair.from_secret_key(base58.b58decode(b58_string))
print("Created Keypair with Public Key: {}".format(keypair.public_key))