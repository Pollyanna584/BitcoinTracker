# BitcoinTracker:
### Small Python project using IFTTT to send the current BitCoin price to a channel in Discord
  
![GitHub Repo stars](https://img.shields.io/github/stars/Pollyanna584/BitcoinTracker?style=social)

# About :
- I created this using Python@3.11 on MacOS using VSCode so these instructions are for MacOS

- This script was inspired by this article, [Python Project for Beginners: Bitcoin Price Notifications](https://realpython.com/python-bitcoin-ifttt/), which was written by [novoselrok](https://github.com/novoselrok).<br><br>Although I had to make some significant changes to use the CoinMarketCap API and the Discord applet from IFTTT, I would not have gotten this far without the write up, so thank you [novoselrok](https://github.com/novoselrok)!

## Goal
To use Python to post the current Bitcoin (BTC) price in a Discord channel.

## Note before starting
This is currently in a semi-working state.  The [Discord applet](https://ifttt.com/discord/health) in IFTTT has its own share of issues<br>![alt text](https://i.imgur.com/ypuQkpZ.png)<br>The script at its current state does what it is supposed to do, but it currently returns:<br>`{"JsonPayload":23538.12}`<br> when it should return:<br>`23538.12`<br>

# Lets get started!

## Roadmap :
- Setup Python environment
- Setup CoinMarketCap API
- Setup IFTTT to receive JSON info via Webhook and deliver it to Discord
- The python code

## Python environment
If you are familiar with virutal environments, you can skip this part, otherwise:
- Create a virtual environemnt within python:<br>`python3 -m venv bitcoin_env`
- Activate the virtual environment<br>`source bitcoin_env/bin/activate`
- Install requests `pip install requests`
Requests is the library we will need to reach out to the webhook

## Setup CoinMarketCap API
- Sign up for a free account at the [CoinMarketCap Website](https://coinmarketcap.com/api/)
- Go to [the developer page](https://pro.coinmarketcap.com/account) and get your API key
![alt text](https://i.imgur.com/W8855gW.png)<br>**NOTE :** DO NOT SHARE THIS WITH ANYONE<br>
- Once you have your API key, test it in terminal using this code:<br>**Be sure to replace &ltAPIKey&gt with the API key from the last step**<br>````curl -H "X-CMC_PRO_API_KEY: <APIKey>" -H "Accept: application/json" -d "start=1&limit=5000&convert=USD" -G https://sandbox-api.coinmarketcap.com/v1/cryptocurrency/listings/latest````
- The response should look something like this:<br>```{"status":{"timestamp":"2023-02-27T03:48:30.669Z","error_code":0,"error_message":null,"elapsed":1,"credit_count":1,"notice":null},"data":[{"id":5202,"name":"x57hlxgghio","symbol":"hr009a0sor","slug":"t17wp635xi","cmc_rank":5784,"num_market_pairs":1664,"circulating_supply":5023,"total_supply":1931,"max_supply":3985,"last_updated":"2023-02-27T03:48:30.669Z","date_added":"2023-02-27T03:48:30.669Z"........```
- We will parse this later for the info we need from Bitcoin, but for now, just ensuring it connects is enough to move on
- If you'd like to modify the script to include other information, you can find that [documentation here](https://coinmarketcap.com/api/documentation/v1/#section/Quick-Start-Guide)

## Setting up IFTTT :
- Create a free account at [IFTTT's website](https://ifttt.com/)<br>They have a limit of 2 applets you can create for a free account, but we'll only need 1.<br>I'm sure you'll think of plenty of ways to use the other one when working on this project!
- Click the `Create` button on the top
- Click the `Add` button next to `If This`
- Search for `Webhooks` and select it
- Choose the option for Receive a web request with a JSON payload
- Choose the name for your event.  I used `bitcoin_price_tracker` for my project
- Click `Create Trigger`
- Click the `Add` button next to `Then That`
- Search for `Discord` and select it
- Click `Connect` and go through the steps to log into Discord and put it in server you want the messages to appear in.<br>**NOTE: You must have the Manage Server permissions for this to work**
- I chose the option `Post a rich message to a channel`
- From the dropodown, choose the 'Channel' which is actually the server you're connecting to. The dropdown below that is for the channel you would like to add it to.<br>**Note: The bot may need to manually be added to the Discord channel later**
- I am only going to use the `Message` action field, so I am going to delete the info from every other field and enter ```Latest bitcoin prices:<br>{{JsonPayload}}``` as my message.
- Click `Create Action` > `Continue` > `Finish` to complete
- You will also need the key for the webhook.  That can be found by going to the [webhooks IFTTT page](https://ifttt.com/maker_webhooks) and click `Documentation` for the key.
- Save this key and **DO NOT SHARE IT WITH ANYONE!!!**<br>If someone else gets this key they can post to your channel!
- Test the whole thing by using the following code changing:<br>`{event}` to `bitcoin_price_tracker` (or whatever you named the event in the `If This` portion of the IFTTT setup)<br>And `{YourWebhookAPIKey}` to the key we just retrieved.
`curl -X POST -H "Content-Type: application/json" -d '{"this":[{"is":{"some":["test","data"]}}]}' https://maker.ifttt.com/trigger/{event}/json/with/key/b{YourWebhookAPIKey}`
- You will now see `Congratulations! You've fired the bitcoin_price_tracker JSON event` in the terminal and your Discord channel will recieve the message `Latest bitcoin prices:

{"this":[{"is":{"some":["test","data"]}}]}`
- **Note: If this does not work, ensure you have the IFTTT Discord bot in the channel you are trying to message in<br>![alt text](https://i.imgur.com/uAmlIUe.png)


## Python Code
- 