# print statements

# print("im begining tolearn", 7)
# print(13*45)
# print ("i think i know it but \nthis is how you chsnge lines", " you type \n . ")
# print (" Hey im a \"good boy\" as they say")  
# print("hey",6, 7, 8 , sep="~", end="009") # sep=~ is used to separate as separator between the printed characters
# print("hero")

 # use end=(something) to not go to next line which is default action and continue with the line 
#using separation as "Something"
''' use \" to print " in outputcuz interpreter cant tell differecne if 
it is indicating the end of a string or if it is there to be printed
this also works for single ' you'll have to use  \' 
''' 
#use \n to move to print in next line
#  this to comment 
# ctrl + / to comment or  uncommnet  multiple lines 
''' by using tripple ' you can perform 
multiline comments'''
# alt + up / down key to move a full  line 


#variables and data types

# a="buck"
# b = True 
# c =  4
# d = None 
# e = complex(8, 2)
# print(e)
# print("The type of a is ", type(b))

# list1 = [1 , 4, 4.5 , [-4, 6] , ["apple" , "pink"]  ]
# print(list1)
# # it is mutable(can be changed )
# tuple1 = (("mangoes","oranges"), ("gang ","one"))
# print(tuple1)
# # it is not mutable 
#  # mapped data type
# dict1 = {"name": "ashu" , "age":"20" , "isleadr ": True }
# print(dict1)


# new Operators 

# print (15/4)
# print (15//4)
# print (14//5)
# # floor division operator - it removes the last decimal and returns lower closest number cuz of floor
# print(5**3)
# raises power , here 5 is powered by 3 
#rest operators you know already


#Type casting 

#Explicit typecasting 
# a = "1"
# b = "5"
# print (int(a)+int(b)) # int()function converted string to integer 
# print ( a + b)

# #Implicit type casting
# c = 9
# d = 1.5 
# print (c + d ) # the integer c is implicitly converted to double data type by python 


#Taking inputs

# a = input("Enter your name :")
#  # default input is in string form , you can print a statement while taking an input 
# print("My name is",a)
# b = input ()
# c = input()
# print (b+c)
# print(int(b)+ int(c)) 
# you 'll have to convert it to integer to perform integer calculations


# Strings 


# apple = ''' hello harry 
#  nice to met you 
#  "i want to eat an apple " 
#  how are you doing '''
# print (apple)
# # ''' ''' (triple single quotes)  ,the things iniside thids will be considered strings ,
# # this is used to print multiline strings
# #  these can also be used 
# # to print " " in the  output 
# print(apple [31])
# # in python the string is llike an array of characters 
# for character  in apple :
#     print(character) 
# loop in a string 

# names = "ashutosh , infinity" 
# print(names[0:12]) #starts counting from 0 and goes till 9 ,but doesnt includes 9 
# print (len ( names)) 
# print (names[:6]) # [] is used for slicing  , 0 is predefined if you didn't put it 
# print(names[0:-5]) # it subtarcts 5 form the total length of the string
# print(names[-5:-1]) # the indexes are counted from length of string -5 till length of string-1 

# print(names.upper()) # Strings are immutable , it cannot be changed 
# # here the function creates a new string and then prints 
# print(names.lower())
# a = "!!Ashu !!!! <<<"
# print(a)
# print(a[:-4].rstrip("!")) # strips rear trailling characters 
# #doesnt do anything to front or middle trailing characters hence i used -4 to remove last trailing characters
# print(a.replace("!",">"))
# print(a.split(" ")) # here the space is used as variable to identify and separate strings 
# b = "ashutosh Is a Not a Bad Person"
# print(b.capitalize()) # capitalises the first letter and conveerts everything else to lower case 
# print(len(b))
# print(b.center(60))# moves the string to the centre with repect to the input 
# print(len(b.center(60)))
# print(b.count("as"))
# print(b.endswith('n')) # return true or false 
# print(b.endswith("ot", 8, 17)) # it can check within an input subset 
# print(b.find("Noh"))
# print(b.isalnum()) # checks if the string is alphanumeric or not(it has only alphabts or numbers)
# print(b.isalpha())# checks if the string has only alphabets - now it is giving false cuz of the spaces
# print(b.islower()) # checks if all the values are lower case
# c= "this is spartan \n"
# print(c)
# print(c.isprintable()) # it prints false cuz \n doesnt print on output
# d= "   "
# print(d.isspace()) #if there is any character other than space it'll return false
# e = "This Is Not Good"
# print(e.istitle()) # returns true only if all the words in the string are capitallised
# print(e.isupper())
# print(e.startswith("T"))
# print(e.swapcase())
# print(e.title()) # converts to title - Capitslizes every word in the string 


