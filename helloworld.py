# Contents
# 1. Print+Input : Programming with effect
# 2. Math
# 3. Conditionals
# 4. Iterators
# 5. Modularity - Functions
# 6. Objects



# We start
# print("Welcome to Session 1")

# Variables and Math
# a = 5
# b = 10
# print("a+b:", a+b)
# print("a-b:",a-b)
# print("a*b:",a*b)
# print("a/b:",a/b)

# # This is a comment. Comments are meant to make your code easy to understand
# # Guess the following
# print("?",a ** 2) # This prints exponent

# Hello There. This is ignored by your computer!


# # Conditionals
# a = 90
# if a > 18:
#     print("You can vote")
# else:
#     print("Nope")

# a = input("Enter your number")

# print(a)

# # Loops
# some_number = 0

# while some_number < 5:
#     some_number += 1
#     print(some_number)

# a = 0
# print(a)
# a = a + 1
# print(a)
# a = a + 1
# print(a)
# a = a + 1
# print(a)
# a = a + 1
# print(a)

# user_number = int(input("enter number"))
# some_number = 0

# while some_number < user_number:
#     some_number += 1
#     print(some_number)

# lists
# lst = [1,2,3,4,5]
# sum = 0
# for i in lst: # For each number i in the list lst, do the following
#     sum += i

# # Syntactic Sugar
# print(sum)

# some_number = 0

# while some_number < len(lst):
#     sum += lst[some_number]
#     some_number += 1

# print(sum)


# # Function

# f(x) = x^2, f(3)=9, f(4) = 16
# g(x) = 3*x, g(10) = 30

# import math

# def squared_difference(x,y):
#     return (x-y)*(x-y)

# def distance(x1,x2,y1,y2):
#     term1 = squared_difference(x1,x2)
#     term2 = squared_difference(y1,y2)
#     return math.sqrt(term1 + term2)


# print(math)

# Given a list of points (X,Y)
# Find the perimeter of the polygon formed

# Can you write a code to calculate the n-th Fibonacci number.
# F(n) = F(n-1) + F(n-2), F(0) = 0, F(1) = 1, n >= 0

# Recursion

# def recursive(a):
#     if a == 1:
#         return a
#     else:
#         return recursive(a-1) + 5 # 1 + 5 + 5 = 11
    
# print(recursive(3))

# # Lambda
# x = lambda a : a + 10
# print(x(5))
