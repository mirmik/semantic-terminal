from semterm.session import Session
from semterm.dialog import Dialog
from semterm.console import Console

current_dialog = None
session = Session()

def main():
	console = Console(session)
	console.repl()

if __name__ == "__main__":
	main()