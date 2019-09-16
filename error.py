class EncodeError(Exception):
	def __init__(self, message):
		super().__init__(message)

class DecodeError(Exception):
	def __init__(self, message):
		super().__init__(message)