my_list = [55, 41, 52, 68, 45, 27, 40, 25, 37, 26]

temp = my_list[6]
my_list[6] = my_list[7]
my_list[7] = temp

print(my_list)

my_list = [27, 32, 18,  2, 11, 57, 14, 38, 19, 91]

temp = my_list[3]
my_list[3] = my_list[0]
my_list[0] = temp

print(my_list)
