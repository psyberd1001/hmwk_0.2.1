my_list = [42, 0, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
i = 0
while i < len(my_list):
    if my_list[i] < 0 or i > len(my_list):
        break
    else:
        if my_list[i] == 0:
            del my_list[i]
        else:
            print(my_list[i])
            i += 1
