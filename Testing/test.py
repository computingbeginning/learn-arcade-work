my_list = [-4, -2, -56, -2, -30]
positive_outlook_list = []
biggest_number = my_list[0]
for item in my_list:
    if item >= 0:
        positive_outlook_list.append(item)

print(positive_outlook_list)