# If Else statements

# a = int( input("Enter your age :"))
# if(a < 18): # semicolon is important 
#  print("you cannot drive") # space before execution statement is important , it indicates the level of indent , the space is like curly brackets in java
# elif(a==18): # you can make nested if simailarly to java 
#  print("just turned 18 bitch ")
# else : 
#  print("you can drive")
#  print ("you are gay  ")


# Match case statement 


# x = int(input("Enter the value of x : "))
# match x :
#  case 1 :
#    print("x is one ")
#  case 2 :
#   print( "The number was 2 ")
#  case 3 : 
#   print("case is 3 ") 
#  case _ if x!= 10:
#   print( x, "is not 10")
#  case _ if x == 10 :
#   print( x ,"is 10 ")
#  case _ if x < 10 :
#   print( x, " is smaller than 10 ")
#  case _ :
#   print( x)
# break is not needed  , if the case matches the code runs leaving the others 
 
 
# LOOPS - for loops and while loops


# name = "ashutosh"
# for i in name :
#     print (i)
#     if(i== "b") :
#         print("i found a b ")

# colours = ["Red","Green","Blue", "Orange"]
# for c in colours :
#     print(c)
#     for i in c :
#         print(i)     

# for k in range(7) : 
#     print(k)
# for p in range (0,21,2) : # range doesn't takes in last one , the third parameter tells how many numbers to skip after every number
#     print(p*2)

# While loop

# i= 0  #for while loop you'll have to  initialise the variable
# while(i<=3) : # you can create an infinite loop  with this
#     print(i)
#     i=i+1 
# else:  # while doesn't need else statemen 
#     print("nothing is true ")

# Break and continue statemet 

# for  i in range (12):
#     print(i*5 )
#     if(i== 8):
#         break  # completely stops the loop
# print("loop ended at i = " , i )

# for  i in range (12):
#     if(i== 8):
#      print("You shouldn't find  " , i*5 )
#      continue   # just skips the particular iteration , starts next iteration and leaves what was next 
#     print(i*5 )

#simulating do while in python 
# i= int(input())
# while(i>50) :
#     print(i)
#     i= i-1 
# print (i)

# i= int(input())
# for p in range(i , 50):
#     print(i)
#     if i >50 :
#         i = i-1 
#         continue 
#     else :
#         break 

# i= int(input())
# while True :
#     print(i)
#     i= i+1 
#     if(i >100 ):
#         break 


# FUNCTIONS


# def mean (a,b):  # syntax : def function_name () : 
#     gmean  = (a+b)/2 
#     return gmean 
# print( mean(8,9))

# def passing ():
#     pass # if i decide to write the function later and but let the code run for now , th keyword "pass" helps pass incomplete function 


# def average (a=2, b = 5): # here 2 and 5 act as default values , if a parameter is not passed then these default values are used for calc
#     print("the average is : " , (a+b)/2)
# average (b=8) # if you just put values then the values will be assigned according to their position , 
# # if you dont assign default values then the code won't run without assigning values , but if you do it'll go anyways with the default values

#function for user defined numbers of input 

# def avg(*numbers) : # numbers is a touple - you can input as many numbers as you want 
#     sum=0 
#     for i in numbers :
#         sum = sum + i 
#     average = sum / len(numbers)
#     print(average)

# avg(5, 5, 8,9,0,2,5 )


# Lists
 
# lis = [ 2,4,6, "Ashu" ] # syntax : list_name = [*values within square brackets separated by , (coma)] 
# # you can insert any type of values in a list
# print (lis[2]) # the index of the variable starts from 0 
# print(lis[-3]) # it counts from backwards , len(lis) - the_variable 

# if "Ashu" in  lis : # you can check any variable with this method
#     print("it is ")
# else :
#     print("It isn't")

# print(lis)
# print(lis[:]) # you can directly print whole list like this or even  print(lis) 
# print(lis[0:-1]) # -1 is the stop limit
# print(lis[0:3:2]) # 2 is the jump index 

# lst = [i**i for i in range (13)] # th i**i part cna be modified into any complex equation
# print(lst) 
# lst = [i**i for i in range (13) if i%2==0 ]  # you can put any condition 
# print(lst) 


