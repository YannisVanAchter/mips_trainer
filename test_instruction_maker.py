import unittest

from typing import Callable
import instruction_maker as im

class TestInstructionMaker(unittest.TestCase):
    def test_translate_bin_to_mips32(self, mips_expected, binary):
    
        returned = im.translate_bin_to_mips32(binary)

        self.assertEqual(mips_expected, returned)
        
    def test_translate_mips32_to_bin(self, mips, binary_expected):
    
        returned = im.translate_mips32_to_bin(mips)

        self.assertEqual(binary_expected, returned)
        
    
    
    def setUp(self):
        def test_function(func: Callable = im.random_instruction, arg=None, expected=None, test=True):
            print("In function : ", func)
            try:
                if arg != None:
                    r =  func(test=test)
                    print(r)
                    return None
                r = func(arg, test=test)
                if r != expected: print(f"expected : {expected} \nreturned : {r}")
            except Exception as e:
                print("Error : ", e)
        
        test_function(im.random_instruction)
        print()
        
        test_function(im.create_R_Type_bin)
        print()
        
        test_function(im.create_J_type_bin)
        print()
        
        test_function(im.create_I_type_bin)
        print()   

        # test_function(__main__)
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
        
        for dic in data_to_test:
            self.test_translate_bin_to_mips32(dic['mips'], dic['bin'])
            
        for dic in data_to_test:
            self.test_translate_mips32_to_bin(dic['mips'], dic['bin'])