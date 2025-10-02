def character_counter (message, dictionary):
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary [character] += 1

    print(dictionary)

    print(sum(dictionary.values()))

    print("-" * 45)
    #Alternative 1
    print("#Alternative 1")
    vlalues_list = list(dictionary.values())
    print(vlalues_list)
    largest_number_index = vlalues_list.index(max(vlalues_list))
    repeted_character = list(dictionary.keys())[largest_number_index]
    print(f"The most repeted character is: {repeted_character} , repeating {dictionary[repeted_character]} times")

    print("-" * 45)
    #Alternative 2
    print("#Alternative 2")
    largest_number2 = max(dictionary, key = dictionary.get)
    print(f"The most repeted character is: {largest_number2} , repeating {dictionary[repeted_character]} times")

message = input("Write a message: ")
print("-" * 45)
dictionary = {}
character_counter(message, dictionary)
