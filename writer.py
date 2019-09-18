# Tools for writing packets.
import strings

class Writer:
	def __init__(self):
		self.data = bytearray()

	def write_byte(self, n: int):
		self.data.append(n)

	def write_bool(self, b: bool):
		self.write_byte(1 if b else 0)

	def write_int32(self, n: int):
		n &= 0xFFFFFFFF
		if n < 0x80 or (n > 0x81 and n <= 0xFF):
			self.write_byte(n)
		elif n <= 0xFFFF:
			self.write_byte(0x80)
			self.write_byte(n & 0xFF)
			self.write_byte((n >> 8) & 0xFF)
		else:
			self.write_byte(0x81)
			self.write_byte(n & 0xFF)
			self.write_byte((n >> 8) & 0xFF)
			self.write_byte((n >> 16) & 0xFF)
			self.write_byte((n >> 24) & 0xFF)

	def write_uint32(self, n: int):
		if n < 1 << 7:
			self.write_byte(n & 0xFF)
		elif n < 1 << 14:
			self.write_byte((n & 0x7F) | 0x80)
			self.write_byte((n >> 7) & 0xFF)
		elif n < 1 << 21:
		    self.write_byte((n & 0x7F) | 0x80)
		    self.write_byte(((n >> 7) & 0x7F) | 0x80)
		    self.write_byte((n >> 14) & 0xFF)
		else:
			self.write_byte((n & 0x7F) | 0x80)
			self.write_byte(((n >> 7) & 0x7F) | 0x80)
			self.write_byte(((n >> 14) & 0x7F) | 0x80)
			self.write_byte((n >> 21) & 0xFF)

	def write_string(self, s: str):
		for c in s:
			self.write_int32(strings.encode_char(c))
		
		self.write_int32(0)

