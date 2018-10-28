original = input("")

flag = 0
chida=""
for char in original:
	if char == '"':
		flag += 1
		if flag%2 == 1:
			chida += "``"
		else:
			chida += "''"
	elif char == "\n":
		chida+="\n"
	else:
		chida+=char

print(chida)