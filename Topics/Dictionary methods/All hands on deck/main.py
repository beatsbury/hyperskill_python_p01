card_dict = {"2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7,
             "8": 8, "9": 9, "10": 10, "Jack": 11, "Queen": 12, "King": 13, "Ace": 14}
input_list = []
num_list = []
index = 0

while index < 6:
    input_value = input()
    input_list.append(input_value)
    index += 1

for in_value in input_list:
    num_list.append(card_dict.get(in_value))

print(sum(num_list) / len(num_list))
