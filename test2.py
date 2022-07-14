from unittest import TestCase, main
from dog import Dog

class DogTestCase(TestCase):
    def setUp(self) -> None:
        self.dog = Dog('sparky', 5)
    
    def test_1_init_name(self):
        self.assertTrue(self.dog.name=='Sparky')
    
    def test_2_init_age(self):
        self.assertTrue(self.dog.age==5)
    
    def test_3_speak(self):
        self.assertEqual(self.dog.speak(),'Bark')

    def test_4_birthday(self):
        self.dog.birthday()
        self.assertTrue(self.dog.age==6)

    def test_5_name_change(self):
        self.dog.change_name('buster')
        self.assertTrue(self.dog.name=='Buster')
    