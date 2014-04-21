import pexpect

service = "python"
cmd = "print ('hello')"


child = pexpect.spawn("python try.py")
child.expect('.*')
print child.after
#child.expect('\n>>>')
#child.sendline(cmd)
#child.expect('\n>>>')
#print child.before