# Manipulation of lists 


# l = [2,4,5,6,6,74,5,4,5]
# l.append(56) # to add a variable at the end of the list 
# print (l)
# l.sort() # to sort a list
# print(l)
# l.sort(reverse =True) # to reverse sort a list 
# l.reverse()# reverses a list
# print(l)
# print(l.index(4)) # returns first index 
# print(l.count(4)) # counts number of times of occurence of a variable 

# #if you do
# #m = l  
# #l[0] = 3 
# #print(l)
# # it changes the "l" list cuz it is the reference 
# # Hence you have to use copy function 
# m = l.copy()
# m[0] = 5 
# print(l)
# print(m)

# l.insert (3,56) # inserts the variable 56 at the position 3 
# print(l)

# l = [2,4,5,6,6,74,5,4,5]
# m = [9, 0 ,7,455,45,46,644 ]
# l.extend(m) # extends and adds variables of m to list l 
# # or k = l+m 
# # print(k )

# TUPLES - similar to list , its just that you can't change it 

# tup = ( 1,13,7,4,5,"it accepts string values too") # enclosed within ( )
# # tup[0] =  7 , this can't be done 
# print (len(tup))
# print (tup)
# print(tup[5])
# if 13 in tup :
#     print("It does")
# tup2 = tup[1:6]
# print(tup2)

# # operations in tuple

# tuple1 = (1,2,3,4,5,6,7)
# tuple2 = (8,9,0)
# tuple3 = tuple1 + tuple2
# print (tuple3)
# res = tuple3.count(4) # counts the number of input variables 
# print(res)
# res2 = tuple3.index(4) # gives index of input
# print (res2)
# res2 = tuple3.index(4,3,8) # starts searching for 4 , form 3 and goes upto 8th position 
# resl = len(tuple3)

# def tuple_to_string (t):
#     return[*t]
# # converts tuple to list
# print(type(tuple_to_string(tuple3)))


# import time
# t= time.strftime('%H:%M:%S') # time.strftime returns time 
# hour = int(time.strftime('%H'))
# print( hour)

# KBC in pyhton 
# ques = ["what is the name of the creator of this game","dogs or cats","beach or mountains"]
# options = ["a","b","c-both", "d-none of the above"]
# ans = ["ashutosh", "d","b"]
# for i in range(int(len(ques))):
#     print(ques(i))
#     print(options)
#     if (): 
#         print("It is the correct answer")
        
    
# sen = "Hey my name is {0} and i am from {1}" 
# country = "india"
# name = "ashutosh "
# print(sen.format(name,country)) # .format puts the variables in place according to the number in the brackets
# print(f"Hey my name is {name} and i am from {country}")
# print(f"Hey my name is {{name}} and i am from {country}")           # syntax: print(f"")
# # Anything can be calculated or put within the curly brackets 
# pie = 22/7 
# print(f"the value of pie closse to 2 decimal places is : {pie:.2f}") # By using :.2f it will acess only digits upto 2 decimmal places ,
# # but :.2f only works in (f"")

# def square(n):
#     '''doc string should be written jsut after declaring the function'''
#     print(n**2)
# square (5)
# print(square.__doc__) # the syntax is: function_name .__doc__
# # the difference between a doc and a comment is that a comment gets ignored completely but a doc string can be printed 


# RECURSION


# def factorial(n) :
#     if(n<=1):
#         return (1)
#     else :
#         return (n * factorial(n-1))
# #print(factorial(5))   

# def fibo(n):
#     if n==0:
#         return 0 
#     elif n == 1:
#         return 1
#     elif n == 2:
#         return 1
#     else:
#         return (fibo(n-1) + fibo(n-2))
# print(fibo(6))



# SETS


# s = {1 ,2,3,4,2,34,5,45,3,5,4,5,89} # it doesnt registers repeated values , it is made by curly brackets 
# print(s)
# s1 = {"clara","meh", "in", 89, 29, False, 12.5} # it can take multiple data types 
# print(s1) # it doesn't maintain order 
# hary = set() # to make an empty set you use set() & not set{} , set{} is an empty  dict & not set
# print(type (hary))
# # manipluation of sets
# print(s.union(s1)) # values of s1 and s remains unchanged
# # to change s 
# #s.update(s1) # adds all unique values of s1 in s
# s2 = s.union(s1)
# s3 = s.intersection(s1)
# print(s3)
# s.intersection_update(s1) # changes s to  a set where only intersecting values are present
# print(s) 
# s4 =  s.difference(s1)# returns the intersection
# s1.difference_update(s)  # updates s1 to the intersection of s1 and s 
# s5 = s1.symmetric_difference(s) # gives s1(union)s - s1(intersection)s
# print(s5)

