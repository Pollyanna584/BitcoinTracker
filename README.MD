# BitcoinTracker:
### Small Python project using IFTTT to send the current BitCoin price to a channel in Discord
  
![GitHub Repo stars](https://img.shields.io/github/stars/Pollyanna584/BitcoinTracker?style=social)

# Shoutouts :
This script was inspired by [Python Project for Beginners: Bitcoin Price Notifications](https://realpython.com/python-bitcoin-ifttt/) which was written by [novoselrok](https://github.com/novoselrok), although I had to make some significant changes to use the CoinMarketCap API and the Discord applet from IFTTT.<br>That being said, I would not have gotten this far without the write up so thank you noveselrok!

# Goal :
To use Python to post the current Bitcoin (BTC) price in a discord channel.

# Resources :
To create this script, we will be using:<br><br>The CoinMarketCap API to get the current price of bitcoin<br>IFTTT to recieve the JSON info and send it to Discord

# Note before starting :
This is currently in a semi-working state.  The [Discord applet](https://ifttt.com/discord/health) in IFTTT has its own share of issues<br>![alt text](https://i.imgur.com/ypuQkpZ.png)<br>The script at its current state does what it is supposed to do, but it currently returns<br>`{"JsonPayload":23538.12}`<br> when it should return <br>`23538.12`<br>

# Roadmap :
- Setup Python environment
- Setup CoinMarketCap API
- Setup IFTTT to receive JSON info via Webhook and deliver it to Discord
- The python code

# Python environment :
-

# Setup CoinMarketCap API :
- Sign up for a free account at the [CoinMarketCap Website](https://coinmarketcap.com/api/)
- Go to [the developer page](https://pro.coinmarketcap.com/account) and get your API key
![alt text](https://i.imgur.com/W8855gW.png)<br>**NOTE**<br>DO NOT SHARE THIS WITH ANYONE<br>

# Setting up IFTTT :
- 

# Python Code