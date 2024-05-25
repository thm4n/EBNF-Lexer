from typing import List, Dict, Tuple, Literal
from enum import Enum
import re

class ParseEBNF():
	class TokenSpecifications(Enum):
		SKIP          = r'[ \t]+'       # Skip over spaces and tabs
		COMMENT       = r'\(\*.*?\*\)'  # Comments
		IDENTIFIER    = r'[a-zA-Z_]\w*' # Identifiers
		ASSIGN        = r'::='          # Assignment operator
		ALTERATION    = r'\|'           # Alternation
		LITERAL       = r'"[^"]*"'      # String literals
		LEFT_PAREN    = r'\('           # Left parenthesis
		RIGHT_PAREN   = r'\)'           # Right parenthesis
		LEFT_BRACKET  = r'\['           # Left brace
		RIGHT_BRACKET = r'\]'           # Right brace
		LEFT_BRACE    = r'\{'           # Left brace
		RIGHT_BRACE   = r'\}'           # Right brace
		STAR          = r'\*'           # Kleene star
		COMMA         = r','            # Comma
		SEMICOLON     = r';'            # Semicolon
		NEWLINE       = r'\n'           # Newline
		MISMATCH      = r'.'            # Any other character

	class SyntaxError(Exception):
		def __init__(self, message):
			super().__init__(message)
			self.message = message

		def __str__(self):
			return f"Syntax Error: {self.message}"

	def __init__(self, ebnf_path: str):
		with open(ebnf_path, 'r') as file:
			self.__tokenize__(file.read())

		self.__parse__()

	def __tokenize__(self, input_string: str) -> List[str]:
		tok_regex = '|'.join(f'(?P<{regex.name}>{regex.value})' for regex in self.TokenSpecifications)
		get_token = re.compile(tok_regex).match
		self.tokens = []
		line_no = 1
		
		mo = get_token(input_string)
		while mo is not None:
			kind = mo.lastgroup
			value = mo.group(kind)
			
			if kind != 'SKIP' and kind != 'COMMENT' and kind != 'MISMATCH' and kind != 'NEWLINE':
				self.tokens.append((kind, value))
			
			if kind == 'MISMATCH':
				raise RuntimeError(f'{value!r} unexpected on line {line_no}')
			elif kind == 'NEWLINE':
				line_no += 1

			mo = get_token(input_string, mo.end()) if mo else None
	
	def __get_curr_token__(self):
		for token_type, token in self.tokens:
			yield (token_type, token)
		return (None, None)

	def __parse__(self):
		self.rules = {}
		
		token_type, token = self.__get_curr_token__()
		while token_type is not None and token is not None:
			if token_type is self.TokenSpecifications.IDENTIFIER:
				rule = self.__read_identifier__()
				self.rules[token] = rule
					

			token_type, token = self.__get_curr_token__()

	def __read_identifier__(self) -> Tuple[TokenSpecifications, str]:
		token_type, token = self.__expect__([self.TokenSpecifications.ASSIGN])

		# the token_type is for sure ASSIGN
		# now should parse expression		

	def __expect__(self, expected_types: List[TokenSpecifications]) -> Tuple[TokenSpecifications, str]:
		token_type, token = self.__get_curr_token()
		if token_type is None or token is None:
			raise self.SyntaxError("Unexpected ''")
		if token_type not in expected_types:
			raise self.SyntaxError(f"Unexpected {token_type}: {token!r}")
		
		return (token_type, token)
