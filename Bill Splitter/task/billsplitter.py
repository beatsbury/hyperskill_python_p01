# write your code here
import random

number_of_friends = int(input("Enter the number of friends joining (including you)"))
print()

if number_of_friends < 1:
    print("No one is joining for the party")
else:
    friends = []
    
    print("Enter the name of every friend (including you), each on a new line")
    for n in range(number_of_friends):
        friends.append(input())
    
    friends_dict = dict.fromkeys(friends, 0.0)
    print()
    sum_total = int(input("Enter the total bill value"))
    split_value = round(sum_total / number_of_friends, 2)
    for record in friends_dict:
        friends_dict[record] = split_value

    print()

    lucky_choice = input("Do you want to use the \"Who is lucky?\" feature? Write Yes/No")

    print()

    if lucky_choice != "Yes":

        print("No one is going to be lucky")
        print()
        print(friends_dict)

    else:

        the_lucky = random.choice(friends)
        print("{} is the lucky one".format(the_lucky))
        new_split_value = round(sum_total / (number_of_friends - 1), 2)

        for record in friends_dict:
            if record != the_lucky:
                friends_dict[record] = new_split_value
            else:
                friends_dict[record] = 0
        print(friends_dict)
