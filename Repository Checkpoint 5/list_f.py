#    //    . metodo    //modify the original list//     funcion()     //crate a copy of the list//

my_list = [5, 2, 3, 1, 4]
print(my_list)

#max is to find the greatest number in a list
greatest = max(my_list)
print ("The gresater number in the list is:",greatest)

# min is to find the smallest number in a list
small = min(my_list)
print("The smallest number in a list is:", small)

#sum is to sum all numbers in the list 
list_sum = sum(my_list)
print("The sum of all numbers in the list is:", list_sum)

#To know how many elements are in the list
length = len(my_list)
print("This list has", length, "elements")

#sorted make your list of numbers in order
order = sorted(my_list)
print("The list in order would be:", order)

#
def filter_price (price):
    if (price > 400):
        return True
    else:
        return False

item_price = [230, 400, 450, 350, 370]
filtered_price = filter(filter_price, item_price)
print(list(filtered_price))