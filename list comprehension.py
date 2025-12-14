#we use list comprehension to create a list of even numbers from the original list
numbers = [1, 2, 3, 4, 5, 6]
even = [x for x in numbers if x % 2 == 0]
print("List of even numbers from original: ", even)



def square(n):
    return n * n

# map in python is an inbuilt function / predefined function which maps any function with a data structure, so the function will run on the values of the data stucture
numbers = (1, 2, 3, 4)
result = map(square, numbers)

print(list(result))
print(square(9))

print("--------------------------------")

list1 = [90,23,87]
list2 = [12,34,7]

sum_lists = map(lambda x,y:x+y,list1,list2)#lambda is a predefined function in python
print(list(sum_lists))



list1 = ["aa","bb","cc"]
list2 = [23,45,56]
my_list = [1,2,3,100,200]
list3=zip(list1,list2,my_list)

print(list(list3))
li4 = list(list3)
li4.reverse()
print(li4)