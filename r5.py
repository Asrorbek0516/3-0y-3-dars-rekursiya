def sonlar_kopaytmasi(royxat):
    if len(royxat)==1:
        return royxat[0]
    return royxat[0] * sonlar_kopaytmasi(royxat[1:])

print(sonlar_kopaytmasi([2,3,4]))