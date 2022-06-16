import unittest

from typing import Callable

# module to test
import instruction_maker as im

class TestInstructionMaker(unittest.TestCase):
    
    def test_function(self, func: Callable = im.random_instruction, arg: str = None, expected: str = None, test=True):

        returned = func(test) if arg != None else func(arg, test=test)
        
        self.assertEqual(returned, expected)
    
    def setUp(self):
        data_to_test = [
            {
                'mips' : "slt $t5, $t6, $a8",
                'bin' : '000000011010111000111000000101010',
            },
            {
                'mips' : "add $t1, $t2, $s2",
                'bin' : '00000001010100100100100000100000',
            },
            {
                'mips' : "lw $s1, 12($sp)",
                'bin' : '10001111101100010000000000001100',
            },
            {
                'mips' : "beq $s1, $s2, 9384",
                'bin' : '00010010001100100010010010101000',
            },
            {
                'mips' : "j 9384",
                'bin' : '00001000000000000010010010101000',
            },
            {
                'mips' : "add $s1, $s1, $s2",
                'bin' : '00000010001100101000100000100000',
            },
            {
                'mips' : "beq $s1, $s2, 2094",
                'bin' : '00010010001100100000100000101110',
            },
            {
                'mips' : "lw $s1, 44($sp)",
                'bin' : '10001110001111010000000000101100',
            },
            {
                'mips' : "jal 2094",
                'bin' : '00001100000000000000100000101110',
            },
        ]
        self.test_function(self, im.random_instruction)
        
        self.test_function(self, im.create_R_Type_bin)
        
        self.test_function(self, im.create_J_type_bin)
        
        self.test_function(self, im.create_I_type_bin)
        
        for dic in data_to_test:
            self.test_function(self, im.translate_bin_to_mips32, dic['mips'], dic['bin'])
            self.test_function(self, im.translate_mips32_to_bin, dic['bin'], dic['mips'])
            
        self.test_function(self, im.__main__)