# print(s.isdisjoint(s1)) # returns true if no elements are common 
# print(s.issuperset(s1)) # returns true if all the elemnets of s1 are present in s 
# print(s.subset(s1))  # returns true if all the elemnets of s are present in s1
# s.add("anything you wwant to add") # adds a variable to the set 
# s.remove("anything you wwant to add") # to remove anything from a set use set_name.remove() or set_name.discard() function 
# # if you use remove it'll show error and the code won't run further if the element wasn't present  but 
# # discard doesn't showa any error
# item = s1.pop() # pop function returns last variable in the set but we cant know which element cuz sets dont maintain order 
# print(item)
# # del s - this function delets the entire set 
# s.clear() # makes the set an empty set , delets all values inside set 

# if 2 in s : # in function can be used to check if a variable is present in the set 
#     print (" 2 is present")


# Dictionaries 


# dic = {"me":"ashutosh",
#         "profession":"king",
#         "will he be able to":"for sure"
#         ,2032 : "turned truth"} # it can go multiline 
# print(dic)
# print(dic["profession"])
# #print (dic[2031]) - throws error if not found
# print(dic.get(2031)) # - gives none as output  if not found
# print(dic.keys()) # returns the keys of the dictionary
# for key in dic :
#     print(f"The values corresponding to key {key} is {dic[key]}")

# print(dic.items())

# ep1 = {122:45, 123:67 , 124:5,125:46}
# ep2 = {234:56 , 235:40 , 236:45}
# ep1.update(ep2) # adds all values of ep2 to ep1
# empt = {}  # empty dictionary 
# ep1.pop(123) # removes calue of 123 
# ep1.popitem() # removes the last keyword pair 
# # del ep1 # delets the entire detionary 
# del ep1[122] # delets the particular key 


# for i in range (100):
#     print(i )
#     i = i+1
#     if i>=10:
#         break
# else : # the else statement executes only when the for loop is completed , otherwise it doesn't executes  
#     print("the loop stopped at" , i+1 )

# i=0
# while i< 16 : 
#     print(i)
#     i = i+1 
#     if i == 13 :
#         break
# else :
#     print("the code reached end")


#  Exeption handling

# a = input("Enter the number : ")
# print ("Multiplication table of {a} is ")
# try:
#     for i in range (1,11) :
#         print(f"{int (a)} X {i} = {int (a )*i}" )
# except Exception as e :
#     print(e)

# print("some important lines of code ")
# print("end of code")


# a = input("Enter the number : ")
# print ("Multiplication table of {a} is : ")
# try:
#     for i in range (1,11) :
#         print(f"{int (a)} X {i} = {int (a )*i}" )
# except:
#     print("some error occured")

# print("some important lines of code ")
# print("end of code")

# handling different types of errors
 
# try:
#     num= int(input("enter an integer :"))
#     a = [3,7]
#     print(a[num])
# except ValueError :  # there are various keywords for various types of errors 
#      print("the input wasn't integer ")
# except IndexError:
#     print("Index error")


# Finally clause 

# def fun() :
#     try:
#         l = [1,3,5,6,7,9]
#         i = int(input("Enter the index :"))
#         print(l[i])
#         return 1  
#     except :
#         print("Some error occured ")
#         return 0 
#     finally :
#         print("i will execute anyways")
# x = fun()
# print (x)

# Custom Errors 

# i = int(input("Enter the number :"))

# if(i<5 or i>9) : 
#     raise ValueError("value should be between 5 and 9 ") 
# # it throws an error so that the execution doesn't continues with a wrong value


# i = input("Enter the word :")

# if(i != "quit") :
#     raise ValueError("The input wasn't quit") 


## Short hand if else 

# a = 330
# b= 330
# print("A")if a>b else print("=") if a == b else print("B") 
# c = 9 if a>b else 0 
# print(c)


# # Enumerate function 
# marks = [6,67,674,5,4554,345,54,657,34]
# for i, marks in enumerate (marks, start = 1 ) :     # i acts as a counter if the keyword enumerate is used  , start is a  keyword if tou dont wnt to start counting from 0
#     print(marks)
#     if (i  == 4):
#         print("Highest number here ")


# Import in java 

