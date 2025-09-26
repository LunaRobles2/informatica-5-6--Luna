birthdays = {
    "Jazmin" : "5 Enero",
    "Rodrigo" : "10 Septiembre",
    "Luisa" : "25 Octubre"
}
print(birthdays)
look = input("You are looking for: ")

if look == "Jazmin" or "Rodrigo" or "Luisa":
    print((birthdays[look]), "is the birthday of", look)
else:
    then_look = input("I do not have birthday information for", look, "What is their birthday?")
    birthdays [look] = then_look
