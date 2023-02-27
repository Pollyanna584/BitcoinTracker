# BitcoinTracker:
### Small Python project using IFTTT to send the current BitCoin price to a channel in Discord
  
![GitHub Repo stars](https://img.shields.io/github/stars/Pollyanna584/BitcoinTracker?style=social)

# About :
- I created this using Python@3.11 on MacOS using VSCode so these instructions are for MacOS

- This script was inspired by this article, [Python Project for Beginners: Bitcoin Price Notifications](https://realpython.com/python-bitcoin-ifttt/), which was written by [novoselrok](https://github.com/novoselrok).<br><br>Although I had to make some significant changes to use the CoinMarketCap API and the Discord applet from IFTTT, I would not have gotten this far without the write up, so thank you [novoselrok](https://github.com/novoselrok)!

# Goal :
To use Python to post the current Bitcoin (BTC) price in a Discord channel.

# Resources :
To create this script, we will be using:
- The CoinMarketCap API to get the current price of Bitcoin
- IFTTT to recieve the JSON info and send it to Discord

# Note before starting :
This is currently in a semi-working state.  The [Discord applet](https://ifttt.com/discord/health) in IFTTT has its own share of issues<br>![alt text](https://i.imgur.com/ypuQkpZ.png)<br>The script at its current state does what it is supposed to do, but it currently returns:<br>`{"JsonPayload":23538.12}`<br> when it should return:<br>`23538.12`<br>

# Roadmap :
- Setup Python environment
- Setup CoinMarketCap API
- Setup IFTTT to receive JSON info via Webhook and deliver it to Discord
- The python code

# Lets get started~

## Python environment :
If you are familiar with virutal environments, you can skip this part, otherwise:
- Create a virtual environemnt within python:<br>`python3 -m venv bitcoin_env`
- Activate the virtual environment<br>`source bitcoin_env/bin/activate`
- Install requests `pip install requests`
Requests is the library we will need to reach out to the webhook

## Setup CoinMarketCap API :
- Sign up for a free account at the [CoinMarketCap Website](https://coinmarketcap.com/api/)
- Go to [the developer page](https://pro.coinmarketcap.com/account) and get your API key
![alt text](https://i.imgur.com/W8855gW.png)<br>**NOTE :** DO NOT SHARE THIS WITH ANYONE<br>
- Once you have your API key, test it in terminal using this code:<br>**Be sure to replace <APIKey> with the API key from the last step**<br>```curl -H "X-CMC_PRO_API_KEY: <APIKey>" -H "Accept: application/json" -d "start=1&limit=5000&convert=USD" -G https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest```<br>

## Setting up IFTTT :
- 

## Python Code
- 