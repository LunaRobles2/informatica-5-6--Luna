def main():
    import requests
    import json
    print(("🧡 🩷  ")*10)

    product_list = [
    "blush", "lip_liner","lipstick","foundation","eyeliner","eyeshadow","bronzer","mascara"
]
    print("💋💄",product_list)
    product = (input("What type of product are you searching for? "))
    tag_list = [
    "Canadian","CertClean","Chemical Free","Dairy Free","EWG Verified","EcoCert","Fair Trade","Gluten Free","Hypoallergenic",
    "Natural","No Talc","Non-GMO","Organic","Peanut Free Product","Sugar Free","USDA Organic","Vegan","alcohol free","cruelty free",
    "oil free","purpicks","silicone free","water free"
]
    print("💋💄",tag_list)
    tag = (input("What type of free of are you searching for? "))
    response = requests.get ("http://makeup-api.herokuapp.com/api/v1/products.json?product_type="+product+ "&tag_list=" +tag +"&brand=maybelline")

    i=0
    for i in len(response.json()):
        look = (response.json()[i]["name"])
        print(look)
        i+=1

    print(("🧡 🩷  ")*10)
main()