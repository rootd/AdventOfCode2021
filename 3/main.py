#!/usr/bin/env python

def partOne(lines,bitsPerLine):
	# Build bitlist
	bitList = []
	for lineNo in range(len(lines)):
		bitList.append([0] * bitsPerLine)
		for bit in range(len(lines[lineNo])):
			bitList[lineNo][bit] = int(lines[lineNo][bit])

	# Count zeros and ones
	zeroCounter = [0] * bitsPerLine
	oneCounter = [0] * bitsPerLine
	for element in bitList:
		for bitNo in range(len(element)):
			oneCounter[bitNo] += 1 if (element[bitNo] == 1) else 0
			zeroCounter[bitNo] += 1 if (element[bitNo] == 0) else 0
	
	# Compare counted zeros and ones
	gammaRate = ""
	epsilonRate = ""
	for pos in range(bitsPerLine):
		gammaRate = gammaRate + ("1" if (oneCounter[pos] > zeroCounter[pos]) else "0")
		epsilonRate = epsilonRate + ("1" if (oneCounter[pos] < zeroCounter[pos]) else "0")
	gammaRate = int(gammaRate, 2)
	epsilonRate = int(epsilonRate, 2)
	
	print("Gamma rate: " + str(gammaRate))
	print("Epsilon rate: " + str(epsilonRate))
	print("Power consumption: " + str(gammaRate * epsilonRate))
	
def partTwo(lines,bitsPerLine):
	# Build bitlist
	bitList = []
	for lineNo in range(len(lines)):
		bitList.append([0] * bitsPerLine)
		for bit in range(len(lines[lineNo])):
			bitList[lineNo][bit] = int(lines[lineNo][bit])
	
	oxygenList = bitList.copy()
	for pos in range(bitsPerLine):
		# Count zeros and ones
		zeroCounter = [0] * bitsPerLine
		oneCounter = [0] * bitsPerLine
		for element in oxygenList:
			for bitNo in range(len(element)):
				oneCounter[bitNo] += 1 if (element[bitNo] == 1) else 0
				zeroCounter[bitNo] += 1 if (element[bitNo] == 0) else 0
		
		if(oneCounter[pos] >= zeroCounter[pos]):
			oxygenList = [line for line in oxygenList if line[pos]==1]
		else:
			oxygenList = [line for line in oxygenList if line[pos]==0]
			
		if(len(oxygenList) == 1):
			break
			
	C02list = bitList.copy()
	for pos in range(bitsPerLine):
		# Count zeros and ones
		zeroCounter = [0] * bitsPerLine
		oneCounter = [0] * bitsPerLine
		for element in C02list:
			for bitNo in range(len(element)):
				oneCounter[bitNo] += 1 if (element[bitNo] == 1) else 0
				zeroCounter[bitNo] += 1 if (element[bitNo] == 0) else 0
		
		if(oneCounter[pos] < zeroCounter[pos]):
			C02list = [line for line in C02list if line[pos]==1]
		else:
			C02list = [line for line in C02list if line[pos]==0]
			
		if(len(C02list) == 1):
			break
			
	oxygenRate = ""
	CO2Rate = ""
	for pos in range(len(oxygenList[0])):
		oxygenRate = oxygenRate + str(oxygenList[0][pos])
	for pos in range(len(C02list[0])):
		CO2Rate = CO2Rate + str(C02list[0][pos])
	
	oxygenRate = int(oxygenRate, 2)
	CO2Rate = int(CO2Rate, 2)
	
	print("Oxygen generator rating rate: " + str(oxygenRate))
	print("CO2 scrubber rating: " + str(CO2Rate))
	print("Life support rating: " + str(oxygenRate * CO2Rate))
	
if __name__ == "__main__":
	print("AdventOfCode - Day 3")
	print("********************")
	
	with open("input.txt") as f:
		lines = f.read().splitlines()
	bitsPerLine = len(lines[0])
	
	print("\nPart one")
	print("========")
	partOne(lines,bitsPerLine)
	
	print("\nPart two")
	print("========")
	partTwo(lines,bitsPerLine)