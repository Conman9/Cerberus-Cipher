import argparse
import base64
from banner import banner

def menu():
	#parser = argparse.ArgumentParser(prog='CerberusCipher', description=banner())
	parser = argparse.ArgumentParser(description=banner())
	parser.add_argument('-e', '--encrypt', help='encrypt phrase',
						action='store')

	parser.add_argument('-d', '--decrypt', help='decrypt phrase',
						action='append')


	args = parser.parse_args()
	base64.standard_b64encode(args)
	print(args)
	#print(args.accumulate(args.Help))

menu()