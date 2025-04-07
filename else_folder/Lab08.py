import time

names = ["john doe", "jane smith", "bob johnson"]
valid_name_count = 0
for name in names:
    split_name = name.split()
    if len(split_name) == 2:
        forward_name, last_name = split_name[0], split_name[1]
        print(f"{forward_name} {last_name}")
        valid_name_count += 1
    time.sleep(1)
print("total: " + str(valid_name_count))