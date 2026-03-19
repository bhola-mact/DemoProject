

nums=[1,2,3,4,5,6,7,8,9,10]
print("nums",nums)

#lamda function

# f= lambda a : a*a
# result=f(5)
# print(result)
#
# f1= lambda a,b : a+b
# result=f1(5,6)
# print(result)



evens= list(filter(lambda x: x % 2 == 0, nums))
print("evens",evens)
odds= list(filter(lambda x: x % 2 != 0, nums))
print("odds",odds)


sqrs= list(map(lambda n:n*n , nums))
print("sqrs", sqrs)




from functools import reduce

sum=reduce (lambda a,b: a+b, nums)
print("sum", sum)

