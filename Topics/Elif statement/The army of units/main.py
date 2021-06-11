army_size = int(input())

if army_size < 1:
    answer = "no army"
elif 1 <= army_size <= 9:
    answer = "few"
elif 10 <= army_size <= 49:
    answer = "pack"
elif 50 <= army_size <= 499:
    answer = "horde"
elif 500 <= army_size <= 999:
    answer = "swarm"
else:
    answer = "legion"

print(answer)
