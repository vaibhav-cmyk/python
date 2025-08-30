num =4421
digits=[]
temp=num
while temp>0:
    digit=temp%10
    digits.append(digit)
    temp=temp//10
product=1
sum=0
for i in range(len(digits)):
    product=product*digits[i]
    sum=sum+digits[i]

print(product)
print(sum)
result=product-sum
print(product,'-',sum,'=',result)