import test

while True:
	text = input('oreo > ')
	result, error = test.run("<stdin>", text)

	if error: print(error.as_string())
	else: print(result)
