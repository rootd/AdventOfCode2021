#!/usr/bin/env python
import re
import copy

regex = r"(\d+),(\d+)\s->\s(\d+),(\d+)"

class HydrothermalVent:
	def __init__(self, match):
		self.x1 = int(match.group(1))
		self.y1 = int(match.group(2))
		self.x2 = int(match.group(3))
		self.y2 = int(match.group(4))

def partOne(hydrothermalVents, oceanFloor):
	for hydrothermalVent in hydrothermalVents:
		isHorizonal = (hydrothermalVent.x1 == hydrothermalVent.x2) and (hydrothermalVent.y1 != hydrothermalVent.y2)
		isVertical = (hydrothermalVent.y1 == hydrothermalVent.y2) and (hydrothermalVent.x1 != hydrothermalVent.x2)
		if isHorizonal or isVertical:
			for coordX in range(min(hydrothermalVent.x1, hydrothermalVent.x2), max(hydrothermalVent.x1, hydrothermalVent.x2)+1):
				for coordY in range(min(hydrothermalVent.y1, hydrothermalVent.y2), max(hydrothermalVent.y1, hydrothermalVent.y2)+1):
					oceanFloor[coordX][coordY] += 1

	twoOrMoreLines = 0
	for coordX in range(len(oceanFloor)):
		for coordY in range(len(oceanFloor[coordX])):
			if oceanFloor[coordX][coordY] >= 2:
				twoOrMoreLines += 1
	
	print("At least two lines overlap at " + str(twoOrMoreLines) + " points.")

def partTwo(hydrothermalVents, oceanFloor):
	for hydrothermalVent in hydrothermalVents:
		isHorizonal = (hydrothermalVent.x1 == hydrothermalVent.x2) and (hydrothermalVent.y1 != hydrothermalVent.y2)
		isVertical = (hydrothermalVent.y1 == hydrothermalVent.y2) and (hydrothermalVent.x1 != hydrothermalVent.x2)
		isDiagonal = abs(hydrothermalVent.x1-hydrothermalVent.x2) == abs(hydrothermalVent.y1-hydrothermalVent.y2)

		if isHorizonal or isVertical:
			for coordX in range(min(hydrothermalVent.x1, hydrothermalVent.x2), max(hydrothermalVent.x1, hydrothermalVent.x2)+1):
				for coordY in range(min(hydrothermalVent.y1, hydrothermalVent.y2), max(hydrothermalVent.y1, hydrothermalVent.y2)+1):
					oceanFloor[coordX][coordY] += 1
		elif isDiagonal:
			if (hydrothermalVent.x1 < hydrothermalVent.x2 and hydrothermalVent.y1 < hydrothermalVent.y2):
				# (x1,y1) \
				#          \
				#           \ (x2,y2)
				for coordX in range(hydrothermalVent.x1, hydrothermalVent.x2+1):
					oceanFloor[coordX][hydrothermalVent.y1 + (coordX - hydrothermalVent.x1)] += 1
			elif (hydrothermalVent.x1 > hydrothermalVent.x2 and hydrothermalVent.y1 > hydrothermalVent.y2):
				# (x2,y2) \
				#          \
				#           \ (x1,y1)
				for coordX in range(hydrothermalVent.x2, hydrothermalVent.x1+1):
					oceanFloor[coordX][hydrothermalVent.y2 + (coordX - hydrothermalVent.x2)] += 1
			elif (hydrothermalVent.x1 > hydrothermalVent.x2 and hydrothermalVent.y1 < hydrothermalVent.y2):
				#           / (x1,y1)
				#          /
				# (x2,y2) /
				for coordX in range(hydrothermalVent.x2, hydrothermalVent.x1+1):
					oceanFloor[coordX][hydrothermalVent.y2 - (coordX - hydrothermalVent.x2)] += 1
			elif (hydrothermalVent.x2 > hydrothermalVent.x1 and hydrothermalVent.y1 > hydrothermalVent.y2):
				#           / (x2,y2)
				#          /
				# (x1,y1) /
				for coordX in range(hydrothermalVent.x1, hydrothermalVent.x2+1):
					oceanFloor[coordX][hydrothermalVent.y1 - (coordX - hydrothermalVent.x1)] += 1
			
	twoOrMoreLines = 0
	for coordX in range(len(oceanFloor)):
		for coordY in range(len(oceanFloor[coordX])):
			if oceanFloor[coordX][coordY] >= 2:
				twoOrMoreLines += 1
	
	print("At least two lines overlap at " + str(twoOrMoreLines) + " points.")

if __name__ == "__main__":
	print("AdventOfCode - Day 5")
	print("********************")
	
	with open("input.txt") as f:
		lines = f.read().splitlines()

	hydrothermalVents = []
	for line in lines:
		hydrothermalVents.append(HydrothermalVent(re.match(regex, line)))

	maxX = max(max(hydrothermalVents, key=lambda item: item.x1).x1, max(hydrothermalVents, key=lambda item: item.x2).x2) + 1
	maxY = max(max(hydrothermalVents, key=lambda item: item.y1).y1, max(hydrothermalVents, key=lambda item: item.y2).y2) + 1
	oceanFloor = [[0] * maxY for i in range(maxX+1)]

	print("\nPart one")
	print("========")
	partOne(hydrothermalVents, copy.deepcopy(oceanFloor))
	
	print("\nPart two")
	print("========")
	partTwo(hydrothermalVents, copy.deepcopy(oceanFloor))