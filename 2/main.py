#!/usr/bin/env python

def partOne(lines):
	horizontal = depth = 0
	for i in range(len(lines)):
		subStrings = lines[i].split()
		if(subStrings[0] == "forward"):
			horizontal += int(subStrings[1])
		elif(subStrings[0] == "down"):
			depth += int(subStrings[1])
		elif(subStrings[0] == "up"):
			depth -= int(subStrings[1])
			
	print("Horizontal: " + str(horizontal))
	print("Depth: " + str(depth))
	print("Multiplied: " + str(horizontal * depth))
	
def partTwo(lines):
	horizontal = depth = aim = 0
	for i in range(len(lines)):
		subStrings = lines[i].split()
		if(subStrings[0] == "forward"):
			horizontal += int(subStrings[1])
			depth += int(subStrings[1]) * aim
		elif(subStrings[0] == "down"):
			aim += int(subStrings[1])
		elif(subStrings[0] == "up"):
			aim -= int(subStrings[1])
			
	print("Horizontal: " + str(horizontal))
	print("Depth: " + str(depth))
	print("Multiplied: " + str(horizontal * depth))

if __name__ == "__main__":
	print("AdventOfCode - Day 2")
	print("********************")
	
	with open("input.txt") as f:
		lines = f.read().splitlines()
	
	print("\nPart one")
	print("========")
	partOne(lines)
	
	print("\nPart two")
	print("========")
	partTwo(lines)
	