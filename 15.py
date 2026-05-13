min = None
max = None

num = 75869

for i in str(num):
    parsed_num = int(i)

    if min is None:
        min = parsed_num
    elif min > parsed_num:
        min = parsed_num

    if max is None:
        max = parsed_num
    elif max < parsed_num:
        max = parsed_num


print(f"Min: {min}, Max:{max}")
