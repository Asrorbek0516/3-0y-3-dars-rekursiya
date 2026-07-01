def royxatda_bormi(royxat, element):
    if len(royxat)==0:
        return False
    if royxat[0]==element:
        return True
    
    return royxatda_bormi(royxat[1:],element)

print(royxatda_bormi([3, 7, 1, 9], 7))