candies=[10,5,2,18]
extra_candies=100
total=[]
greatest_no=max(candies)
print("Highest candy is:",greatest_no)
for i in range(len(candies)):
    new_total=candies[i]+extra_candies
    total.append(new_total)

print("total candies with extracandies:",total)
result=[]
for i in range(0,len(total)):
    if total[i] >= greatest_no:
        result.append(True)
    else:
        result.append(False)

print("total candies:",result)
