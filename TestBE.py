import unittest
from easyBE import easyBE

class TestEasyBE(unittest.TestCase):
    def test_greet(self):
        my_instance = easyBE()
        self.assertEqual(my_instance.greetSelf(), "Hello, World!")

    def test_input(self):
        test = 'Test'
        my_instance = easyBE()
        self.assertEqual(my_instance.saySomething(test), test)

if __name__ == '__main__':
    unittest.main()
