birthdays = {
    "Jazmin" : "5 Enero",
    "Rodrigo" : "10 Septiembre",
    "Luisa" : "25 Octubre"
}
print(birthdays)

while True:
    look = input("You are looking for: ")


    if look in birthdays:
        print((birthdays[look]), "is the birthday of", look)
        break

    else:
        print ("I do not have birthday information for", look)
        birthday = input("What is their birthday?")
        birthdays [look] = birthday
        print (birthdays)
