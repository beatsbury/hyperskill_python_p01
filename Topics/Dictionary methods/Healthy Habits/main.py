# the list "walks" is already defined
# your code here
days_sum = 0
for day in walks:
    days_sum += day['distance']
print(days_sum // len(walks))
