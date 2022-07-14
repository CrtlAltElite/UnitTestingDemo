from unittest import TestCase, main
from wbs import firstc, numsum

class NumSumTestCase(TestCase):
    def test_1_base(self):
        self.assertEqual(numsum(1234),10)

    def test_2_zeros(self):
        self.assertEqual(numsum(0000),0)

    def test_3_base_again(self):
        self.assertEqual(numsum(5555),20)


class FirstCTestCase(TestCase):
    def test_1_con_first(self):
        self.assertTrue(firstc('cat')=='c')
    
    def test_2_con_second(self):
        self.assertEqual(firstc('obo'),'b')

    def test_3_con_third(self):
        self.assertEqual(firstc('eel'),'l')

    def test_4_no_con(self):
        self.assertFalse(firstc('euouae'))

    def test_5_all_numbers(self):
        self.assertFalse(firstc("1234567"))

    def test_6_cont_numbers(self):
        self.assertEqual(firstc("123k567"), "k")

    def test_7_con_first_with_caps(self):
        self.assertTrue(firstc('CAT')=='C')

    def test_8_con_second_with_caps(self):
        self.assertTrue(firstc('OBO')=='B')

    

