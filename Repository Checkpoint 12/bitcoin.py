import requests
print(("⬛")*25)
API_KEY = "27be317712d2e0375eddb213e8dc4cf2fbbbb05662302b9b819757b6f9cb4e8b"
bitcoin = float(input("How many bitcoins did you want to buy? "))
response = requests.get ("https://rest.coincap.io/v3/assets/bitcoin?apiKey="+API_KEY)
bitcon_price = float(response.json()["data"]["priceUsd"])
total = round(bitcoin * bitcon_price, 2)
print(f"Your total will be: 🪙  🪙  🪙  ${total:,.2f}🪙  🪙  🪙")
print(("⬛")*25)