import sublime
import sublime_plugin
import re

class FenCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		sels = self.view.sel()
		found = False
		for sel in sels:
			term = self.view.substr(sel)
			if (len(sel) < 3):
				return
			# debug self.view.insert(edit, 0, "Searching..." +  term)

			pattern = re.compile("	(" + term + ")[ \t]+(.*)")

			for i, line in enumerate(open(r'ENGLISH_FRENCH.md')):
				for match in re.finditer(pattern, line):
				 # debug  res = 'Found on line %s: %s' % (i+1, match.group(2))
				 res = "<<" + match.group(2) + ">> "
				 self.view.insert(edit, 0, res)
				found = True
		if (not found):
			self.view.insert(edit, 0, "<<NOT FOUND>>")	

