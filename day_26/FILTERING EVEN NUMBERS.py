list_of_strings = input().split(',')

new_list = [int(x) for x in list_of_strings]
result = [num for num in new_list if num % 2 == 0]

print(result)