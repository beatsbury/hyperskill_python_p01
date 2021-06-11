coord1 = float(input())
coord2 = float(input())

if (coord1 == 0) & (coord2 == 0):
    answer = "It's the origin!"
elif (coord1 == 0) or (coord2 == 0):
    answer = "One of the coordinates is equal to zero!"
elif coord1 > 0:
    if coord2 < 0:
        answer = "IV"
    else:
        answer = "I"
else:
    if coord2 < 0:
        answer = "III"
    else:
        answer = "II"

print(answer)
