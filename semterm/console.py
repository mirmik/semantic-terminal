class Console:
	def __init__(self, session, debug=False):
		self.session = session
		session.set_debug_mode(debug)

	def repl(self):
		while True:
			inp = input()
			self.session.input(inp)
