import basic
from functools import cache

def func(text):
	result, error = basic.run("<stdin>", text)

	if error: return error.as_string()
	else: return result

while True:
	try:
		text = input('hmm > ')
	except:
		print("\nClosing...")
		exit()

	if text in ("close()", "close"):
		print("Closing ...")
		exit()

	print(func(text))
