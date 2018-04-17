#1. Place Interpreter(cmd) code into following file
input_file = open('interactive_session.py', 'r')

#2. Run this script in same folder as interactive_session.py

#3. Resulting mostly runnable code will be placed here:
OUTPUT_FILE_NAME = 'output.py'


errors = ['TypeError', 'Traceback', 'NameError', 'SyntaxError',
	  'ImportError', 'AttributeError', 'IndentationError'
	  '<built-in method', 'KeyboardInterrupt'
	 ]

out = []

interpreter_output = False
start_puting_into_output_file = False

for line in input_file:

	#first line is commented out
	if line[:11] == 'Type "help"':
		out.append('#' + line)
		interpreter_output = True
		start_puting_into_output_file = True
	
	if start_puting_into_output_file == False:
		out.append('\n')
		continue
		
	#  File "<stdin>", line 1, in <module>
	if line[:2] == '  ':
		out.append('#' + line)
		interpreter_output = True
		
	#>>> [0, 2]
	#[0, 2]
	if line[0] == '[':
		out.append('#' + line)
		interpreter_output = True
		
	#>>> ^Z
	if line[:5] == '>>> ^':
		out.append('#' + line)
		interpreter_output = True
		
	for error in errors:
		if line.startswith(error):
			out.append('#' + line)
			interpreter_output = True
	
	if not interpreter_output:
		
		not_interpreter_output = False
		
		if line[:4] == '>>> ':
			line = line[4:]
			not_interpreter_output = True
			
		#dealing with up to 6 indentations
		if line[:48] == '...                                             ':
			line = '\t' + '\t' + '\t' + '\t' + '\t' + '\t' + line[48:]
			not_interpreter_output = True
			
		if line[:40] == '...                                     ':
			line = '\t' + '\t' + '\t' + '\t' + '\t' + line[40:]
			not_interpreter_output = True
			
		if line[:32] == '...                             ':
			line = '\t' + '\t' + '\t' + '\t' + line[32:]
			not_interpreter_output = True

		if line[:24] == '...                     ':
			line = '\t' + '\t' + '\t' + line[24:]
			not_interpreter_output = True
			
		if line[:16] == '...             ':
			line = '\t' + '\t' + line[16:]
			not_interpreter_output = True
			
		if line[:8] == '...     ':
			line = '\t' + line[8:]
			not_interpreter_output = True
			
		if line[:4] == '... ':
			line = line[4:]
			not_interpreter_output = True
		
		if not_interpreter_output == False:
			out.append('#' + line)
		else:
			#append line without adding '#' at the start because it is user input
			out.append(line)
	
	interpreter_output = False
	
out_file = open(OUTPUT_FILE_NAME, 'w')

for line in out:
	out_file.write(line)
