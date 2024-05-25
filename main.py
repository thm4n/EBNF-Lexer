#!/usr/bin/python3

from argparse import ArgumentParser

from ParseEBNF import ParseEBNF

def main():
	arg_parser = ArgumentParser()
	arg_parser.add_argument('path', type=str, help='Path to  the ebnf file')
	args = arg_parser.parse_args()
	
	ParseEBNF(args.path)

if __name__ == '__main__':
	main()
