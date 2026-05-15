data = [10, 21, 4, 45, 66, 93, 11]


odd_count = len(list(filter(lambda x: x % 2 == 1, data)))
event_count = len(list(filter(lambda x: x % 2 == 0, data)))

print(f"ODD: {odd_count}, EVENT: {event_count}")
