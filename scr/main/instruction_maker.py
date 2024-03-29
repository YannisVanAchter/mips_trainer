# encoding UFT-8
""" 
Module to create MIPS32 instruction in binary format and tranlate: bin <-> mips
"""
__author__  = "Yannis Van Achter <yannis.van.achter@gmail.com>"
__date__    = "15 june 2022"
__version__ = "1.0"
__format__  = "Black formater <https://pypi.org/project/black/>"

# import
import random

from typing import Callable

# data ressources and basic function
def set_lenght(bin: str, lenght: int = 5) -> (str):
    """set lenght of a binary string

    apply shift left to arrive at lenght given in parameters

    Parameters:
    -----------
        bin (str): Binary string where we add 0 at begin
        lenght (int, optional): max lenght we want if the string is to large nothing to do. Defaults to 5

    Returns:
    --------
        bin (str): binary string where we add 0 at begin as requered
    """
    while len(bin) < lenght:
        bin = "0" + bin
    return bin

def from_int_to_bin(int_word: int, size: int) -> (str):
    """Translate integer to signed binary expression 

    Args:
    -----
        int_word (int): number to translate
        size (int): size of the word in binary 

    Returns:
    --------
        str: word tranlated
    """
    adress = bin(int_word)
    if adress.startswith('-'):
        adress = '1' + set_lenght(adress[3:], size) # skip -0b for negative binary number
    else:
        adress = '0' + set_lenght(adress[2:], size) # skip 0b for positive binary number
    return adress


MIPS_INSTRUCTION_DICT_BIN_FUNCT = {  # Function code at end of mips instruction
    "add": set_lenght(bin(32)[2:], 6),
    "sub": set_lenght(bin(34)[2:], 6),
    "slt": set_lenght(bin(42)[2:], 6),
    "jr": set_lenght(bin(8)[2:], 6),
}

MIPS_INSTRUCTION_DICT_BIN_OP = {  # op code at begining of mips instruction
    "lw": set_lenght(bin(35)[2:], 6),
    "sw": set_lenght(bin(43)[2:], 6),
    "add": set_lenght(bin(0)[2:], 6),
    "sub": set_lenght(bin(0)[2:], 6),
    "slt": set_lenght(bin(0)[2:], 6),
    "jr": set_lenght(bin(0)[2:], 6),
    "jal": set_lenght(bin(3)[2:], 6),
    "j": set_lenght(bin(2)[2:], 6),
    "beq": set_lenght(bin(4)[2:], 6),
    "bne": set_lenght(bin(5)[2:], 6),
}

MIPS_R_TYPE = [
    "add",
    "sub",
    "slt",
    "jr",
]

MIPS_J_TYPE = [
    "jal",
    "j",
]

MIPS_I_TYPE = [
    "lw",
    "sw",
    "beq",
    "bne",
]

MIPS_REGISTER_DICT_BIN = {
    "$zero": set_lenght(bin(0)[2:]),
    "$at": set_lenght(bin(1)[2:]),
    "$v0": set_lenght(bin(2)[2:]),
    "$v1": set_lenght(bin(3)[2:]),
    "$a0": set_lenght(bin(4)[2:]),
    "$a1": set_lenght(bin(5)[2:]),
    "$a2": set_lenght(bin(6)[2:]),
    "$a3": set_lenght(bin(7)[2:]),
    "$t0": set_lenght(bin(8)[2:]),
    "$t1": set_lenght(bin(9)[2:]),
    "$t2": set_lenght(bin(10)[2:]),
    "$t3": set_lenght(bin(11)[2:]),
    "$t4": set_lenght(bin(12)[2:]),
    "$t5": set_lenght(bin(13)[2:]),
    "$t6": set_lenght(bin(14)[2:]),
    "$t7": set_lenght(bin(15)[2:]),
    "$s0": set_lenght(bin(16)[2:]),
    "$s1": set_lenght(bin(17)[2:]),
    "$s2": set_lenght(bin(18)[2:]),
    "$s3": set_lenght(bin(19)[2:]),
    "$s4": set_lenght(bin(20)[2:]),
    "$s5": set_lenght(bin(21)[2:]),
    "$s6": set_lenght(bin(22)[2:]),
    "$s7": set_lenght(bin(23)[2:]),
    "$t8": set_lenght(bin(24)[2:]),
    "$t9": set_lenght(bin(25)[2:]),
    "$k0": set_lenght(bin(26)[2:]),
    "$k1": set_lenght(bin(27)[2:]),
    "$gp": set_lenght(bin(28)[2:]),
    "$sp": set_lenght(bin(29)[2:]),
    "$fp": set_lenght(bin(30)[2:]),
    "$ra": set_lenght(bin(31)[2:]),
}

