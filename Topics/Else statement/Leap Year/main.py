# put your python code here

user_input = int(input())

print("Leap" if (user_input % 4 == 0) & (user_input % 100 != 0) or (user_input % 400 == 0) else "Ordinary")
