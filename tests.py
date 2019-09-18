import unittest
from writer import Writer
from reader import Reader

class TestIntegers(unittest.TestCase):
	def test_int32(self):
		NUMBERS = [-2147483647, 0, 2147483647]

		writer = Writer()
		for n in NUMBERS:
			writer.write_int32(n)

		reader = Reader(writer.data)
		for n in NUMBERS:
			self.assertEqual(reader.read_int32(), n)

	def test_uint32(self):
		NUMBERS = [0, 127, 1 << 21]

		writer = Writer()
		for n in NUMBERS:
			writer.write_uint32(n)

		reader = Reader(writer.data)
		for n in NUMBERS:
			self.assertEqual(reader.read_uint32(), n)

if __name__ == '__main__':
	unittest.main()