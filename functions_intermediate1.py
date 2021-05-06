import random
def randInt(min=0, max=100):
    num = random.random() * max + min
    return round(num)
print('integer between 0 to 100: ', randInt(), '\n')

import random
def randInt(min=0, max=100):
    num = random.random() * max + min
    return round(num)
print('integer between 0 to 50: ', randInt(max=50), '\n')

import random
def randInt(min=0, max=100):
    num = random.random() * (max-min) + min             # (max-min) this is the trick! 
    return round(num)
print('integer between 50 to 100: ', randInt(min=50), '\n')

import random
def randInt(min=0, max=100):
    num = random.random() * (max-min) + min             # again!
    return round(num)
print('integer between 50 and 500: ', randInt(min=50, max=500), '\n')

# Edge Cases! 
import random
def randInt(min=0, max=100):
    if min > max:
        print('you are not very good at this')
        return
    num = random.random() * (max-min) + min
    return round(num)
print('edge case min>max: ', randInt(min=10, max=5), '\n')

# Edge Cases! 
import random
def randInt(min=0, max=100):
    if max < 0:
        print('you are not very good at this')
        return
    num = random.random() * (max-min) + min
    return round(num)
print('edge case max<0: ', randInt(min=10, max=-5), '\n')