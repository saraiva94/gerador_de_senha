from time import sleep
import random

lower = 'abcdefghijklmnopqrstuvwxyz'
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
number = '0123456789'
symbols = '!@#$%&*(_)/'

use_for = lower + upper + number + symbols
length_for_pass = 8
password = ''.join(random.sample(use_for, length_for_pass))

print('generating password')

sleep(0.3)
print('.')
sleep(0.3)
print('.')
sleep(0.3)
print('.')

print('')

print(f'You key is: {password}')