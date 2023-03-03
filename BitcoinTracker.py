##Ensure you replace <YourCMCAPIKey> and <YourWebhookAPIKey> before running this

from requests import Request, Session
import requests
import json
import pprint

#test webhook: curl -X POST -H "Content-Type: application/json" -d '{"this":[{"is":{"some":["test","data"]}}]}' http://maker.ifttt.com/trigger/bitcoin_price_update/json/with/key/<YourWebhookAPIKey>

BITCOIN_API_URL= 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
IFTTT_WEBHOOK_URL = 'https://maker.ifttt.com/trigger/{}/json/with/key/<YourWebhookAPIKey>'


def getInfo (): # Function to get the info

    parameters = { 'slug': 'bitcoin', 'convert': 'USD' } # API parameters to pass in for retrieving specific cryptocurrency data

    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '<YourCMCAPIKey>'
    } # Replace 'YOUR_API_KEY' with the API key you have recieved in the previous step

    session = Session()
    session.headers.update(headers)

    response = session.get(BITCOIN_API_URL, params=parameters)

    global btcPrice

    btcPrice = json.loads(response.text)['data']['1']['quote']['USD']['price']

    btcPrice = round(btcPrice, 2)
    btcPrice = float((f'{btcPrice:.2f}'))
    pprint.pprint(btcPrice) #This tests the price and prints it out in terminal.  You can comment it out when testing is complete

def post_ifttt_webhook(event, value):
    # The payload that will be sent to IFTTT service
    data = {'JsonPayload': value}
    # inserts our desired event
    ifttt_event_url = IFTTT_WEBHOOK_URL.format(event)
    # Sends a HTTP POST request to the webhook URL
    requests.post(ifttt_event_url, json=data)

        
getInfo() # Calling the function to get the statistics
post_ifttt_webhook('bitcoin_price_tracker', btcPrice) # Calling the function to send info to Discord
