import unittest
import prac11

class TestMain(unittest.TestCase):
    def setUp(self):
        print("About to run a function")

    def test_do_stuff(self):
        """Test Case 1"""
        test_param = 10
        result = prac11.do_stuff(test_param)
        self.assertEqual(result, 15)
    
    def test_do_stuff2(self):
        """Test Case 2"""
        test_param = "abc"
        result = prac11.do_stuff(test_param)
        self.assertIsInstance(result, ValueError)
    
    def test_do_stuff3(self):
        """Test Case 3"""
        test_param = None
        result = prac11.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")
    
    def test_do_stuff4(self):
        """Test Case 4"""
        test_param = ''
        result = prac11.do_stuff(test_param)
        self.assertEqual(result, "Please enter number")

    def tearDown(self):
        print("Cleaning up")


if __name__ == "__main__":
    unittest.main()

# python -m unittest -v
