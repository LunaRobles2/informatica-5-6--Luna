def character_counter (message, dictionary):
    for character in message:
        dictionary.setdefault(character, 0)
        dictionary [character] += 1

    print(dictionary)

    print(sum(dictionary.values()))

    #Alternative 1
    vlalues_list = list(dictionary.values())
    print(vlalues_list)
    largest_number_index = vlalues_list.index(max(vlalues_list))
    repeted_character = list(dictionary.keys())[largest_number_index]
    print(f"The most repeted character is: {repeted_character} , repeating {dictionary[repeted_character]} times")

message = input("Write a message: ")
dictionary = {}
character_counter(message, dictionary)
