# encoding UFT-8
""" 
Module to create MIPS32 instruction in binary format and tranlate: bin <-> mips
"""
__author__  = "Yannis Van Achter <yannis.van.achter@gmail.com>"
__date__    = "15 june 2022"

# import
import random

from typing import Callable

# data ressources and basic function 
def set_lenght(bin: str, lenght=5) -> (str):
    while len(bin) < lenght:
        bin = '0' + bin
    return bin

MIPS_INSTRUCTION_DICT_BIN_FUNCT = {
    'add' : set_lenght(bin(32)[2:],6),
    'sub' : set_lenght(bin(34)[2:],6),
    'slt' : set_lenght(bin(42)[2:],6),
    'jr' : set_lenght(bin(8)[2:],6),
}

MIPS_INSTRUCTION_DICT_BIN_OP = {
    'lw' : set_lenght(bin(35)[2:],6),
    'sw' : set_lenght(bin(43)[2:],6),
    'add' : set_lenght(bin(0)[2:],6),
    'sub' : set_lenght(bin(0)[2:],6),
    'slt' : set_lenght(bin(0)[2:],6),
    'jr' : set_lenght(bin(0)[2:],6),
    'jal' : set_lenght(bin(3)[2:],6),
    'j' : set_lenght(bin(2)[2:],6),
    'beq' : set_lenght(bin(4)[2:],6),
    'bne' : set_lenght(bin(5)[2:],6),
}

MIPS_R_TYPE = [
    'add',
    'sub',
    'slt',
    'jr',
]

MIPS_J_TYPE = [
    'jal',
    'j',
]

MIPS_I_TYPE = [
    'lw',
    'sw',
    'beq',
    'bne',
]

MIPS_REGISTER_DICT_BIN = {
    '$zero' : set_lenght(bin(0)[2:]),
    '$at' : set_lenght(bin(1)[2:]),
    '$v0' : set_lenght(bin(2)[2:]),
    '$v1' : set_lenght(bin(3)[2:]),
    '$a0' : set_lenght(bin(4)[2:]),
    '$a1' : set_lenght(bin(5)[2:]),
    '$a2' : set_lenght(bin(6)[2:]),
    '$a3' : set_lenght(bin(7)[2:]),
    '$t0' : set_lenght(bin(8)[2:]),
    '$t1' : set_lenght(bin(9)[2:]),
    '$t2' : set_lenght(bin(10)[2:]),
    '$t3' : set_lenght(bin(11)[2:]),
    '$t4' : set_lenght(bin(12)[2:]),
    '$t5' : set_lenght(bin(13)[2:]),
    '$t6' : set_lenght(bin(14)[2:]),
    '$t7' : set_lenght(bin(15)[2:]),
    '$s0' : set_lenght(bin(16)[2:]),
    '$s1' : set_lenght(bin(17)[2:]),
    '$s2' : set_lenght(bin(18)[2:]),
    '$s3' : set_lenght(bin(19)[2:]),
    '$s4' : set_lenght(bin(20)[2:]),
    '$s5' : set_lenght(bin(21)[2:]),
    '$s6' : set_lenght(bin(22)[2:]),
    '$s7' : set_lenght(bin(23)[2:]),
    '$t8' : set_lenght(bin(24)[2:]),
    '$t9' : set_lenght(bin(25)[2:]),
    '$k0' : set_lenght(bin(26)[2:]),
    '$k1' : set_lenght(bin(27)[2:]),
    '$gp' : set_lenght(bin(28)[2:]),
    '$sp' : set_lenght(bin(29)[2:]),
    '$fp' : set_lenght(bin(30)[2:]),
    '$ra' : set_lenght(bin(31)[2:]),
}

# functions 
def translate_bin_to_mips32(bin_instruction: str = '0'*32, test=False) -> (str):
    def find_mips_from_bin(bin_word, dictionary: dict):
        for key, value in dictionary.items():
            if value == bin_word: return key
    
    opcode = find_mips_from_bin(bin_instruction[:7], MIPS_INSTRUCTION_DICT_BIN_OP)
    if test: 
        print('In function translate_bin_to_mips32')
        print(opcode)
    
    if opcode in MIPS_R_TYPE:
        rs = find_mips_from_bin(bin_instruction[7:12], MIPS_REGISTER_DICT_BIN)
        if test: print(rs)
        
        rt = find_mips_from_bin(bin_instruction[12:17], MIPS_REGISTER_DICT_BIN)
        if test: print(rt)
        
        rd = find_mips_from_bin(bin_instruction[17:22], MIPS_REGISTER_DICT_BIN)
        if test: print(rd)
        
        shamt = '0'*5
        func = find_mips_from_bin(bin_instruction[25:], MIPS_INSTRUCTION_DICT_BIN_FUNCT)
        if test: print(func)
        
        mips_code = func + rd + rs + rt
    
    elif opcode in MIPS_I_TYPE:
        rs = find_mips_from_bin(bin_instruction[7:12], MIPS_REGISTER_DICT_BIN)
        if test: print(rs)
        
        rt = find_mips_from_bin(bin_instruction[12:17], MIPS_REGISTER_DICT_BIN)
        if test: print(rt)
        
        address = int(bin_instruction[17:], 2)
        if test: print(address)
        
        if opcode in ('lw', 'sw'): mips_code = f"{opcode} {rt}, {address}({rs})"
        else: mips_code = f"{opcode} {rs}, {rt}, {address}"

        
    elif opcode in MIPS_J_TYPE:        
        address = int(bin_instruction[7:], 2)
        if test: print(address)
        mips_code = opcode + address
    
    else: 
        mips_code = ValueError(f"The binary instruction did not find mips instruction wich correspond to {bin_instruction}")

    return mips_code
        

