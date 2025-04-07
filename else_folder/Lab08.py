import time
from typing import List

def count_valid_names(names: List[str]) -> int:
    valid_name_count = 0

    for name in names:
        split_name = name.split()
        if len(split_name) == 2:
            first_name, last_name = split_name
            print(f"{first_name} {last_name}")
            valid_name_count += 1
        time.sleep(1)

    return valid_name_count

if __name__ == "__main__":
    names = ["john doe", "jane smith", "bob johnson"]
    valid_name_count = count_valid_names(names)
    print(f"Total valid names: {valid_name_count}")