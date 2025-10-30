# Test file to verify IronPython 2.7 syntax
# This should have NO syntax errors for IronPython 2.7

import rhinoscriptsyntax as rs

# Test 1: Simple print
print "Test 1: Basic print works"

# Test 2: String formatting
name = "Rhino"
print "Test 2: Hello from {0}".format(name)

# Test 3: Exec with string literal
try:
	code = 'print "Test 3: Exec works"'
	exec code
except:
	print "Test 3: Exec failed"

# Test 4: Exec with scope
try:
	my_globals = {'rs': rs}
	code = 'print "Test 4: Exec with scope works"'
	exec code in my_globals
except:
	print "Test 4: Exec with scope failed"

# Test 5: Multi-line exec
try:
	code = '''
x = 5
y = 10
print "Test 5: x + y = " + str(x + y)
'''
	exec code
except:
	print "Test 5: Multi-line exec failed"

print "All syntax tests complete"
