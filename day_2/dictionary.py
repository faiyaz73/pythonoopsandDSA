# dic ={
#     "name": "John",
#     "age": 30,
#     "city": "New York" 

# print((dic["name"]))
# (dic["age"]) = 31  #  update the value of the key "age" in the dictionarypython dictionary.py
# print((dic["age"]))

# for key in dic:
#     print(key, dic[key])  #  print the key and its corresponding value in the dictionary

# for key in dic.keys():
#     print(key)  #  print all the keys in the dictionary
# for value in dic.values():
#     print(value)  #  print all the values in the dictionary
# for items  in dic.items():
#      print(items)  #  print all the key-value pairs in the dictionary as 
# for keys, values in dic.items():
#     print(keys, values)  #  print all the key-value pairs in the dictionary with keys and values separated
# dic.pop("age")  #  remove the key "age" and its corresponding value from the dictionary
# print(dic)  #  print the updated dictionary
# dic.clear()  #  remove all the key-value pairs from the dictionary
# print(dic)  #  print the empty dictionary


to = (1,6,65,43,23,45,67,89,90,100)
# to[0] = 10  #  this will raise an error because tuples are immutable and cannot be modified after creation

# print(to.index(65))  #  this will return the index of the value 65 in the tuple

user=("faiyaz", "24", "ghaziabad")  #  create a tuple with three values
name ,age, city = user  #  unpack the tuple into separate variables
print(name)  #  print the value of the variable name
print(age)   #  print the value of the variable age
print(city)  #  print the value of the variable city