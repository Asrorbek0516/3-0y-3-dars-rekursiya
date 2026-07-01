def ikkilik_son(n):
    if n==0:
        return "0"
    if n==1:
        return "1"
    return ikkilik_son(n//2) + str(n%2)

print(ikkilik_son(25))