# import math 
# print(math.floor(7.9))
# print(math.sqrt(81))

# from math import sqrt , pi # to import only specific functions
# print(7*pi)
# print(sqrt(94))

# from math import sqrt as s, pi # to call function by assigning a name to it 
# print(7*pi)
# print(s(94))

# from math import * # to import everything 
# import math
# print(dir (math))
# print(math.nan,type(math.nan ))
# you can  import anything from other files as well like this

# import importing 
#  # importing runs the all function in package which is being imported
# importing.welcome () 


#  OS module in Python

# import os  - done in experimentation folder


# Global and local variables 

# x = 10
# def fun():
#     global x   # it acesses the global value of x and it can be changed now  
#     x= 3
#     y = 6 
#     print(y)
# fun()
# print(x)
# #print(y) # if i print it will show error cuz y defined earlier is a local varialble within a function 


# File handling in Python 

# f = open('testing.txt','r')
# # syntax :f = open('file_name','r') , here you can read using 'r' , write using'w' and append (add) someting by 'a' 

# text = f.read()
# print(text)
# f.close() # close is important
# # if you open a file in write mode which doens't exists then it will be created 

# with open('testing.txt','a') as f :
#     f.write("Hey this is an update")


# f = open('testing.txt','r')
# while True :
#     line = f.readline()
#     if not line :
#         break
#     print(line,type(line))

# f = open('writingtest.txt','w')
# lines = ['line 1 \n','line 3 \n','line 3 \n'] # while writting it doesnt goes to next line for that you'll have to use "\n"
# f.writelines(lines)
# f.close()


# with open('testing.txt','r') as f :
#     print(type(f))
#     # Moves to the 12th byte in the file
#     f.seek(12)
#     # reads the next 5 bytes
#     print(f.tell()) # tell functions tells where the cursor is positioned , or where it is seeked , from which position it will start reading
#     data = f.read (5)
#     print(data) 


# with open('sample.txt','w') as f :
#     f.write("Hello mf")
#     f.truncate(5)

# with open('sample.txt','r') as f :
#     print(f.read())


# double = lambda x : x*2  # a lambda function is a single line function in order to make the code smaller 
# print(double(3))
# avg = lambda x,y,z : (x+y+z)/3
# print(avg(3,5,7))

# def appl(fx,value) :  # you can pass a function from a function
#     return 6 + fx(value)

# print(appl(double, 8))
# # which can also be written as 
# print(appl(lambda x : x*2 , 8))  # one line functions come handy  at these types of operations 
# print(appl(lambda x : x*x , 8))




#  MAP

# def cube(x):
#     return x**3 
# l = [2,4,5,3,3,5,6,8]
# # to create the cube ofwhole list :
# ''' newl = []
# for itmes in l 
# new.append(cube(item))
# '''
# # but with map  it is like
# newl = map(cube,l) # a map maps evry element into the function and maps them back into the list 
# # can also be written as map(lambda x : x**3,l) 
# print(list(newl))  # the map object ha to be converted into a list 

# #  FILTER 
# def a_boolean_func(x):
#     return x > 5 
# newll = filter (a_boolean_func , l) 
# # filter function passes every value through a boolean function and if the func returns true the value remains else the value is filtered out
# print(list(newll)) # the filter type has to be converted intro list type 
# # it can be also written as 
# print (list(filter(lambda x : x>4, l)))

# from functools import reduce  # reduce has to be imported 

# sum = reduce (lambda x ,y : x*y , l ) 
# #  reduce functoin keeps on reducing first two consecutive values till there is only 1 value which is the result , with the function which has been feeded
# # here it first multiplies first two values and then the result(cuz result will become the first value after computation) with the next value and so on 
# print(sum) 


# class person : # user defined objects are make by using keyword class 
#     name = "ashu"  # default values will be printed if no new values are feeded 
#     occupation = "king"
#     networth = "limitless"  
#     def info(self):
#         print(f"{self.name } is a {self.occupation} with net worth of {self.networth}")

# a = person() # initialise the object with a variable 
# print(a.occupation, a.name,a.networth)
# a.networth = "infinite potential "
# print(a.occupation, a.name,a.networth)
# a.info()

# class person : # user defined objects are make by using keyword class 
#     def __init__(self,n,o):  # this runs every time an object is made
#         print("hey this is running")
#         self.name = n 
#         self.occ = o 
#     def info(self):
#         print(f"{self.name} is a {self.occ}")

