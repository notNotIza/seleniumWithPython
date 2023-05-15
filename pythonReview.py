# Review of python foundations

# print("This is a review")

# # variables and data type review
# a = 3
# print(type(a))
# print(type(int(a)))

# someWord = "haha"
# print(someWord + " is of data type: " + str(type(someWord)))
# print("{0} is of data type: {1}".format(someWord,type(someWord)))

# b,c,d,e,f, g= 3.1, 'a', 300, "a", 300000000000000000000000, True
# h = 1j
# i = ["x","y","z"]
# j = (1,2,3)
# k = range(5)
# l = {"firstname":"Jane", "lastname":"Doe", "age": 20}
# m = {"apple","orange","cherry"}
# n = None
# print(type(b)) #float
# print(type(c)) #str
# print(type(d)) #int
# print(type(e)) #str
# print(type(f)) #int
# print(type(g)) #bool
# print(type(h)) #complex
# print(type(i)) #list
# print(type(j)) #tuple - an immutable list
# print(type(k)) #range
# print(type(l)) #dict
# print(type(m)) #set
# print(type(n)) #NoneType

# # challenge (from project euler): Find all the multiples of 3 or 5 below the provided parameter value number
# def multiplesOf3Or5(number):
#     found = []
#     sum = 0
#     currentNum = number
#     while(currentNum > 0):
#         currentNum =currentNum - 1
#         if(currentNum%3==0 or currentNum%5==0):
#             found.append(currentNum)
#             sum += currentNum
#     #print(found)

#     return sum


# print(multiplesOf3Or5(10))
# print(multiplesOf3Or5(49))
# print(multiplesOf3Or5(1000))
# print(multiplesOf3Or5(8456))
# print(multiplesOf3Or5(19564))

# challenge (from project euler): There exists exactly one pythagorean triplet for which a + b + c = 1000. Find the product abc s.t. a + b + c = number.
# Note: a pythagorean triplet is a set of 3 natural numbers, a<b<c for which, aSquared + bSquared = cSquared
# def specialPythagoreanTriplet(number):
#     a = 1
#     while(a<number):
#         a += 1
#         b = a
#         while(b<number):
#             b += 1
#             c = number - a - b
#             if(c > 0):
#                 if(c**2 == (a**2 + b**2)):
#                     print("a: {}, b: {}, c: {}".format(a,b,c))
#                     return a*b*c
    
# print(specialPythagoreanTriplet(24))
# print(specialPythagoreanTriplet(120))
# print(specialPythagoreanTriplet(1000))


# how to create a dictionary at run time and add data into it
# dic = {"name":"Georgia", "age":30, "role":"main character"}

# print(dic)
# print(dic["name"])

# mainCharacter = {}
# mainCharacter["name"] = "Georgia"
# mainCharacter["age"] = 30
# mainCharacter["favColor"] = "blue"
# mainCharacter["favFood"] = "pizza"
# print(mainCharacter)
