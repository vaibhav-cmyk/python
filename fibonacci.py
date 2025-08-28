def feb(n):
    a=0
    b=1

    if n<0:
        print('enter accurate value')
    elif n ==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(2,n):
            c=a+b
            a=b
            b=c
            if c < 100:
                print(c)
            else:
              return

feb(200)