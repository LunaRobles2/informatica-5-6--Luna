def main():
    list_length = int(input("Enter the length of a list: "))
    num_list = []

    for number in range(list_length):
        list_element = int(input("Enter element: "))
        num_list.append (list_element)
        file= open("largest.txt","a")
        file.write(f"{list_element}\n")
        file.close()

    print (num_list) 

    large_num = max(num_list)
    print ("The largest number is:",large_num)



main()
