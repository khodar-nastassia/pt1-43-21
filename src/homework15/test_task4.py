import task4
import unittest


class FuncTest(unittest.TestCase):
	def test_check_ordered_fractions(self):
		denominator = 1000000
		expected = '428570'
		result = task4.ordered_fractions(denominator)
		self.assertEqual(expected, result)

		with self.assertRaises(TypeError):
			task4.ordered_fractions('100000')


if __name__ == '__main__':
    unittest.main()
