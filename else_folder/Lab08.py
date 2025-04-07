import time

names = ["john doe", "jane smith", "bob johnson"]   # List of names
totalppl = 0                                        # Initialize total people count
for name in names:                                  # Loop through each name
    split_name = name.split()                       # Split the name into first and last
    if len(split_name) == 2:                        # Check if there are two parts
        print(split_name[0] + " " + split_name[1])  # Print the name
        totalppl += 1                               # Increment the people count
    time.sleep(1)                                   # Sleep for 1 second
print("total: " + str(totalppl))                    # Print total count