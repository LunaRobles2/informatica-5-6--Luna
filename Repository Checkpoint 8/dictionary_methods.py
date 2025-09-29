dictionary = {
    "Color" : "Blue",
    "Age" : "17"
}

#Values
print(dictionary.values())
for v in dictionary.values():
    print(v)

#keys
print(dictionary.keys())
for k in dictionary.keys():
    print(k)

#items
print(dictionary.items())
for i in dictionary.items():
    print(i)

#print key and value using methods
# to do

picnic_items = {"apples" : 5, "cups" : 2}
print (f"I'm bringinng {picnic_items.get("cups")} cups.")

print (f"I'm bringinng {picnic_items.get("eggs", 0)} eggs.")

#setting Default Values
pet_info = {
    "name" : "Kenji",
    "Age" : "5"
}

pet_info.setdefault("color", "Black")
pet_info ["color"] = "Black"
pet_info.setdefault("color", "White")
print(pet_info)