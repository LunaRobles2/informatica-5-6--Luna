capitals = {
    "Mexico" : "Mexico City",
    "Canada" : "Ottawa",
    "Brazil" : "Brasilia"
}

capitals["Italy"] = "Rome" #Add a new Key
del capitals["Brazil"] #Deletes Keys
capitals.pop ("Canada")
capitals.clear
print(capitals)

Students = {
    "Hermione" : "Gryffindor",
    "Harry" : "Gryffindor",
    "Ron" : "Gryffindor",
    "Draco" : "Slytherin"
}

for key in Students:
    print(f"{key}: {Students[key]}")
print("-" * 45)
Student = [
    {"name" : "Hermione", "House" : "Gryffindor", "Patronus" : "Otter"},
    {"name" : "Harry", "House" : "Gryffindor", "Patronus" : "Stag"},
    {"name" : "Ron", "House" : "Gryffindor", "Patronus" : "Jack Russell Terrier"},
    {"name" : "Draco", "House" : "Slytherin", "Patronus" : "____"}
]
for element in Student:
    print(f"{element["name"]},{element["House"]}, {element["Patronus"]}")
