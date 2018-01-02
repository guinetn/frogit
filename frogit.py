import sublime
import sublime_plugin
import re

enfr = r'N:\@md\md\.ENGLISH_FRENCH.md'

class FrogitCommand(sublime_plugin.TextCommand):
	def run(self, edit):		
		found = False
		res = ""
		term = ""
		for region in self.view.sel():  #get user selection
			term = self.view.substr(self.view.word(region))
			if len(term) > 2:
				pattern = re.compile("	(" + term + ")[ \t]+(.*)")

				for line in open(enfr):
					for match in re.finditer(pattern, line):
						res = match.group(2) 						
						found = True

				html = """
			    <body>
			        <style>
			            div { color: yellow; border:solid 1px black; }			         
			        </style>
			        <div>%s</div>			        
			    </body>
				""" % (res)	
				self.view.show_popup(html, max_width=512, on_navigate=lambda x:copy(self.view, x))	
								
				# Add missing translation in the en/fr file. Todo: automatic add in right position with a simple translation
				if (not found):
					with open(enfr, "a") as f:						
						f.write(term)
		    			