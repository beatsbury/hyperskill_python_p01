# put your python code here
alpha_dict = dict.fromkeys(list('abcdefghijklmnopqrstuvwxyz'))

for item in alpha_dict:
    alpha_dict.update({item: item + item})

double_alphabet = alpha_dict
