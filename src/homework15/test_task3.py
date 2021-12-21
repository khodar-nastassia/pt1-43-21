import task3
import unittest


class FuncTest(unittest.TestCase):
    '''Test for task3'''
    def test_check_count_of_word(self):
        expected = 2
        result = task3.count_of_word('hello world')
        self.assertEqual(expected, result)

        with self.assertRaises(TypeError):
            task3.count_of_word(123)


if __name__ == '__main__':
    unittest.main()
