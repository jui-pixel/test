import time

names = ["john doe", "jane smith", "bob johnson"]
totalppl = 0
for name in names:
    split_name = name.split()
    if len(split_name) == 2:
        print(split_name[0] + " " + split_name[1])
        totalppl += 1
    time.sleep(1)
print("total: " + str(totalppl))