# functions
def translate_bin_to_mips32(bin_instruction: str = "0" * 32, verbose=False) -> (str):
    """translate binary string of mips32 instruction in formated mips32

    Parameter:
    ----------
        bin_instruction (str, optional): binary instruction to translate. Defaults to '0'*32.

    Return:
    -------
        mips_code (str): formated mips code ready to use
    """

    def find_mips_from_bin(bin_word: str, dictionary: dict):
        for key, value in dictionary.items():
            if value == bin_word:
                return key
        else:
            return "Unfound"

    opcode = find_mips_from_bin(bin_instruction[:6], MIPS_INSTRUCTION_DICT_BIN_OP)
    if verbose:
        print("In function translate_bin_to_mips32")
        print(opcode)

    if opcode in MIPS_R_TYPE:
        rs = find_mips_from_bin(bin_instruction[6:11], MIPS_REGISTER_DICT_BIN)
        if verbose:
            print(rs)

        rt = find_mips_from_bin(bin_instruction[11:16], MIPS_REGISTER_DICT_BIN)
        if verbose:
            print(rt)

        rd = find_mips_from_bin(bin_instruction[16:21], MIPS_REGISTER_DICT_BIN)
        if verbose:
            print(rd)

        func = find_mips_from_bin(bin_instruction[27:], MIPS_INSTRUCTION_DICT_BIN_FUNCT)
        if verbose:
            print(func)

        mips_code = f"{func} {rd}, {rs}, {rt}"

    elif opcode in MIPS_I_TYPE:
        rs = find_mips_from_bin(bin_instruction[7:12], MIPS_REGISTER_DICT_BIN)
        if verbose:
            print(rs)

        rt = find_mips_from_bin(bin_instruction[12:17], MIPS_REGISTER_DICT_BIN)
        if verbose:
            print(rt)

        address = int(bin_instruction[17:], 2)
        if verbose:
            print(address)

        if opcode in ("lw", "sw"):
            mips_code = f"{opcode} {rt}, {address}({rs})"
        else:
            mips_code = f"{opcode} {rt}, {rs}, {address}"

    elif opcode in MIPS_J_TYPE:
        address = int(bin_instruction[7:], 2)
        if verbose:
            print(address)
        mips_code = f"{opcode} {address}"

    else:
        raise ValueError(
            f"The binary instruction did not find mips instruction wich correspond to {bin_instruction}"
        )

    return mips_code + ";"


def translate_mips32_to_bin(
    mips_instruction: str = "add $s1, $s1, $s2;", verbose=False
):
    """translate formated mips32 in binary string

    Parameter:
    ----------
        mips_instruction (str, optional): mips instruction to translate. Defaults to '0'*32.

    Return:
    -------
        bin_instruction (str): formated binary code ready to use
    """
    mips_instruction = mips_instruction.strip(";")
    mips_instruction_list = [
        a.strip(",") for a in mips_instruction.split(" ")
    ]  # list of word in mips ex: ['add', '$s1', '$t1', $t2']
    if verbose:
        print("In function translate_mips32_to_bin")
        print(mips_instruction_list)

    opcode = mips_instruction_list[0]
    op = MIPS_INSTRUCTION_DICT_BIN_OP[opcode]
    if verbose:
        print(op)

    if opcode in MIPS_R_TYPE:
        rs = MIPS_REGISTER_DICT_BIN[mips_instruction_list[2]]
        if verbose:
            print(rs)

        rt = MIPS_REGISTER_DICT_BIN[mips_instruction_list[3]]
        if verbose:
            print(rt)

        rd = MIPS_REGISTER_DICT_BIN[mips_instruction_list[1]]
        if verbose:
            print(rd)

        shamt = "0" * 5
        func = MIPS_INSTRUCTION_DICT_BIN_FUNCT[opcode]
        if verbose:
            print(func)

        bin_instruction = op + rs + rt + rd + shamt + func

    elif opcode in MIPS_I_TYPE:
        rt = MIPS_REGISTER_DICT_BIN[mips_instruction_list[1]]
        if verbose:
            print(rt)

        if opcode in ("lw", "sw"):
            offset_base = (
                mips_instruction_list[2].strip(")").split("(")
            )  # offset(base address)
            if verbose:
                print(offset_base)

            adress = from_int_to_bin(int(offset_base[0]), 15)
            if verbose:
                print(adress)

            rs = MIPS_REGISTER_DICT_BIN[offset_base[1]]
            if verbose:
                print(rs)

        else:
            rs = MIPS_REGISTER_DICT_BIN[mips_instruction_list[2]]
            if verbose:
                print(rs)

            adress = from_int_to_bin(int(mips_instruction_list[3]), 15)            
            if verbose:
                print(adress)

        bin_instruction = op + rs + rt + adress

    elif opcode in MIPS_J_TYPE:
        adress = set_lenght(bin(int(mips_instruction_list[1])), 26)
        if verbose:
            print(adress)

        bin_instruction = op + adress

    if verbose:
        print(bin_instruction)
    return bin_instruction


