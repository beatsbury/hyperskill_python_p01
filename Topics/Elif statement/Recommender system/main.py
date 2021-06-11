user_age = int(input())

if user_age <= 16:
    answer = "Lion King"
elif 17 <= user_age <= 25:
    answer = "Trainspotting"
elif 26 <= user_age <= 40:
    answer = "Matrix"
elif 41 <= user_age <= 60:
    answer = "Pulp Fiction"
else:
    answer = "Breakfast at Tiffany's"

print(answer)
