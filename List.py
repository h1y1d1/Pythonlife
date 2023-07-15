"""Lists are used to store multiple items in a single variable. In this section we will learn about:

1.) Creating lists
2.) Indexing and Slicing Lists
3.) Basic List Methods
4.) Nesting Lists
5.) Introduction to List Comprehensions
Lists are constructed with brackets [ ] and commas separating every element in the list.

Let's go ahead and see how we can construct lists!"""

#create a list with name of student_names
"""student_names=["shiva","vishwa","akhil","chandu","surya","emma","staine"]
print(student_names)
print(type(student_names))

ms_dhoni = [2011.6,2007,1983]
print(ms_dhoni)
print(type(ms_dhoni))

student_total = ["gopi", 766, "surya", 23, True, False, 56.09, 34.8]
print(student_total)
print(type(student_total))

surya = list([1,2,3,4]) # surya = [1,2,3,4]
print(surya)"""

#name = "surya"
#print(name[2])

#Indexing and Slicing

#Indexing and slicing work just like in strings. Let's make a new list to remind ourselves of how this works:

"""movies = ["RRR", "KGF 2", "Radhe shyam","sita ramam","karthikeya 2","pushpa"]
print(movies)
print(movies[5])
print(movies[2:5])
print(movies[:4])
print(movies[-1])
print(movies[-3])
print(movies[-5:-1])"""

#list methods
"""movies=["RRR", "KGF 2", "RS","sita ramam","karthikeya 2","pushpa"]
movies.append("spy")
movies.append("salaar")
movies.append("RRR")
#movies.append(["surya","chandana"])

movies.insert(2,"project k")
movies.insert(5,"animal")
#print(movies)

trash=movies.remove("spy")
print(trash)
movies.remove("RRR")
#print(movies)

trash_bin = movies.pop()
print(movies)
print(trash_bin)
#movies.clear()
#print(movies)
list1= ["surya",2,3,4]
list1.pop(0)
print(list1)"""


movies=["RRR", "KGF 2", "RS","sita ramam","karthikeya 2","pushpa"]
movies.sort()
print(movies)

numbers = [3,5,5,9,6,1,1,2,2,7,6,9,23,23,43,21]
numbers.sort(reverse=True)
print(numbers)

#mobiles =["1 plus","oppo","samsung","Apple"]

mobiles =["Apple","Apple","Apple","samsung",["1 plus","oppo"]]
print(mobiles[2][0])

print(mobiles.count("Apple"))

list1= [1,2,3]
list2= [ "surya ", "python "," life "]
print(list1)
list1.extend(list2)
print(list1)
print(len(list1))