def translate_mips32_to_bin(mips_instruction : str = 'add $s1, $s1, $s2', test=False):
    mips_instruction_list = [a.strip(',') for a in mips_instruction.split(' ' )]
    if test:
        print('In function translate_mips32_to_bin')
        print(mips_instruction_list)
    
    opcode = mips_instruction_list[0]
    op = MIPS_INSTRUCTION_DICT_BIN_OP[opcode]
    if test: print(op)

    if opcode in MIPS_R_TYPE:
        rs = MIPS_REGISTER_DICT_BIN[mips_instruction_list[2]]
        if test: print(rs)
        
        rt = MIPS_REGISTER_DICT_BIN[mips_instruction_list[3]]
        if test: print(rt)
        
        rd = MIPS_REGISTER_DICT_BIN[mips_instruction_list[1]]
        if test: print(rd)
        
        shamt = '0'*5
        func = MIPS_INSTRUCTION_DICT_BIN_FUNCT[opcode]
        if test: print(func)
        
        bin_instruction = op + rs + rt + rd + shamt + func
        
    elif opcode in MIPS_I_TYPE:
        rt = MIPS_REGISTER_DICT_BIN[mips_instruction_list[1]]
        if test: print(rt)
        
        if opcode in ('lw', 'sw'):
            offset_base = mips_instruction_list[2].strip(')').split('(')# offset(base address)
            if test: print(offset_base)
            
            address = set_lenght(bin(int(offset_base[0]))[2:], 16)
            if test: print(address)
            
            rs = MIPS_REGISTER_DICT_BIN[offset_base[1]]
            if test: print(rs)
            
        else:
            rs = MIPS_REGISTER_DICT_BIN[mips_instruction_list[2]]
            if test: print(rs)
            
            address = set_lenght(bin(int(mips_instruction_list[3]))[2:], 16) 
            if test: print(address)
        
        bin_instruction = op + rs + rt + address
            
    elif opcode in MIPS_J_TYPE:
        address = set_lenght(bin(int(mips_instruction_list[1]))[2:], 26)
        if test: print(address)
        
        bin_instruction = op + address
        
    if test: print(bin_instruction)
    return bin_instruction

def create_J_type_bin(test=False) -> (str):
    instruction = random.choice(MIPS_J_TYPE)
    opcode = MIPS_INSTRUCTION_DICT_BIN_OP[instruction]
    if test:
        print("In function create_J_type_bin")
        print(opcode)
        
    address = set_lenght(bin(random.randint(0,67108863))[2:], 26)
    if test: print(address)
    
    return opcode + address

def create_I_type_bin(test=False) -> (str):
    instruction = random.choice(MIPS_I_TYPE)
    opcode = MIPS_INSTRUCTION_DICT_BIN_OP[instruction]
    if test:
        print("In function create_I_type_bin")
        print(opcode)
    
    rs = MIPS_REGISTER_DICT_BIN[random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))]
    if test: print(rs)
    
    rt = MIPS_REGISTER_DICT_BIN[random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))]
    if test: print(rt)
    
    address = set_lenght( bin(random.randint(0, 65535))[2:], 16)
    if test: print(address)
    
    return opcode + rs + rt + address

def create_R_Type_bin(test=False) -> (str):
    opcode = '0' * 6
    if test:
        print("In function create_R_Type_bin")
        print(opcode)
        
    rs = MIPS_REGISTER_DICT_BIN[random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))]
    if test: print(rs)
        
    rt = MIPS_REGISTER_DICT_BIN[random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))]
    if test: print(rt)
        
    rd = MIPS_REGISTER_DICT_BIN[random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))]
    if test: print(rd)
        
    shamt = '0'*5
    
    funct = MIPS_INSTRUCTION_DICT_BIN_FUNCT[random.choice(list(MIPS_INSTRUCTION_DICT_BIN_FUNCT.keys()))]
    if test: print(funct)
        
    return opcode + rs + rt + rd + shamt + funct

