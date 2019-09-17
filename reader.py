# Tools for reading packets.
import strings
from error import DecodeError

class Reader:
	def __init__(self, data: bytes):
		self.data = data

	def read_byte(self) -> int:
		if len(self.data) == 0:
			raise DecodeError('Reached end of packet')

		b = self.data[0]
		self.data = self.data[1:]

		return b

	def read_bool(self) -> bool:
		b = self.read_byte()
		if b == 1:
			return True
		elif b == 0:
			return False
		else:
			raise DecodeError('Invalid value for bool: ' + str(b))

	def read_int32(self) -> int:
		b = self.read_byte()
		if b == 0x80:
			return self.read_byte() + (self.read_byte() << 8)
		elif b == 0x81:
			return self.read_byte() + (self.read_byte() << 8) + (self.read_byte() << 16) + (self.read_byte() << 24)
		else:
			return b

	def read_uint32(self) -> int:
		n = self.read_byte()
		if n & (1 << 7) != 0:
			n += (self.read_byte() << 7) - (1 << 7)
		
		if n & (1 << 14) != 0:
			n += (self.read_byte() << 14) - (1 << 14)

		if n & (1 << 21) != 0:
			n += (self.read_byte() << 14) - (1 << 14)

		if n & 1 << 28 != 0:
			n += 0x0F << 24

		return n

	def read_string(self) -> str:
		s = ''

		while True:
			n = self.read_int32()
			if n == 0:
				return s

			s += strings.decode_char(n)
		
