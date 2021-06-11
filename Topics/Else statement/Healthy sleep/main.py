A = int(input())
B = int(input())
H = int(input())

answer = "Normal"

if H < A:
    answer = "Deficiency"
elif H > B:
    answer = "Excess"

print(answer)
