import  time
from itertools import count

total = 100
count = 0
while count < total:
    count += 1
    print(f"count: {count}")
    time.sleep(1)
