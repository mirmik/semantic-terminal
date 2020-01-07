from semterm.session import Session
from semterm.dialog import Dialog
from semterm.console import Console

from semterm.dialogs.starter import StarterDialog
from semterm.dialogs.camera import CameraDialog

from argparse import ArgumentParser 
import sys

current_dialog = None
session = Session()

session.add_dialog(StarterDialog())
session.add_dialog(CameraDialog())

def main():
	parser = ArgumentParser()
	parser.add_argument("--debug", action="store_true")

	args = parser.parse_args(sys.argv[1:])

	console = Console(session, debug=args.debug)
	console.repl()

if __name__ == "__main__":
	main()