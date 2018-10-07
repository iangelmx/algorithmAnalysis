def getInstruccion(program, index):
	if "SAME" not in program[index]:
		return program[index]
	else:
		inst = program[index].split()
		return getInstruccion( program, (int(inst[2])-1) )

def decode(program):
	positionAux = 0
	for instruction in program:
		if "SAME" in instruction:
			inst = instruction.split()
			instruction = getInstruccion( program, (int(inst[2])-1) )

		if instruction == "RIGHT":
			positionAux += 1
		elif instruction == "LEFT":
			positionAux -= 1
	return positionAux

if __name__ == "__main__":
	try:
		testCases = int( input("") )
		for a in range(0, testCases):
			position = 0
			n = int( input("") )
			program = []
			for b in range(0, n):
				program.append( input("").strip() )

			finalPosition = decode(program)
			print(finalPosition)

	except Exception as ex:
		#print(ex)
		pass