# a = person("ashu", "king" )
# b= person( "kohai","assist")
# c= person()
# a.info ()
# b.info()


# DCEORATORS 

# def greet(fx):
#     def mfx( *args , **kwargs):
#         print("Morning King")
#         fx(*args , **kwargs)   # here the function is executed here  after printing 
#         print("Geting back to conquer")
#     return mfx

# also can be written as greet(hello)() - here if any value have to be passsed then it will not reach the function 
# @greet  # decorator - gives the function to the decortaing function and then it is executed  according to that function 
# def hello():
#     print("wish my lord ")

# hello()

# @greet
# def sqrt(x):
#   print( x**(1/2))

# sqrt(9)


# class MyClass :
#     def __init__(self,value):
#         self._value = value
#     def show(self) :
#         print(f"value is {self._value}")

#     @property  # getter - gets a value 
#     def ten_value(self):
#         return 10*self._value

#     @ten_value.setter  # works a a function to set a value in a function
#     def ten_value(self,new_value):
#         self._value = new_value/10
# obj = MyClass(9)

# print(obj.ten_value)
# obj.show()


# INHERITANCE

# class employee :
#     def __init__(self,name,id):
#         self.name = name 
#         self.id = id  
#     def showDetails(self ):
#         print(f"The name of the employe {self.id} is {self.name} ")

# class progmeer (employee):
#     def showLang(self):
    
#         print(" uses python to code")

# e1 = progmeer("ranchor das",894)
# e1.showDetails()
# e1.showLang()

# class employee :
#     def __init__(self,name,id):
#         self.name = name 
#         self.id = id  
#     def showDetails(self ):
#         print(f"The name of the employe {self.id} is {self.name} ")

# class progmeer (employee):
#     def showLang(self, lang ):
#         self.lang = lang
#         print(f" uses {self.lang} to code")

# e1 = progmeer("ranchor das",894 )
# e1.showDetails()
# e1.showLang("python")


# Public , private  , protected 

# in a class anything with self is at default as public 

# class employee :
#     def __init__(self) :
#         self.name = "ashu"

# a = employee()
# print(a.name)
# PRIVATE 
# class employee :
#     def __init__(self) :
#         self.__name = "ashu"  # the (__) double underscore indicates the private variables and these variables cannot be acessed directly 

# a = employee()
# #print(a.name)
# print(a._employee__name) # the term "_employee"  has to be used in order to access the variable if __ is used in it 
# #print(a.__dir__())


# # To get a random integer 
# import random
# print(random.randint(-1,9))

# #  STATIC METHODS
# class Math :
#     def __init__(self,num) :
#         self.num = num

#     def addtwonum(self,n) :
#         self.num = self.num + n 
#     @staticmethod        # for a static method self keyword is not necessary 
#     def givingpower(a,b):
#         return a**b
    
# a = Math(7)
# print(a.num)
# a.addtwonum(9)
# print(a.num)
# print(a.givingpower(5,3)) 

# class Employee:
#     companyName = "Appul"  # class variable acts as default variable until specifically chnaged for a particualar instance 
#     def __init__ (self,name):
#         self.name = name
#         self.appreiation = 0.1
#     def showDetails (self):
#         print(f"{self.name} in the company {self.companyName} got a raise of {self.appreiation} ")

# emp1 = Employee("ashu")
# emp1.appreiation = 0.5 
# emp1.companyName = "Appul India "
# emp1.showDetails()

# Employee.companyName = "gogol"
# print(Employee.companyName)

# emp2 = Employee("yoges")
# emp2.showDetails()


# class Employee:
#     company = "Appul" 
#     def show (self):
#         print(f"{self.name} in the company {self.company} ")

#     @classmethod   # this decorator allows method to acess / changes class variable in the method itself , else the change would have been just for the instance and not for class 
#     def changeCompany(cls, newCompany):
#         cls.company = newCompany

# emp1 = Employee()
# emp1.name = "pegasis"
# emp1.show()
# emp1.changeCompany ("Appul India")
# emp1.show()
# print(Employee.company)


# class Emploee:
#     def __init__(self, name, salary) :
#         self.name = name
#         self.salary = salary 

#     @classmethod
#     def fromStr(cls , string):
#         return cls(string.split("-")[0],int(string.split("-")[1]))

# e1 = Emploee("harry puttar",30000)
# print(e1.name,e1.salary)

# string = "john wick - 150000"
# e2 = Emploee.fromStr(string)
# print(e2.name,e2.salary)