def create_J_type_bin(verbose=False) -> (str):
    """make random J-Type intruction in mips32 formated

    Parameter:
    ----------
        test (bool, optional): True if you want to test the function. False otherwise. Defaults to False.

    Return:
    -------
        mips_code (str): mips32 instruction for jump

    Note:
    -----
        The address in in base ten
    """
    opcode = random.choice(MIPS_J_TYPE)
    if verbose:
        print("In function create_J_type_bin")
        print(opcode)

    address = random.randint(-33554431, 33554431)
    if verbose:
        print(address)

    return f"{opcode} {address};"


def create_I_type_bin(verbose=False) -> (str):
    """make random I-Type intruction in mips32 formated

    Parameter:
    ----------
        verbose (bool, optional): True if you want to test the function. False otherwise. Defaults to False.

    Return:
    -------
        mips_code (str): mips32 instruction for branch or load/store

    Note:
    -----
        The address in in base ten
    """
    opcode = random.choice(MIPS_I_TYPE)
    if verbose:
        print("In function create_I_type_bin")
        print(opcode)

    rs = random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))
    if verbose:
        print(rs)

    rt = random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))
    if verbose:
        print(rt)

    address = random.randint(-32767, 32767)
    if verbose:
        print(address)

    if opcode in ("lw", "sw"):
        mips_code = f"{opcode} {rt}, {address}({rs});"
    else:
        mips_code = f"{opcode} {rs}, {rt}, {address};"

    return mips_code


def create_R_Type_bin(verbose=False) -> (str):
    """make random R-Type intruction in mips32 formated

    Parameter:
    ----------
        verbose (bool, optional): True if you want to test the function. False otherwise. Defaults to False.

    Return:
    -------
        mips_code (str): mips32 instruction for jump
    """
    if verbose:
        print("In function create_R_Type_bin")

    rs = random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))
    if verbose:
        print(rs)

    rt = random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))
    if verbose:
        print(rt)

    rd = random.choice(list(MIPS_REGISTER_DICT_BIN.keys()))
    if verbose:
        print(rd)

    func = random.choice(list(MIPS_INSTRUCTION_DICT_BIN_FUNCT.keys()))
    if verbose:
        print(func)

    return f"{func} {rd}, {rs}, {rt};"


def random_instruction(verbose=False) -> (tuple[str]):
    """generate one random instrcution in mips32 writen in binary

    Parameter:
    ----------
        verbose (bool, optional): True if you want to test the function. False otherwise. Defaults to False.

    Return Tuple:
    -------------
        bin_instruction : instruction in binary (str)
        default_instruction : instruction in mips 32 for correction (str)

    Note:
    -----
        In default_instruction if there is an addres this is in base 10
    """

    mips_instruction = None
    instruction_type: Callable = random.choice(
        (create_R_Type_bin, create_I_type_bin, create_J_type_bin)
    )

    if verbose:
        print("In function random_instruction")
        print("bin_instruction : ", mips_instruction)
        print("instruction_type : ", instruction_type)

    mips_instruction = instruction_type(verbose)

    if verbose:
        print("bin_instruction after call of function : ", mips_instruction)

    bin_instruction = translate_mips32_to_bin(mips_instruction, verbose=verbose)

    if verbose:
        print("default_instrcution : ", mips_instruction)

    return bin_instruction, mips_instruction


def main():
    import os
    import time

    def clear():
        command = "clear"
        if os.name in ["nt", "dos"]:
            command = "cls"
        os.system(command)

    while True:
        try:
            clear()
            bin_instruction, mips_instruction = random_instruction()
            print(f"tranlate the following binary instruction: \n{bin_instruction}")

            user_answer = input(f"\nEnter your answer in mips32 : ").strip()

            if user_answer == mips_instruction:
                print("\nYou have performed admirably")
                time.sleep(3)
            else:
                print(
                    f"\nYou will be more lucky next time, but you are on the right way\nThe answer was : {mips_instruction}"
                )
                time.sleep(10)
        except KeyboardInterrupt:
            exit("Hope to see you soon 😎😉")


if __name__ == "__main__":
    main()
