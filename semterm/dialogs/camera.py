import semterm.dialog
import semterm.util as util
import os

class CameraDialog(semterm.dialog.Dialog):
	trigger_list = [ "показать" ]
	target_list = [ "камера" ]

	def __init__(self):
		super().__init__()

	def estimate(self, sents):
		verb = self.first_verb(sents)
		noun = self.first_noun(sents)

		if self.debug_mode:
			print("VERB:", verb)
			print("NOUN:", noun)

		if verb is None or noun is None:
			return 0.0

		if verb.normal_form in self.trigger_list and noun.normal_form in self.target_list:
			self.stash = noun.normal_form
			return 1.0

		return 0.0

	def apply(self):
		if self.debug_mode:
			print("self", "apply")

		util.execute_with_terminal(cmd="gst-launch-1.0 v4l2src device=/dev/video0 ! video/x-raw,width=640,height=480 ! autovideosink")