# DIR , DICT and HELP 

# x = [7,9,5,3]
# print(dir (x))  # to show the directries and functions that can be run currently
# print(x.__hash__)
# print(x.__doc__)


# class person:
#     def __init__(self,name,age):
#         self.name = name 
#         self.age  = age
#         self.version = "updating "

# y= person("yamini", 83)
# print(y.__dict__)     # __dict__ to print as a dictionary 


# print(help(person)) 
# print(help(str))
# # the help method is used to get helpdocumentation for an object , including a description of its attributes and methods  

# class employee:
#     def __init__(self,name,id) :
#         self.name  = name
#         self.id = id

# class programmer(employee):
#     def __init__(self, name, id,lang):
#         super().__init__(name, id)  # the keyword supper is used to acess the parent class 
#         self.lang = lang

# happy = employee("happy singh ", 567)
# happy2 = programmer("happy singhania ",7,"cobra")

# print(happy.name,happy.id)
# print(happy2.name,"of id",happy2.id,"uses",happy2.lang,"to code")



#  METHOD OVERRIDING 

# class shape :
#     def __init__(self,x,y) :
#         self.x = x
#         self.y = y

#     def area(self):
#         return self.x*self.y

# class circle (shape):
#     def __init__(self, radius):
#         super().__init__(radius , radius)

#     def area(self):
#         return 3.14 *super().area()

# a = circle(67)
# print(a.area())


# EXERCISE
# problem statement - rename all the png files from 1 uptil n as 1.png uptil n.png . and do the same for other file 

#  OPERATOR OVERLOADING 

# class vector :
#     def __init__(self,i,j,k) :
#         self.i = i
#         self.j = j
#         self.k = k
#     def __str__(self):
#         return f"{self.i}i + {self.j}j + {self.k}k"
#     def __add__(self , x):
#         return vector(self.i + x.i, self.j+ x.j ,self.k+x.k)
# v1 = vector(3,4,5)
# print(v1)
# v2 = vector(7,2,3)

# print(v1 + v2) # the + in this calculation is interpreted to __add__ , htis is known as operator overloading


# MULTIPLE INHERITANCE 

# class employee :
#     def __init__(self,name) :
#         self.name = name
#     def show(self):
#             print(f"the name is {self.name}")

# class dancer :
#     def __init__(self, dance) :
#         self.dance = dance
#     def show(self):
#             print(f"the dance is {self.dance}")

# class danceremployee(dancer,employee):
#     def __init__(self , dance ,name) :
#         self.dance = dance 
#         self . name = name 

# o = danceremployee("break dance","srusti")
# print(o.name,o.dance)
# o.show()
# print(danceremployee.mro())

#  MULTI LEVEL INHERITANCE 

# class animal :
#     def __init__(self,  name , species) :
#         self.name = name 
#         self.species = species
#     def showDetails(self):
#         print(f"Name : {self.name} , Species : {self.species }")

# class dog(animal):
#     def __init__(self, name,breed ):
#         animal.__init__(self,name, species = "dog")
#         self.breed = breed 

#     def showDetails(self):
#         animal.showDetails(self)
#         print(f"Breed : {self.breed}")

# class goldenretriever(dog): 
#     def __init__(self, name, colour):
#         dog.__init__(self , name,  breed = "Golden retriever")
#         self.colour = colour
#     def showDetails(self):
#      dog.showDetails(self)
#      print(f"Colour : {self.colour}")

# o = goldenretriever("tony","black")
# o.showDetails()
# print(goldenretriever.mro())


# WAP to pronounce list of names using win32 API , list will be feeded manually .
# done in shoutout.py in experimentation folder 


# WALRUS OPERATOR (:)

# a = True
# print(a:= False) # first makes a false then prints it 

# num = [1,2,3,4,5]
# while(n := len(num)) > 0 :
#     print(num.pop())

# # without walrus 
# foods = list()
# while True :
#     food = input("What food do you like ? :")
#     if food == "quit":
#         break
#     foods.append(food)
# print(foods)

# with walrus 
# foods = list()
# while(food := input("what fruit do you like  ? :")) != "quit":
#     foods.append(food) 
# print(foods)


# Generators 

# def my_genrator():
#     for i in range(5):
#         yield i       #  a genrator generates values in real time and doesn't stores any value , just the method to generate it , it is acesed  by the keyword yeild
#  # for large calcuatios it saves memory and computational power beacause you don't have to generate all values at once
# gen = my_genrator()
# # print(next (gen))
# # print(next (gen))
# # print(next (gen))
# # print(next (gen))

