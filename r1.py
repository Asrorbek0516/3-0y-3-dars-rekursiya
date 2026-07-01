def  juft_sonlar_yigindisi(n):
    if n<=0:
        return 0
    if n%2==0:
        return n+juft_sonlar_yigindisi(n-1)
    else:
        return juft_sonlar_yigindisi(n-1)
    
print(juft_sonlar_yigindisi(10))
