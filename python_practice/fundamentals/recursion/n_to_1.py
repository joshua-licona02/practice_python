def opposite(n):

    if n > 0:
       print(n, end=' ')
       opposite(n-1)

n=10
opposite(n)