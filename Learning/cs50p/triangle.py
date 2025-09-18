# # def fib(n):
# #     if n < 1:
# #         return None
# #     if n < 3:
# #         return 1

# #     elem_1 = elem_2 = 1
# #     the_sum = 0
# #     for i in range(3, n + 1):
# #         the_sum = elem_1 + elem_2
# #         elem_1, elem_2 = elem_2, the_sum
# #     return the_sum


# # for n in range(1, 10):  # testing
# #     print(n, "->", fib(n))

# # Recursive implementation of the factorial function.

# def factorial(n):
#     if n == 1:    # The base case (termination condition.)
#         return 1
#     else:
#         return n * factorial(n - 1)


# print(factorial(4)) # 4 * 3 * 2 * 1 = 24

# var = 123

# t1 = (1, )
# t2 = (2, )
# t3 = (3, var)

# t1, t2, t3 = t2, t3, t1

# print(t1, t2, t3)

# duplicates = 0

# tup = 1, 2, 3, 2, 4, 5, 6, 2, 7, 2, 8, 9
# for elem in tup:
#     if elem == tup[elem]:
#         duplicates += 1
#     else:
#         continue
# print(duplicates)    # outputs: 4

# colors = (("green", "#008000"), ("blue", "#0000FF"))

# colors_dictionary = dict(colors) #we can simply use the dict function inbuilt in python 
# print(colors_dictionary)



# dictionary = {}
# my_list = ['a', 'b', 'c', 'd']

# for i in range(len(my_list) - 1):
#     dictionary[my_list[i]] = (my_list[i], )

# for i in sorted(dictionary.keys()):
#     k = dictionary[i]
#     print(k[0])

# def fun(x):
#     if x % 2 == 0:
#         return 1
#     else:
#         return


# print(fun(fun(2)) + 1)
foo = (1, 2, 3)
foo.index(0)



