# BitcoinTracker:
### Small Python project using IFTTT to send the current <br> BitCoin price to a channel in Discord
  
![GitHub Repo stars](https://img.shields.io/github/stars/Pollyanna584/BitcoinTracker?style=social)

# Goal: :
- To use Python to post the current Bitcoin (BTC) price in a discord channel.<br>We will be using:<br>The CoinMarketCap API to get the current price of bitcoin<br>IFTTT to recieve the JSON info and send it to Discord

# Note before starting:
- This is currently in a semi-working state.  The Discord applet in IFTTT has its own share of issues<br>![alt text](https://i.imgur.com/ypuQkpZ.png)<br>The script at its current state does what it is supposed to do, but it returns `{"JsonPayload":23538.12}` when it should return `23538.12` in discord

# Setting up IFTTT
- 