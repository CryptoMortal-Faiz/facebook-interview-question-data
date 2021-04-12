# Given a ´dictionary, print the key for nth highest value present in the dict

new_dict ={"google":12, "amazon":9, "flipkart":4, "gfg":13}
 
# maximum value
max = max(new_dict.values())
 
# iterate through the dictionary
max2 = 0
for v in new_dict.values():
     if(v>max2 and v<max):
            max2 = v

# key_list = list(my_dict.keys())
# val_list = list(my_dict.values())
 
# # print key with val 100
# position = val_list.index(100)
# print(key_list[position])
 
# # print key with val 112
# position = val_list.index(112)
# print(key_list[position])
 
# # one-liner
# print(list(my_dict.keys())[list(my_dict.values()).index(112)]) 
# print the second largest value
print(max2)
