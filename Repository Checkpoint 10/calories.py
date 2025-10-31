def main():
    print("🥛 🍉 " * 10)
    print("Count your calories!!!")
    dic = {
    "Whole milk" : 73,
    "Soymilk" : 30,
    "Yogurt" : 68.5,
    "Yogurt Sour Cream" : 16,
    "egg" : 75,
    "egg white" : 16,
    "Cream Cheese" : 17,
    "Butter regular and salted " : 36,
    "Almonds" : 170,
    "Peanuts" : 166,
    "Black beans" : 113,
    "Pinto beans" : 122,
    "Chicken Wing" : 80,
    "Pork" : 178,
    "Carrots" : 13,
    "Lettuce" : 2,
    "Watermellon" : 11,
    "Banana" : 33
    }

    print(dic)
    x = str(input("Write a food item from the list: "))
    y = str(input("Write another food item from the list: "))
    list = [x,y]

    if x == "Whole milk" or x == "Soymilk" and y == "Watermellon":
        print ("❌Error❌: you cannot mix watermelon 🍉 and milk 🥛")
    elif x == "Watermellon" and y == "Whole milk" or y == "Soymilk":
        print()
    else:
        sum = 0
        for value in list:
            sum += dic[value]
        print("the sum of", x, "and", y, "is", sum)
    
main()