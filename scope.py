def count():
    even=0
    odd=0

    for i in a:
        if i %2==0:
            even+=1
        else:
            odd+=1
    return even, odd

a = [1,2,3,5,6,7,8,9]
even,odd = count()
print(even)
print(odd)