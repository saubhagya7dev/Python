# def makepair(list1, list2):
#     if len(list1) != len(list2):
#         return "Error: Lists must have equal length"
    
#     # Create list of pairs using zip and list comprehension
#     return [(list1[i], list2[i]) for i in range(len(list1))]

# # Alternative solution using zip
# def makepair_alt(list1, list2):
#     return list(zip(list1, list2))


# Write a python function contsqr(n), that returns the count of perfect 
# squares less than equal to n . (n>1)

# import math
# def contsqr(n):
#     if n < 1:
#         return "Error: n must be greater than 1"
#     return math.floor(math.sqrt(n))

# def printsqr_alt(n):
#     return [i * i for i in range(1, int(n ** 0.5) + 1)]

# n=50
# result=contsqr(n)
# sqrno=printsqr_alt(n)
# print(result)
# print(sqrno)




#write a python function alternating that takes as argument a sequence lst. The function returns true 
#if the elements in lst are alternately odd and even starting with an even no. otherwise it returns false 

# def alternating(lst):
    
#     if not lst:
#         return False
    
#     for i in range(len(lst)):
#         if lst[i] % 2 == 0:
#             if lst[i+1] % 2 != 0:
#                 return True
#             else:
#                 if lst[i+1] % 2 == 0:
#                     return False

# print(alternating([2,7,3,4,5]))



# def sum(n1,n2):
#     return n1+n2
# n1=int(input("enter the no 1."))
# n2=int(input("enter the no 2."))
# print(sum(n1,n2))


# import math

# def circle_stats(radius):
#     area=math.pi*radius**2
#     circumference=2*math .pi*radius
#     return area,circumference

# radius=int(input("enter the radius of the circle."))
# area,circumference=circle_stats(radius)
# rounded_area=round(area,2)
# rounded_circumference=round(circumference,2)
# print("area of the circle is",rounded_area,"and circumference is",rounded_circumference)



# def even_generator(limit):
#     for i in range(2,limit+1,2):
#         yield i

# even = even_generator(100)
# print(list(even), end=" ")

# def factorial(n):
#     if n == 0 or n == 1:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(5))

def decorator(func):
    def wrapper():
        print("Before the function call")
        func()
        print("After the function call")
    return wrapper

@decorator
def say_hello():
    print("Hello!")

say_hello()
