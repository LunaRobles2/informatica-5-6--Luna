import requests
import json
print(("🧡 🩷  ")*9)

product = (input("What type of product are you searching for? "))
free_list = [
"Canadian","CertClean","Chemical Free","Dairy Free","EWG Verified","EcoCert","Fair Trade","Gluten Free"
"Hypoallergenic"
Natural
No Talc
Non-GMO
Organic
Peanut Free Product
Sugar Free
USDA Organic
Vegan
alcohol free
cruelty free
oil free
purpicks
silicone free
water free
]
free = (input("What type of free of are you searching for? "))
response = requests.get ("http://makeup-api.herokuapp.com/api/v1/products.json?product_type="+free+product+"maybelline")
look = (response.json()["name"]["product_type"]["description"])