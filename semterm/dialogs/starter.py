import semterm.dialog
import os

class StarterDialog(semterm.dialog.Dialog):
	trigger_list = [ "активировать", "запустить", "инициировать", "включить" ]
	target_list = [ "терминал", "браузер" ]

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

		if self.stash == "терминал": os.system("terminator &")
		elif self.stash == "браузер": os.system("firefox &")