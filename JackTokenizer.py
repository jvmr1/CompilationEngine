import re

class JackTokenizer (object):

	def __init__(self, path):
		with open(path) as in_file:
			tokens = in_file.read()

		pattern_comment = '\/(\*|)\*(.|\n)*?\*\/|\/\/.*'
		self._pattern_symbol = '\{|\}|\(|\)|\[|\]|\.|\,|\;|\+|\-|\*|' \
							   '\/|\&|\||\<|\>|\=|\~'
		self._pattern_int = '\d+'
		self._pattern_identifier = '[a-zA-Z_][a-zA-Z0-9_]*'
		self._pattern_keyword = 'class|constructor|function|method|field|' \
								'static|var|int|char|boolean|void|true|' \
								'false|null|this|let|do|if|else|while|return'
		self._pattern_string = '".*?"'
		patterns = self._pattern_symbol + '|' + self._pattern_int + '|' +  self._pattern_identifier + '|' + self._pattern_keyword + '|' + self._pattern_string
		tokens = re.sub(pattern_comment, '', tokens)
		tokens = re.findall(patterns, tokens)
		self.tokens = tokens
		self.currToken = None

	def hasMoreTokens(self):
		if self.tokens:
			return True
		return False

	def advance(self):
		if self.hasMoreTokens():
			self.currToken = self.tokens.pop(0)

	def tokenType(self):
		if re.search(self._pattern_string, self.getToken()):
			return 'stringConst'
		elif re.search('^(' + self._pattern_keyword + ')$', self.getToken()):
			return 'keyword'
		elif re.search(self._pattern_symbol, self.getToken()):
			return 'symbol'
		elif re.search(self._pattern_int, self.getToken()):
			return 'intConst'
		elif re.search(self._pattern_identifier, self.getToken()):
			return 'identifier'

	def getToken(self):
		return self.currToken

	def nextToken(self):
		if self.hasMoreTokens():
			return self.tokens[0]
