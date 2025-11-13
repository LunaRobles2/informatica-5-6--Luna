import requests
import json
print(("🩷 ")*25)

product = (input("What type of product are you searching for? "))
response = requests.get ("http://makeup-api.herokuapp.com/api/v1/products.json?brand=maybelline")
look = float(response.json()["name"]["product_type"]["description"])
print(f"Your product is: {look}")
print(("⬛")*25)