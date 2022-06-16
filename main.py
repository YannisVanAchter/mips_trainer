
from random import choice
import os
import time

# import pyttsx3

from scr.main import random_instruction, translate_mips32_to_bin, translate_bin_to_mips32

def clear():
    command = 'clear'
    if os.name == 'nt': command = 'cls'
    os.system(command)
    
while True:
    clear()
    process = choice(("pipeline", "multi-cycle", "monocycle"))
    print(f"On the {process} apply the following binary command")
    
    bin_instruction, mips_instruction = random_instruction()
    print(f"tranlate the following binary instruction: \n{bin_instruction}")
    
    user_anwer = input(f"\nEnter your answer in mips32 : ")
    
    if user_anwer == mips_instruction: print ("\nYou have performed admirably")
    else: print(f"\nYou will be more lucki next time, but you are on the right way\nAnswer : {mips_instruction}")
    
    time.sleep(3)