def random_instruction(test=False) -> (str):
    """generate one random instrcution in mips32 writen in binary

    Return:
        bin_instruction : instruction in binary (str)
        default_instruction : instruction in mips 32 for correction (str)
    """
    
    bin_instruction = None
    instruction_type: Callable = random.choice((create_R_Type_bin, create_I_type_bin, create_J_type_bin))
    
    if test:
        print("In function random_instruction")
        print('bin_instruction : ', bin_instruction)
        print('instruction_type : ', instruction_type)
    
    bin_instruction = instruction_type(test=test)
    
    if test: print('bin_instruction after call of function : ', bin_instruction)
    
    mips_instruction = translate_bin_to_mips32(bin_instruction, test=test)
    
    if test: print('default_instrcution : ', mips_instruction)
        
    return bin_instruction , mips_instruction

def test():
    def test_function(func: Callable = random_instruction, arg=[], test=True):
        print("In function : ", func)
        try:
            p =  func(test=test)
            print(p)
        except Exception as e:
            print("Error : ", e)
        
    test_function(random_instruction)
    print()
    
    test_function(create_R_Type_bin)
    print()
    
    test_function(create_J_type_bin)
    print()
    
    test_function(create_I_type_bin)
    print()
    
    translate_mips32_to_bin_return = translate_mips32_to_bin(test=True) 
    translate_default = '0'*6+set_lenght(bin(17)[2:])+set_lenght(bin(18)[2:])+set_lenght(bin(17)[2:])+'0'*5 + MIPS_INSTRUCTION_DICT_BIN_FUNCT['add']
    print("Default : ",translate_default)
    print(translate_mips32_to_bin_return, translate_mips32_to_bin_return==translate_default)
    print()
    
    translate_mips32_to_bin_return = translate_mips32_to_bin('beq $s1, $s2, 2094',test=True) 
    translate_default = set_lenght(bin(4)[2:], 6)+set_lenght(bin(17)[2:])+set_lenght(bin(18)[2:])+set_lenght(bin(2094)[2:], 16)
    print("Default : ",translate_default)
    print(translate_mips32_to_bin_return,  translate_mips32_to_bin_return==translate_default)
    print()
    
    translate_mips32_to_bin_return = translate_mips32_to_bin('lw $s1, 44($sp)',test=True) 
    translate_default = set_lenght(bin(35)[2:], 6)+set_lenght(bin(17)[2:])+set_lenght(bin(29)[2:])+set_lenght(bin(44)[2:], 16)
    print("Default : ",translate_default)
    print(translate_mips32_to_bin_return,  translate_mips32_to_bin_return==translate_default)
    print()
    
    translate_mips32_to_bin_return = translate_mips32_to_bin("jal 2094",test=True) 
    translate_default = set_lenght(bin(3)[2:], 6)+set_lenght(bin(2094)[2:], 26)
    print("Default : ",translate_default)
    print(translate_mips32_to_bin_return,  translate_mips32_to_bin_return==translate_default)
    print()
    
    translate_bin_to_mips32_return = translate_bin_to_mips32('000000011010111000111000000101010', True)
    translate_default = "slt $t5, $t6, $a8"
    print("Default : ",translate_default)
    print(translate_bin_to_mips32_return, translate_bin_to_mips32_return==translate_default)
    
    # TODO: write test case
    # translate_bin_to_mips32_return = translate_bin_to_mips32('000000011010111000111000000101010', True)
    # translate_default = "slt $t5, $t6, $a8"
    # print("Default : ",translate_default)
    # print(translate_bin_to_mips32_return, translate_bin_to_mips32_return==translate_default)

    # translate_bin_to_mips32_return = translate_bin_to_mips32('000000011010111000111000000101010', True)
    # translate_default = "slt $t5, $t6, $a8"
    # print("Default : ",translate_default)
    # print(translate_bin_to_mips32_return, translate_bin_to_mips32_return==translate_default)

    # translate_bin_to_mips32_return = translate_bin_to_mips32('000000011010111000111000000101010', True)
    # translate_default = "slt $t5, $t6, $a8"
    # print("Default : ",translate_default)
    # print(translate_bin_to_mips32_return, translate_bin_to_mips32_return==translate_default)

def __main__(test=False):
    import os
    import time
    def clear():
        command = 'clear'
        if os.name == 'nt': command = 'cls'
        os.system(command)
        
    while True:
        clear()
        bin_instruction, mips_instruction = random_instruction()
        print(f"tranlate the following binary instruction: \n{bin_instruction}")
        
        user_anwer = input(f"\nEnter your answer in mips32 : ")
        
        if test: print(bin_instruction, mips_instruction)
        
        if user_anwer == mips_instruction: print ("\nYou have performed admirably")
        else: print("\nYou will be more lucki next time, but you are on the right way")
        
        time.sleep(30)
        

if __name__ == '__main__':
    test()
    # __main__(True)