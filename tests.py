import unittest
from writer import Writer
from reader import Reader
import strings

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

class TestString(unittest.TestCase):
	def test_string(self):
		DATA = ''.join([chr(u) for u, _ in strings.U2C_TABLE.items()])

		writer = Writer()
		writer.write_string(DATA)

		self.assertEqual(Reader(writer.data).read_string(), DATA)

if __name__ == '__main__':
	unittest.main()