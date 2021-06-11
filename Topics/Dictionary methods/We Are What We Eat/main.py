# the list "meals" is already defined
# your code here
cal_list = []

for item in meals:
    cal_list.append(item['kcal'])

print(sum(cal_list))
