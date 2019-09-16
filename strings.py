from error import EncodeError, DecodeError

# Unicode to cubecode table.
U2C_TABLE = {
	0x000: 0x000, 0x0C0: 0x001, 0x0C1: 0x002, 0x0C2: 0x003, 0x0C3: 0x004, 0x0C4: 0x005, 0x0C5: 0x006, 0x0C6: 0x007, 
	0x0C7: 0x008, 0x009: 0x009, 0x00A: 0x00A, 0x00B: 0x00B, 0x00D: 0x00D, 0x0C8: 0x00E, 0x0C9: 0x00F, 0x0CA: 0x010, 
	0x0CB: 0x011, 0x0CC: 0x012, 0x0CD: 0x013, 0x0CE: 0x014, 0x0CF: 0x015, 0x0D1: 0x016, 0x0D2: 0x017, 0x0D3: 0x018, 
	0x0D4: 0x019, 0x0D5: 0x01A, 0x0D6: 0x01B, 0x0D8: 0x01C, 0x0D9: 0x01D, 0x0DA: 0x01E, 0x0DB: 0x01F, 0x020: 0x020, 
	0x021: 0x021, 0x022: 0x022, 0x023: 0x023, 0x024: 0x024, 0x025: 0x025, 0x026: 0x026, 0x027: 0x027, 0x028: 0x028, 
	0x029: 0x029, 0x02A: 0x02A, 0x02B: 0x02B, 0x02C: 0x02C, 0x02D: 0x02D, 0x02E: 0x02E, 0x02F: 0x02F, 0x030: 0x030, 
	0x031: 0x031, 0x032: 0x032, 0x033: 0x033, 0x034: 0x034, 0x035: 0x035, 0x036: 0x036, 0x037: 0x037, 0x038: 0x038, 
	0x039: 0x039, 0x03A: 0x03A, 0x03B: 0x03B, 0x03C: 0x03C, 0x03D: 0x03D, 0x03E: 0x03E, 0x03F: 0x03F, 0x040: 0x040, 
	0x041: 0x041, 0x042: 0x042, 0x043: 0x043, 0x044: 0x044, 0x045: 0x045, 0x046: 0x046, 0x047: 0x047, 0x048: 0x048, 
	0x049: 0x049, 0x04A: 0x04A, 0x04B: 0x04B, 0x04C: 0x04C, 0x04D: 0x04D, 0x04E: 0x04E, 0x04F: 0x04F, 0x050: 0x050, 
	0x051: 0x051, 0x052: 0x052, 0x053: 0x053, 0x054: 0x054, 0x055: 0x055, 0x056: 0x056, 0x057: 0x057, 0x058: 0x058, 
	0x059: 0x059, 0x05A: 0x05A, 0x05B: 0x05B, 0x05C: 0x05C, 0x05D: 0x05D, 0x05E: 0x05E, 0x05F: 0x05F, 0x060: 0x060, 
	0x061: 0x061, 0x062: 0x062, 0x063: 0x063, 0x064: 0x064, 0x065: 0x065, 0x066: 0x066, 0x067: 0x067, 0x068: 0x068, 
	0x069: 0x069, 0x06A: 0x06A, 0x06B: 0x06B, 0x06C: 0x06C, 0x06D: 0x06D, 0x06E: 0x06E, 0x06F: 0x06F, 0x070: 0x070, 
	0x071: 0x071, 0x072: 0x072, 0x073: 0x073, 0x074: 0x074, 0x075: 0x075, 0x076: 0x076, 0x077: 0x077, 0x078: 0x078, 
	0x079: 0x079, 0x07A: 0x07A, 0x07B: 0x07B, 0x07C: 0x07C, 0x07D: 0x07D, 0x07E: 0x07E, 0x0DC: 0x07F, 0x0DD: 0x080, 
	0x0DF: 0x081, 0x0E0: 0x082, 0x0E1: 0x083, 0x0E2: 0x084, 0x0E3: 0x085, 0x0E4: 0x086, 0x0E5: 0x087, 0x0E6: 0x088, 
	0x0E7: 0x089, 0x0E8: 0x08A, 0x0E9: 0x08B, 0x0EA: 0x08C, 0x0EB: 0x08D, 0x0EC: 0x08E, 0x0ED: 0x08F, 0x0EE: 0x090, 
	0x0EF: 0x091, 0x0F1: 0x092, 0x0F2: 0x093, 0x0F3: 0x094, 0x0F4: 0x095, 0x0F5: 0x096, 0x0F6: 0x097, 0x0F8: 0x098, 
	0x0F9: 0x099, 0x0FA: 0x09A, 0x0FB: 0x09B, 0x0FC: 0x09C, 0x0FD: 0x09D, 0x0FF: 0x09E, 0x104: 0x09F, 0x105: 0x0A0, 
	0x106: 0x0A1, 0x107: 0x0A2, 0x10C: 0x0A3, 0x10D: 0x0A4, 0x10E: 0x0A5, 0x10F: 0x0A6, 0x118: 0x0A7, 0x119: 0x0A8, 
	0x11A: 0x0A9, 0x11B: 0x0AA, 0x11E: 0x0AB, 0x11F: 0x0AC, 0x130: 0x0AD, 0x131: 0x0AE, 0x141: 0x0AF, 0x142: 0x0B0, 
	0x143: 0x0B1, 0x144: 0x0B2, 0x147: 0x0B3, 0x148: 0x0B4, 0x150: 0x0B5, 0x151: 0x0B6, 0x152: 0x0B7, 0x153: 0x0B8, 
	0x158: 0x0B9, 0x159: 0x0BA, 0x15A: 0x0BB, 0x15B: 0x0BC, 0x15E: 0x0BD, 0x15F: 0x0BE, 0x160: 0x0BF, 0x161: 0x0C0, 
	0x164: 0x0C1, 0x165: 0x0C2, 0x16E: 0x0C3, 0x16F: 0x0C4, 0x170: 0x0C5, 0x171: 0x0C6, 0x178: 0x0C7, 0x179: 0x0C8, 
	0x17A: 0x0C9, 0x17B: 0x0CA, 0x17C: 0x0CB, 0x17D: 0x0CC, 0x17E: 0x0CD, 0x404: 0x0CE, 0x411: 0x0CF, 0x413: 0x0D0, 
	0x414: 0x0D1, 0x416: 0x0D2, 0x417: 0x0D3, 0x418: 0x0D4, 0x419: 0x0D5, 0x41B: 0x0D6, 0x41F: 0x0D7, 0x423: 0x0D8, 
	0x424: 0x0D9, 0x426: 0x0DA, 0x427: 0x0DB, 0x428: 0x0DC, 0x429: 0x0DD, 0x42A: 0x0DE, 0x42B: 0x0DF, 0x42C: 0x0E0, 
	0x42D: 0x0E1, 0x42E: 0x0E2, 0x42F: 0x0E3, 0x431: 0x0E4, 0x432: 0x0E5, 0x433: 0x0E6, 0x434: 0x0E7, 0x436: 0x0E8, 
	0x437: 0x0E9, 0x438: 0x0EA, 0x439: 0x0EB, 0x43A: 0x0EC, 0x43B: 0x0ED, 0x43C: 0x0EE, 0x43D: 0x0EF, 0x43F: 0x0F0, 
	0x442: 0x0F1, 0x444: 0x0F2, 0x446: 0x0F3, 0x447: 0x0F4, 0x448: 0x0F5, 0x449: 0x0F6, 0x44A: 0x0F7, 0x44B: 0x0F8, 
	0x44C: 0x0F9, 0x44D: 0x0FA, 0x44E: 0x0FB, 0x44F: 0x0FC, 0x454: 0x0FD, 0x490: 0x0FE, 0x491: 0x0FF,
}

C2U_TABLE = {}

for u, c in U2C_TABLE.items():
	C2U_TABLE[c] = u

def encode_char(c: str):
	try:
		return U2C_TABLE[ord(c)]
	except KeyError:
		raise EncodeError('Unencodable character: \'' + c + '\'')

def decode_char(c: int):
	try:
		return C2U_TABLE[c]
	except KeyError:
		raise EncodeError('Undecodable character: \'' + str(c) + '\'')