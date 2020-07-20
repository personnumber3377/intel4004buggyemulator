import binascii


def integernumber(n,bit_size):
   bin_number = bin(n)
   reverse_number = bin_number[-1:1:-1]
   reverse_number = reverse_number + (bit_size - len(reverse_number))*'0'
   return int(reverse_number,2)


def execinstruction(instruction):

	global selectedrammemorychip

	global selectedrammemoryregister





	binary_string = bin(int(instruction, 16))
	
	binary_string = binary_string[2:]
	
	binary_string = "0"*(8-len(binary_string)) + binary_string

	
	
	# nop instruction

	if binary_string == "00000000":
		registers[0] = registers[0] + 1
		
		return 0

	# jcn instruction

	if binary_string.startswith("0001"):
		
		
		if binary_string[4] == "1":
			
			if binary_string[5] == "1":

				if registers[1] != 0:
					registers[0] = int(instructionarray[registers[0]+1])
					return 0

			if binary_string[6] == "1":

				if registers[2] != "1":
					registers[0] = int(instructionarray[registers[0]+1])
					return 0

			if binary_string[7] == "1":

				if registers[3] != "0":
					registers[0] = int(instructionarray[registers[0]+1])
					return 0
			print("paska")
			registers[0] = registers[0] + 2
					

		else:
			
			if binary_string[5] == "1":
				if registers[1] == 0:
					registers[0] = int(instructionarray[registers[0]+1])
					return 0
					

			if binary_string[6] == "1":

				if registers[2] == "1":
					registers[0] = int(instructionarray[registers[0]+1])
					return 0

			if binary_string[7] == "1":

				if registers[3] == "0":
					registers[0] = int(instructionarray[registers[0]+1])
					return 0
			print("paska")
			registers[0] = registers[0] + 2




	# fim fetch immediate

	if binary_string.startswith("0010") and binary_string[7] == "0":

		
		registerpair = int(binary_string[4:7], 2)
		
		binarynumber = instructionarray[registers[0]+1]
		
		binarynumber = bin(int(binarynumber, 16))
		print(binarynumber)


		
		binarynumber = binarynumber[2:]

		binarynumber = "0"*(8-len(binarynumber)) + binarynumber
		
		print(binarynumber)

		num1 = int(binarynumber[0:4], 2)
		
		num2 = int(binarynumber[4:], 2)

		print(num1)

		print(num2)
		
		registers[2*registerpair+generalregisterbase] = num1
		registers[2*registerpair+generalregisterbase+1] = num2
		registers[0] = registers[0] + 2


	# src send register control

	if binary_string.startswith("0010") and binary_string[7] == "1":
		print("jumped into it")
		numshit = registers[2*int(binary_string[4:7], 2)+generalregisterbase]
		numshit2 = registers[2*int(binary_string[4:7], 2)+generalregisterbase+1]
		print(numshit)
		print(numshit2)
		numshit = str(bin(numshit))
		numshit2 = str(bin(numshit2))

		

		numshit = numshit[2:]

		numshit2 = numshit2[2:]

		print(numshit)
		print(numshit2 + " !!!")

		numshit = "0"*(4-len(numshit)) + numshit

		numshit2 = "0"*(4-len(numshit2)) + numshit2

		


		




			





		

			

		selectedrammemorychip = int(numshit[2:], 2)

		print("memory chip " + str(selectedrammemorychip) + " selected.")

		selectedrammemoryregister = int(numshit[2:4], 2)

		print("memory register " + str(selectedrammemoryregister) + " selected.")

		selectedrommemorychip = int(numshit[:4], 2)

		print("rom chip " + str(selectedrommemorychip) + " selected")



		



		newnumber = numshit + numshit2

		print(newnumber)

		newnumber = int(newnumber, 2)

		print(newnumber)

		print(type(newnumber))

		registers[4] = newnumber

		registers[0] = registers[0] + 1
		
		
		return 0



	# fin fetch indirect

	if binary_string.startswith("0011") and binary_string[7] == "0":



		numshit = registers[generalregisterbase]
		numshit2 = registers[generalregisterbase+1]
		print(numshit)
		print(numshit2)
		numshit = str(bin(numshit))
		numshit2 = str(bin(numshit2))

		newnumber = numshit[2:] + numshit2[2:]

		

		newnumber = int(newnumber, 2)


		memorycontent = memory[newnumber]
		print(memorycontent)
		print(newnumber)

		numero = bin(memorycontent)
		
		numero = str(numero[2:])+(8-len(numero[2:]))*"0"
		print(numero)

		firstregister = int(numero[0:4], 2)

		secondregister = int(numero[4:], 2)

		print(firstregister)
		print(secondregister)

		registers[2*int(binary_string[4:7], 2)+generalregisterbase] = firstregister
		registers[2*int(binary_string[4:7], 2)+generalregisterbase+1] = secondregister
		registers[0] = registers[0] + 1		



	# jin jump indirect

	

	if binary_string.startswith("0011") and binary_string[7] == "1":
		firstregister = registers[2*int(binary_string[4:7], 2)+generalregisterbase]
		secondregister = registers[2*int(binary_string[4:7], 2)+generalregisterbase+1]
		

		firstregister = bin(firstregister)

		secondregister = bin(secondregister)

		
		firstregister = firstregister[2:]
		secondregister = secondregister[2:]

		print(firstregister)
		print(secondregister)

		number = int((firstregister + secondregister), 2)

		print(number)

		registers[0] = memory[number]



	# jun jump unconditional

	if binary_string.startswith("0100"):
		first4bytes = binary_string[4:]
		last8bytes = instructionarray[registers[0]+1]
		last8bytes = bin(int(last8bytes, 16))
		last8bytes = last8bytes[2:]
		
		intshit = first4bytes + last8bytes
		
		integer = int(intshit, 2)
		

		

		registers[0] = integer



	# jms jump to subroutine


	if binary_string.startswith("0101"):
		global stackpointer
		first4bytes = binary_string[4:]
		last8bytes = instructionarray[registers[0]+1]
		last8bytes = bin(int(last8bytes, 16))
		last8bytes = last8bytes[2:]
		print(last8bytes)
		print(first4bytes)
		intshit = first4bytes + last8bytes
		print(intshit)
		integer = int(intshit, 2)
		stack[stackpointer] = registers[0] + 2
		stackpointer = stackpointer+1
		registers[0] = integer

	# inc increment

	if binary_string.startswith("0110"):
		incrementedregister = int(binary_string[4:], 2)

		registers[generalregisterbase+incrementedregister] = registers[generalregisterbase+incrementedregister]+1

		if registers[generalregisterbase+incrementedregister] > 255:
			registers[generalregisterbase+incrementedregister] = 0

		registers[0] = registers[0] + 1



	# isz increment and skip

	if binary_string.startswith("0111"):
		incrementedregister = int(binary_string[4:], 2)
		print("sonta")

		registers[generalregisterbase+incrementedregister] = registers[generalregisterbase+incrementedregister]+1
		if registers[generalregisterbase+incrementedregister] > 255:
			registers[generalregisterbase+incrementedregister] = 0

		if registers[generalregisterbase+incrementedregister] != 0:
			print("paskaaa")
			first4bytes = binary_string[4:]
			last8bytes = instructionarray[registers[0]+1]
			last8bytes = bin(int(last8bytes, 16))
			last8bytes = last8bytes[2:]
			print(last8bytes)
			print(first4bytes)
			intshit = last8bytes
			print(intshit)
			integer = int(intshit, 2)
		

			print(integer)

			registers[0] = integer
			return 0
		registers[0] = registers[0] + 2



	# add instruction


	if binary_string.startswith("1000"):
		print("paskaperse")
		print(int(binary_string[4:], 2))
		print(registers[generalregisterbase + int(binary_string[4:], 2)])
		registers[1] = registers[1] + registers[generalregisterbase + int(binary_string[4:], 2)]
		if registers[1] > 15:
			print("ooooooffff")
			registers[1] = 0
			registers[2] = 1
		registers[0] = registers[0] + 1


	# sub instruction

	if binary_string.startswith("1001"):
		print(registers[generalregisterbase+int(binary_string[4:], 2)])

		numbershit = registers[generalregisterbase+int(binary_string[4:], 2)]



		numbershit = bin(numbershit)
		numbershit = numbershit[2:]
		numbershit = "0"*(4-len(numbershit)) + numbershit
		numbershit = list(numbershit)
		print(numbershit)
		for i in range(0, len(numbershit)):
			if numbershit[i] =="0":
				print("inverted a zero to a one")
				numbershit[i] = "1"
				continue
			if numbershit[i] == "1":
				print("inverted a one to a zero")
				numbershit[i] = "0"
				continue
		print(str(numbershit) + " !!!!!!!")
		print(''.join(numbershit))
		numbershit = int(''.join(numbershit), 2)
		print(numbershit)
		registers[1] = registers[1] - registers[generalregisterbase+int(binary_string[4:], 2)]
		registers[0] = registers[0] + 1


	# ld load

	if binary_string.startswith("1010"):

		ldregister = int(binary_string[4:], 2)

		ldregister = registers[ldregister+generalregisterbase]

		registers[1] = ldregister

		registers[0] = registers[0]+1


	# xch exchange

	if binary_string.startswith("1011"):
		print("paskaaa")
		selectedregister = int(binary_string[4:], 2)
		print(selectedregister)
		paskat = registers[1]
		registers[1] = registers[selectedregister+generalregisterbase]
		registers[selectedregister+generalregisterbase] = paskat

		registers[0] = registers[0] + 1

	# bbl branch back and load (basically ret instruction)

	if binary_string.startswith("1100"):
		

		registers[0] = stack[stackpointer-1]
		print(str(registers[0]) + " !!!!!!!")

		stackpointer = stackpointer - 1


		registers[1] = int(binary_string[4:], 2)


	# ldm load immediate

	if binary_string.startswith("1101"):
		data = int(binary_string[4:], 2)

		registers[1] = data

		registers[0] = registers[0] + 1

	# wrm write to main memory

	if binary_string == "11100000":
		memory[registers[4]] = registers[1]
		registers[0] = registers[0] + 1

	# wmp write ram port

	if binary_string == "11100001":
		ramoutputports[selectedrammemorychip] = registers[1]

		registers[0] = registers[0] + 1

	# wrr write to rom port

	if binary_string == "11100010":

		romoutputports[selectedrommemorychip] = registers[1]
		registers[0] = registers[0] + 1

	# wr0 write status character 0

	if binary_string == "11100100":
		statuscharacters[selectedrammemorychip][selectedrammemoryregister][0] = registers[1]
		registers[0] = registers[0] + 1


	# wr1 write status character 1

	if binary_string == "11100101":
		statuscharacters[selectedrammemorychip][selectedrammemoryregister][1] = registers[1]
		registers[0] = registers[0] + 1

	# wr2 write status character 1

	if binary_string == "11100110":
		statuscharacters[selectedrammemorychip][selectedrammemoryregister][2] = registers[1]
		registers[0] = registers[0] + 1

	# wr3 write status character 1

	if binary_string == "11100111":
		statuscharacters[selectedrammemorychip][selectedrammemoryregister][3] = registers[1]
		registers[0] = registers[0] + 1




	# sbm subtract min memory

	if binary_string == "11101000":
		whattosubtract = memory[registers[4]]
		registers[1] = registers[1] - whattosubtract
		registers[0] = registers[0] + 1

	# rdm read main memory

	if binary_string == "11101001":
		registers[1] = memory[registers[4]]
		registers[0] = registers[0] + 1

	# rdr read rom port

	if binary_string == "11101010":
		registers[1] = romoutputports[selectedrommemorychip]
		registers[0] = registers[0] + 1

	# adm add main memory

	if binary_string == "11101011":
		registers[1] = registers[1] + memory[registers[4]]
		binarynumber = bin(registers[1], 2)
		binarynumber = binarynumber[2:]

		if len(binarynumber) > 4:
			binarynumber = binarynumber[-4:]
			registers[2] = 1

		registers[0] = registers[0] + 1




	# rd0 read status character 0

	if binary_string == "11101100":
		registers[1] = statuscharacters[selectedrammemorychip][selectedrammemoryregister][0]
		registers[0] = registers[0] + 1




	if binary_string == "11101101":
		print("jumped to the instruction ?????")
		print(selectedrammemorychip)
		print(selectedrammemoryregister)
		print(statuscharacters[selectedrammemorychip][selectedrammemoryregister][1])
		registers[1] = statuscharacters[selectedrammemorychip][selectedrammemoryregister][1]
		registers[0] = registers[0] + 1


	if binary_string == "11101110":
		
		registers[1] = statuscharacters[selectedrammemorychip][selectedrammemoryregister][2]
		registers[0] = registers[0] + 1




	if binary_string == "11101111":
		registers[1] = statuscharacters[selectedrammemorychip][selectedrammemoryregister][3]
		registers[0] = registers[0] + 1




	# clb clear both

	if binary_string == "11110000":
		registers[1] = 0
		registers[2] = 0
		registers[0] = registers[0] + 1

		
	# clc clear carry

	if binary_string == "11110001":
		registers[2] = 0
		registers[0] = registers[0] + 1

	# iac increment accumulator

	if binary_string == "11110010":
		registers[1] = registers[1] + 1

		if len(bin(registers[1])[2:]) > 4:
			registers[1] = bin(registers[1])[-4:]
			registers[2] = 1
		else:
			registers[2] = 0

		registers[0] = registers[0] + 1

	# cmc complement carry

	if binary_string == "11110011":
		if registers[2] == 1:
			registers[2] == 0
		elif registers[2] == 0:
			registers[2] = 1
		else:
			print("invalid value in carry/link register aka registers[2]")
		registers[0] = registers[0] + 1

	# cma complement

	if binary_string == "11110100":
		registers[1] = integernumber(registers[1], 4)
		registers[0] = registers[0] + 1


	# ral rotate left

	if binary_string == "11110101":
		numberarray = [0, 0, 0, 0, 0]

		accumulatornumber = bin(registers[1])[2:]
		accumulatornumber = "0"*(4-len(accumulatornumber)) + accumulatornumber
		print(accumulatornumber + " !!!!")
		accumulatornumber = list(accumulatornumber)

		numberarray[1] = accumulatornumber[0]
		numberarray[2] = accumulatornumber[1]
		numberarray[3] = accumulatornumber[2]
		numberarray[4] = accumulatornumber[3]

		numberarray[0] = registers[2]

		numberarray.append('0')

		numberarray = numberarray[1:]

		print(numberarray)


		binarynumber = ''.join(numberarray[1:])

		print(binarynumber)
		binarynumber = int(binarynumber, 2)

		print(binarynumber)

		registers[2] = int(numberarray[0])

		registers[1] = binarynumber

		registers[0] = registers[0] + 1

	# rar rotate right

	if binary_string == "11110110":
		numberarray = [0, 0, 0, 0, 0]

		accumulatornumber = bin(registers[1])[2:]
		accumulatornumber = "0"*(4-len(accumulatornumber)) + accumulatornumber
		print(accumulatornumber + " !!!!")
		accumulatornumber = list(accumulatornumber)

		numberarray[1] = accumulatornumber[0]
		numberarray[2] = accumulatornumber[1]
		numberarray[3] = accumulatornumber[2]
		numberarray[4] = accumulatornumber[3]

		numberarray[0] = registers[2]

		numberarray = ['0'] + numberarray



		numberarray.pop()

		numberarray[1] = str(numberarray[1])

		print(numberarray)


		registers[2] = int(numberarray[0])

		registers[1] = int(''.join(numberarray[1:]), 2)

		print(bin(registers[2]))

		print(registers[1])



		registers[0] = registers[0] + 1


	# tcc transfer carry and clear

	if binary_string == "11110111":
		registers[1] = 0
		registers[1] = registers[2]
		registers[2] = 0
		registers[0] = registers[0] + 1

	if binary_string == "11111000":
		registers[1] = registers[1] - 1
		registers[0] = registers[0] + 1

	# tcs transfer carry subtract

	if binary_string == "11111001":
		if registers[2] == 0:
			registers[1] = 9
		if registers[2] == 1:
			registers[1] = 10
		registers[2] = 0
		registers[0] = registers[0] + 1

	# stc set carry

	if binary_string == "11111010":
		registers[2] = 0
		registers[0] = registers[0] + 1















