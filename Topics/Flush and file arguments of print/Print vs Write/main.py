numbers = [1234, 5678, 90]
with open('file_with_list.txt', 'w') as f:
    f.writelines(str(numbers))
