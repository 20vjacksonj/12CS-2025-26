'''
dictionaries are data structures that store values in key: value pairs
keys are case sensitive
keys must be imutable
duplicate keys are not allowed 
internally uses hashing
'''

#creating dictionary
my_dict = {
    "name" : "Jacob",
    "age" : 17,
    "is_student" : True,
    "courses" : ["maths", "computer science", "geography"],
    "address" : {
        "city" : "New york",
        "zip" : "10001"
    }

}


#accessing values
name = my_dict["name"] # accessing using key
print(name)
age = my_dict.get("age") #accessing using get() method
print(age)



#updating existing elements
my_dict["age"] = 18 #updating age
my_dict["is_student"] = False #updating is_student
#adding ney key:value pair
my_dict["graduation_year"] = 2022
print(my_dict)



#deleting elements from a dictionary: del and pop()
#with del, key must exist, or Keyerror
del my_dict["address"] #using del
print(my_dict) 

#using pop() method
#removes key and returns value
#with  pop(), key must exist, or Keyerror
removed_course = my_dict.pop("courses")
print(my_dict.pop("new", "not found"))



#traversing a dicitonary
#iterating through a dictionary
for key, value in my_dict.items():
    print(f"{key}:{value}")

#checking if key exists
if "name" in my_dict:
    print("Name exists in the dictionary")

#getting all keys and values 
keys = my_dict.keys()
values = my_dict.keys()

#clearing a dictionary
#my_dict.clear()
print("Final dictionary: ", my_dict)



#dictionary functions and methods
#length of dictionary
length = len(my_dict)
print("Length of dictionary: ", length)

#copying a dictionary
copy_dict = my_dict.copy()
print("Copied dictionary: ", copy_dict)

#merging two dictionaries
dict1 = {
    "a" : 1,
    "b" : 2,
    "c" : 3
}

dict2 = {
    "d" : 4,
    "e" : 5,
    "f" : 6
}

dict1.update(dict2) #merging dict2 into dict1
print("Merged dictionary: ", dict1)



keys = ["x", "y", "z"]
new_dict = dict.fromkeys(keys, 0) #all keys initialsed to 0 
print("Dictionary keys: ", new_dict)

#setting default value 
default_value = my_dict.setdefault("new_key", "new_default")
print("Set default value: ", default_value)
print("Final dictionary state: ", my_dict)



#output inital dictionary
print("Initial dictionary", my_dict)
print("Name: ", name)
print("Age: ", age)
print("Updated dictionary: ", my_dict)
print("Removed course: ", removed_course)
#output keys and values
print("Keys: ", list(keys))
print("Values: ",list(values))

#clear method removes all values from a dictionary
#print(my_dict.clear())

#get method returns the item with the key
my_dict.get("name")

#items method returns all values in no particular order as (key, value)
my_list = my_dict.items()
for x in my_list:
    print(x)

#keys method returns all values in no particular order as a sequence of keys
my_list = my_dict.keys()
for x in my_list:
    print(x)

#values returns all values
my_list = my_dict.values()
for x in my_list:
    print(x)