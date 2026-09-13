# website = "fmcodding.com" 
# print(website[0:3])
# print(website[0:3:1])
# print(website[0::2])
# print(website[0::1])
# print(website[::])
# print(website[::-1])
# print(website[2:4])
# print(website[-6:-2])



# w = "websitedevelopment"

# print(w[-1::-1])
name = "Fmcodding Website development"
# print(name.upper())         #  upper case capital letters
# print(name.lower())         #  lower case small letters
# print(name.title())         #  title case first letter of each word capital letters
# print(name.capitalize())    #  capitalize first letter of the string
# print(name.swapcase())      #  swap case upper to lower and lower to upper
# print(name.count("e"))        #  count the number of occurrences of a substring in the string

# print(name.find("Website"))      #  find the index of the first occurrence of a substring in the string
# print(name.index("Website"))     #  find the index of the first occurrence of a substring in the string

# *** find and index me etna  diffirent h ki find method returns -1 if the substring is not found, while the index method raises a ValueError.

# fruits = "  b a n a n a  "
# print(len(fruits))        #  length of the string
# print(fruits.replace("a", "o"))      #  replace all occurrences of a substring with another substring
# print(fruits.strip())   #  remove whitespace from the beginning and end of the string
# print(len(fruits.strip()))        #  length of the string after removing whitespace
# print(fruits.lstrip())  #  remove whitespace from the beginning of the string
# print(fruits.rstrip())  #  remove whitespace from the end of the string
# print("faiyz123".isalnum())  #  check if the string is alphanumeric (contains only letters and numbers)
# print("faiyz".isalpha())  #  check if the string is alphabetic (contains only letters)
# print("123".isdigit())  #  check if the string is numeric (contains only digits)
# print("   ".isspace())  #  check if the string contains only whitespace   (true)
# print("faiyaz".isspace())  #  check if the string contains only whitespace  (false)
# print("faiyaz".isspace())  #  check if the string contains only whitespace  (false)
# print("faiyaz".isspace())  #  check if the string contains only whitespace  (false)
# print("faiyz123".startswith("f"))  #  check if the string starts with a specific substring
# print("faiyz123".endswith("3"))  #  check if the string ends with a specific substring



# isalpha()
# isdigit()
# isdecimal()
# isnumeric()
# isalnum()
# isascii()
# isidentifier()
# islower()
# isupper()
# istitle()
# isspace()
# isprintable()

# strip()	दोनों तरफ से spaces हटाता है
# lstrip()	left side spaces हटाता है
# rstrip()	right side spaces हटाता है
# removeprefix()	शुरुआत का specific text हटाता है
# removesuffix()	अंत का specific text हटाता है


# fruits = "banana,apple,orange  "

# print(fruits.split(","))  #  split the string into a list of substrings based on whitespace

# rsplit()
# splitlines()
# partition()
# rpartition()
# print(fruits.rsplit(","))  #  split the string into a list of substrings based on whitespace, starting from the right


# w = "websitedevelopment"
# for n in w:
#     print(n)

# second metod to print the string with index

# l = len(w)
# for i in range(l):
#     print(i,w[i])



# list and list ke kuch methods 


l = [10,20,30,40,50,60,70,80,90,100]

# print(l[-1::-2])
# l.pop(3)  #  remove the element at index 3 from the list
# l.pop()  #  remove the last element from the list
# l.insert(2, 25)  #  insert the element 25 at index 2 in the list
# l.append(110)  #  add the element 110 at the end of the list
# print(l)

l = [10,20,30,40,50,60,70,80,90,100]
p = [1,2,3,4,5,6,7,8,9,10]
l.extend(p)  #  es sath sare array open ho kr single array ban jata h  apend me aisha nhi hota h 
# print(l)
