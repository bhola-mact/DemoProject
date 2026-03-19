# a = 10
#
# #### modifying local variable inside function
# def something1():
#     a=15
#     print("inside function1 ", a)
#
# something1()
#
# print("outside1 ", a)
#
# #### modifying global variable inside function
# def something2():
#     global a
#     a=15
#     print("inside function2 ", a)
#
# something2()
#
# print("outside2 ", a)
#
# ##Global variables
#
# a=10
# b=20
#
# #### modifying both global and local variables  inside function
# def something3():
#
#     a=9
#     print("inside function3 local a  ", a)
#     x = globals() # list all the global variables
#     #print(x)
#     x= globals()['a'] # fetch value of global variable a
#     print("inside function3 Before change Global a", globals()['a'])
#     globals()['a']=35
#     print("inside function3 After change Global a", globals()['a'])
#
# something3()
#
# print("outside3 ", a)
#

#lamda function

# f= lambda a : a*a
# result=f(5)
# print(result)
#
# f1= lambda a,b : a+b
# result=f1(5,6)
# print(result)


#
# evens= list(filter(lambda x: x % 2 == 0, nums))
# print(evens)
# odds= list(filter(lambda x: x % 2 != 0, nums))
# print(odds)

nums=[1,2,3,4,5,6,7,8,9,10]
print(nums)
# sqrs= list(map(lambda n:n*n , nums))
# print(sqrs)

from functools import reduce

sum=reduce (lambda a,b: a+b, nums)
print(sum)

