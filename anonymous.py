# f=lambda a:a*a
# result= f(5)
# print(result)

# sum=lambda a,b : a+b

# result=sum(10,10)
# print('sum is',result)


from functools import reduce

n=[1,2,3,4,5,6,7,8,9]
even=list(filter(lambda n:n%2==0,n))
double = list(map(lambda n:n+2,even))
sum=reduce(lambda a,b:a+b,double)
print(double)
print(even)
print(sum)