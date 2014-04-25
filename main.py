from flask import Flask, render_template, flash, request
import pexpect

app = Flask(__name__)
app.secret_key = 'guess'

def reset():
	f = open("templates/previous.html",'w')
	f.write("")
	f.close

@app.route('/', methods = ['GET','POST'])
@app.route('/index', methods = ['GET','POST'])
def index():
	home = False
	if request.method == 'POST':
		cmd = request.form['command']
		ftemp = open('templates/previous.html', 'a')
		text = ""
		if cmd == "clear" or cmd == "cls":
			reset()
		elif cmd.endswith(":"):
			child.sendline(cmd)
			child.expect ('\n...')
			output = child.before

			if output.strip() == cmd.strip():
			 	text = """>>>&nbsp;""" + cmd + """<br>"""
			else:
			 	text = """>>>&nbsp;""" + cmd.strip() + """<br>
			 	&nbsp;<font color="RED">""" + output.replace(cmd,"").strip() + """</font><br>"""
			home = True
		
		elif cmd.startswith("    "):
			child.sendline(cmd)
			child.expect ('\n...')
			output = child.before

			if output.strip() == cmd.strip():
			 	text = """...&nbsp;&nbsp;&nbsp;""" + cmd + """<br>"""
			else:
			 	text = """>>>&nbsp;""" + cmd.strip() + """<br>
			 	&nbsp;<font color="RED">""" + output.replace(cmd,"").strip() + """</font><br>"""
			home = True
		else:
			child.sendline(cmd)
			child.expect ('\n>>>')
			output = child.before
			if output.strip() == cmd.strip():
				text = """>>>&nbsp;""" + cmd + """<br>"""
			else:
				text = """>>>&nbsp;""" + cmd.strip() + """<br>
				&nbsp;<font color="RED">""" + output.replace(cmd,"").strip() + """</font><br>"""
			
		ftemp.write(text)
		ftemp.close
		ftemp.flush()
		return render_template('index.html', home = home)
	return render_template('index.html', home = home)


if __name__ == '__main__':
	child = pexpect.spawn("python")
	child.expect('\n>>>')
	reset()
	app.run(debug = True)