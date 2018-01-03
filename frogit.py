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
						res += "• " + term + ": " + match.group(2) + '<br>'
						found = True

				html = """
			    <body>
			        <style>
			        	.arrow-down { width: 0; height: 0; border-style: solid; border-width: 7px 5px; border-color: #ffd500 transparent transparent transparent; }
			            div { color: #ffd500; border:solid 1px black; margin-top:-5px; }			         
			        </style>
			        <div class="arrow-down"></div>
			        <div>%s</div>			        
			    </body>
				""" % (res)	
				self.view.show_popup(html, max_width=256)	
								
				# Add missing translation in the en/fr file. Todo: automatic add in right position with a simple translation
				if (not found):
					with open(enfr, "a") as f:						
						f.write("\r\n"+term)
		    			