memory = [0] * 256
statuscharacters = [[[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]], [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]]
ramoutputports = [4*[0]]
romoutputports = [16*[0]]

selectedrammemoryregister = 0

romoutputport = 0

ramoutputport = 0
stackpointer = 0
stack = [0, 0, 0, "ignorethis"]

file = open("program.bin", "r")
print(((statuscharacters[0])[0])[1])

print(str(statuscharacters[0][0]) + " !!!!!!!!!!")
print(statuscharacters[0][0])
instructionarray = []

for line in file:
	instructionarray.append(line[:-1])
print(instructionarray)
for i in range(0, 260):
	instructionarray.append('00')
#print(instructionarray)


generalregisterbase = 5
registers = [0] * 21

selectedrammemorychip = 0
selectedrommemorychip = 0


print(str(registers) + " eeeeeeeeeeeeeee " + str(bin(registers[1])))
# eip = register 0
# accumulator = register 1
# carry/link = registers 2
# test signal = registers 3
# ram address register = register 4





while True:

	execinstruction(instructionarray[registers[0]])
	
	if registers[0] == 255:
		print("program stopped")
		print(statuscharacters)
		print(registers)
		break
	
	

'''





1111

0000


1111

1111

1111





111

001

110


111

110


 1101

1101



01
10

01
01

10
0

1







111


001



111


110


101

110














10110

11001

101111
010000

'''