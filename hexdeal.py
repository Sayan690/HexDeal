#!/usr/bin/python3

'''

Absolute no dealing with hexadecimal to integer absolute values. We have int() in python for that

hexdeal hex 'Hello World!'
-> 0x48656c6c6f20576f726c6421

hexdeal hex 'Hello World!' -rev
-> 0x21646c726f57206f6c6c6548

hexdeal hex 'Hello World!' -rev -cut 4 -comment -comment-symbol ";"
-> 0x21646c72 ; !dlr
	0x6f57206f ; oW o
	0x6c6c6548 ; lleH

hexdeal unhex "0x48656c6c6f20576f726c6421"
-> Hello World!

hexdeal unhex "21646c726f57206f6c6c6548" -rev
-> Hello World!

hexdeal edit "0x21646c726f57206f6c6c6548" -cut 4 -no-prefix
-> 21646c72
	6f57206f
	6c6c6548

'''

import sys
import argparse

class HexDeal:
	def __init__(self, args):
		self.args = args
		self.data = self.args.data

		if self.args.mode != "hex":
			# Check if the user data consists of a "0x" prefix, if yes, remove it.
			if self.data[:2] == "0x":
				self.data = self.data[2:]

	def to_char(self, hexa: hex) -> str:
		# hexadecimal -> chars

		string = ""

		for i in range(0, len(hexa), 2):
			char = hexa[i] + hexa[i+1]
			string += chr(int(char, 16))

		return string

	def to_hex(self):
		hexa = ''.join(hex(ord(char)).replace("0x", "") for char in self.data)

		self.data = hexa
		self.edit()

	def from_hex(self):
		if self.args.rev:
			c = ""
			for i in range(len(self.data)-1, 0, -2):
				c += self.data[i-1] + self.data[i]
			self.data = c
			print(self.data)

		self.data = self.to_char(self.data)
		self.edit()

	def edit(self):
		out = [self.data]

		# Cut
		if self.args.cut:
			n = self.args.cut * 2 # 1 character byte = 2 hexadecimal digits

			out = [(self.data[i:i+n]) for i in range(0, len(self.data), n)]

		newout = []
		for x in out:
			# Deal with reversed character bytes
			if self.args.rev and self.args.mode != "unhex":
				c = ""
				for i in range(len(x)-1, 0, -2):
					c += x[i-1] + x[i]
				x = c

			# Deal with comments
			if self.args.comment:
				string = self.to_char(x)
				x = f"{x} {self.args.cs} {string}"

			newout.append(x)
		if self.args.rev:
			newout = list(reversed(newout))

		for x in newout:
			if self.args.noprefix or self.args.mode == "unhex":
				print(x)
			else:
				print("0x" + x)

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description = "Hexadecimal characters dealer.")
	parser.add_argument("mode", help = "Mode to run. [hex, unhex, edit]", choices = ("hex", "unhex", "edit"))
	data = parser.add_argument("data", help = "Data provided by the user.")
	if not sys.stdin.isatty():
		data.nargs = '?'
		data.default = sys.stdin.read()
	parser.add_argument("-rev", help = "Reverse the input.", action = "store_true", default = False)
	parser.add_argument("-cut", help = "Cut the output as specified number of character bytes.", type = int, metavar = "")
	parser.add_argument("-comment", help = "Write the character notations of output side by side.", action = "store_true", default = False)
	parser.add_argument("-comment-symbol", help = "Comment symbol. (default: \";\")", default = ";", metavar = "", dest = "cs")
	parser.add_argument("-no-prefix", help = "Don't include the \"0x\" prefix in the output.", action = "store_true", default = False, dest = "noprefix")

	args = parser.parse_args()

	hexdeal = HexDeal(args)

	if args.mode == "hex":
		hexdeal.to_hex()

	elif args.mode == "unhex":
		if args.comment:
			print("[-] Comments aren't available with \"unhex\"")
			exit()
		hexdeal.from_hex()

	else:
		hexdeal.edit()

