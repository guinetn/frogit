import sublime
import sublime_plugin
import re

# SETUP 1/1: Dictionary file path
dictionary = r'N:\md\md\.ENGLISH_FRENCH.md'


# DANGER ZONE. Do not change code below

class FrogitCommand(sublime_plugin.TextCommand):
	def run(self, edit):				
		translations = "" 		# items translated 
		
		# Make a dictionary of selected words & compiled regex
		terms = {}
		for region in self.view.sel():  #get words 'cursorized'
			term = self.view.substr(self.view.word(region))
			if len(term) > 2:								
				terms[term] = re.compile("^\s(" + term + "s?)[ \t]+(.*)", re.I)  # Case insensitive, precompilation for perf
				
			# Extend lexical search
			# Transform trailing '…ies' to '…y'			
			if term[-3:].lower() == 'ies':
				term = term[0:-3] + 'y'
				terms[term] = re.compile("^\s(" + term + ")[ \t]+(.*)", re.I)  				

		if len(terms) > 0:			
			# Search in dictionary file (only 1 pass)
			
			for line in open(dictionary):
				for item in terms:													
					translated = ""				
					for match in re.finditer(terms[item], line):
						translated += "• " + item + ": " + match.group(2) + '<br>'					
					translations += translated				

			# Add missing terms in the dictionnay. Todo: Use an api to automatic add the translation in the right place in the dictionary
			with open(dictionary, "a") as f:
				missingTerms = {("• " + x + ": ") for x in terms if x not in translations}   # missing terms in dictionary file				
				if len(missingTerms) > 0:
					translations += "______________<br>NOT FOUND:<br>" 		

					for x in missingTerms:
						translations += x + "<br>" 		
						f.write("\r\n" + x)								
				
			html = """
			    	<body>
			        	<style>
			            	.arrow-down { width: 0; height: 0; border-style: solid; border-width: 7px 5px; border-color: #ffd500 transparent transparent transparent}
			            	div { color: #ffd500; border:solid 1px black; margin-top:-5px}
			        	</style>
			        	<div class="arrow-down"></div>
			        	<div>%s</div>
			    	</body>
				""" % (translations)
			self.view.show_popup(html, max_width=256)
		
# TESTING AREA: some words to select with multi-cursor 
# afford best translations to user
