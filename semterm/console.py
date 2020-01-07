class Console:
	def __init__(self, session):
		self.session = session

	def repl(self):
		while True:
			inp = input()
			self.session.input(inp.split())
