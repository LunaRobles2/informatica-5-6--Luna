def main():
    print("The length of your list is:",(length(values())))
    print("The mean of your list is:", (mean(values())))

def values():
    value_list = []
    while True:
        value = int(input("Enter a number to add to the list: "))
        if (value !=0):
            value_list.append(value)
            print ("in the order the items were added:", value_list)
            order = sorted(value_list)
            print ("The ordered from smallest to greatest:", order)
            
            continue
        else:
            break
    return (value_list)
    

def length(list):
    return len(list)

def mean(list):
    return (sum(list) / len(list))

def range(list):
    print("The range of your list is:", (max(list) - main(list)))
        

main()