# for j in gen :
#     print(j)   


# import re

# pattern = r"[A-Z]+yclone" # r" represents raw string  , and here [A-Z] means all letters from A to Z
# # sample text
# text = '''n meteorology, a cyclone (/sa.kloʊn/) is a large air mass that rotates around a strong center of low atmospheric pressure, 
# counterclockwise in the Northern Hemisphere and clockwise in the Southern Hemisphere as viewed from above (opposite to an anticyclone).
# [1][2] Cyclones are Dyclone characterized by inward-spiraling winds that rotate about a zone of low pressure.[3][4] The largest low-pressure systems
# are polar vortices and extratropical cyclones of the largest scale (the synoptic scale). Warm-core cyclones such as tropical cyclones 
# and subtropical cyclones Zyclone also lie within the synoptic scale.[5] Mesocyclones, tornadoes, and dust devils lie within the smaller mesoscale.
# [6] Upper level cyclones can exist without the presence of a surface low, and can pinch off from the base of the tropical upper tropospheric
# trough during the summer months in the Northern Hemisphere. Cyclones have also been seen on extraterrestrial planets, such as Mars, Jupiter,
# and Neptune.[7][8] Cyclogenesis is the process of cyclone formation and intensification.[9] Extratropical cyclones begin as waves in large 
# regions of enhanced mid-latitude temperature contrasts called baroclinic zones. These zones contract and form weather fronts as the cyclonic
# circulation closes and intensifies. Later in their life cycle, extratropical cyclones occlude as cold air masses undercut the warmer air and 
# become cold core systems.
# A cyclone's track is guided over the course of its 2 to 6 day life cycle by the steering flow of the subtropical jet stream.'''

# match = re.search(pattern,text)  # searches pattern in text and returns first occurence
# print (match)

# matches = re.finditer(pattern,text)  # searches pattern in text , and returns occurence
# # for matche in matches :
# #     print(matche)
# for matche in matches :
#     print(text[matche.span()[0]:matche.span()[1]])
#     print(matche.span())

#  to learn further about re -regular expressions visit python docs or regEx .com 

# import asyncio 
# import time 

# async def function1():
#     time.sleep(3)
#     print("fuction1 complete")
#     return"the process is on"
# async def function3():
#     time.sleep(5)
#     print("fuction2 complete")

# async def function2():
#     time.sleep(1)
#     print("fuction3 complete")

# async def main():
#     L = await asyncio.gather(
#         function1(),
#         function2(),
#         function3(),
#           )
# print(L) 
## for some reason it showed an error so see it later
# await function1()
# # await function2()
# # await function3()

#asyncio.run(main())


# import threading
# import time 

# def func(sec):
#     print(f"sleeping started for {sec} seconds")
#     time.sleep(sec)
#     print(f"slepping for {sec} seconds over")

# # tp = time.perf_counter()
# # t1 = threading.Thread(target=func , args =[5]) 
# # t2 = threading.Thread(target=func , args =[6])
# # t3 = threading.Thread(target=func , args =[3])

# # t1.start() # in threading the process has to be manually started like this 
# # t2.start()
# # t3.start()
# # tp2 = time.perf_counter() # stores run time i guess 
# # print(tp2-tp)


# from concurrent.futures import ThreadPoolExecutor
# l = [5,4,7]
# def poolingDemo():
#     with ThreadPoolExecutor(max_workers=5) as executor :
#         # future1 = executor.submit(func,4)
#         # future2 = executor.submit(func,2)
#         # future3 = executor.submit(func,3)
#         # print(future1.result())
#         # print(future2.result())
#         # print(future3.result())
#         results = executor.map(func,l)
#         for result in results:
#             print(result)
# poolingDemo()


# import multiprocessing
# import requests 

# def downloadFile(url,name):
#     print(f"started downloading file{name}")
#     response = requests.get(url)
#     open(f"files/file{name}.jpg","wb").write(response.content)
#     print(f"Finished downloading file{name}")

# if __name__== "__main__" :
#     url = "https://picsum.photos/2000/3000"
#     pros = []
#     i = 0
#     for i in range(8):
#         #downloadFile(url,i)
#         #print(f"{i} file downloaded")
#         p = multiprocessing.Process(target=downloadFile,args=[url,i])
#         p.start()
#         pros.append(p)

#     for p in pros :
#         p.join()
