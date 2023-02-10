# Day 12
# Shuffle list

import random

list = [1,2,3,4,5]
def shuffle_list(l):
    random.shuffle(l)
    return list

print(shuffle_list(list))

# Array of 7 unique randomly generated numbers

def rand_num():
    randomlist = random.sample(range(0, 9), 7)
    print(randomlist)
            
rand_num()
