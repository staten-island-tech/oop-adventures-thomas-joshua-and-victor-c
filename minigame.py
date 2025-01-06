""" import time
import random

print("Get ready...")
time.sleep(random.uniform(1, 2))

key = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
print(f"Press {key} now!")
start_time = time.time()
input_char = input(">>> ").strip().upper()
reaction_time = time.time() - start_time

if input_char == key:
    print(f"Good! Your reaction time: {reaction_time:.2f} seconds")
else:
    print("Wrong key!") """

import time
import random
import threading

#creating a timout event
def timeout():
    global timed_out
    timed_out = True
    print("You were too slow to guard!'")

#first setting it to false
timed_out = False

#1-2 second break before the game
print("Get ready...")
time.sleep(random.uniform(1, 2))

#random key to press
key = random.choice(['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
print(f"Press {key} now!")

#2 second timer
timer = threading.Timer(2.0, timeout) 
timer.start()

#starting a timer
start_time = time.time()
input_character = input(">>> ").strip().upper()
#input tells the user to input a letter
#.strip ensures the letter with still be valid even with spaces
#.upper makes sure that no matter uppercase or lowercase, the input will still be valid

timer.cancel()
#cancels time

if not timed_out:
    reaction_time = time.time() - start_time
    if input_character == key:
        print(f"Good! Your reaction time: {reaction_time:.2f} seconds")
    else:
        print("Wrong key! You lost the game.")
