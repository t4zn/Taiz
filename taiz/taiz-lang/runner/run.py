import taiz

while True:
	text = input('taiz > ')
	if text.strip() == "": continue
	result, error = taiz.run('<terror>', text)

	if error:
		print(error.as_string())
	elif result:
		if len(result.elements) == 1:
			print(repr(result.elements[0]))
		else:
			print(repr(result))
