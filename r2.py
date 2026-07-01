def royxat_max(royxat):
    if len(royxat) == 1:
        return royxat[0]
    
    qolgan_max = royxat_max(royxat[1:])
    
    if royxat[0] > qolgan_max:
        return royxat[0]
    else:
        return qolgan_max

print(royxat_max([12, 45, 2, 78, 34]))

