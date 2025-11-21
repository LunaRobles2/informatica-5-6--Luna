def main():
    import requests
    
    print(("🧡 🩷  ")*10)
    print( )
    product_list = ["blush", "lip_liner","lipstick","foundation","eyeliner","eyeshadow","bronzer","mascara"]
    tag_list = ["Canadian","CertClean","Chemical Free","Dairy Free","EWG Verified","EcoCert","Fair Trade","Gluten Free","Hypoallergenic","Natural","No Talc","Non-GMO","Organic","Peanut Free Product","Sugar Free","USDA Organic","Vegan","alcohol free","cruelty free","oil free","purpicks","silicone free","water free"]
    try:
        print("💋💄",product_list)
        product = (input("What type of product are you searching for? "))
        
    except ValueError:
            print("You have to write a product that is in the list")
            return product


    print("💋💄",tag_list)
    tag = (input("What type of free of are you searching for? "))
    response = requests.get ("http://makeup-api.herokuapp.com/api/v1/products.json?product_type="+product+ "&tag_list=" +tag +"&brand=maybelline")

    cof = len(response.json())
    i=0
    while i < cof:
        look = (response.json()[i]["name"])
        print("🌸",look)
        i+=1

    print( )
    print(("🧡 🩷  ")*10)
main()