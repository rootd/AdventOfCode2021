#!/usr/bin/env python

import copy

class Crab:
	def __init__(self, crabPosition):
		self.crabPosition = crabPosition

	def moveToPositionConstantFuel(self, position):
		self.fuel = abs(self.crabPosition - position)
		self.crabPosition = position

	def moveToPositionRisingFuel(self, position):
		self.fuel = sum(range(abs(self.crabPosition - position) + 1))
		self.crabPosition = position

def partOne(crabs):
	fuels = []
	for position in range(min(crabs, key=lambda item: item.crabPosition).crabPosition,max(crabs, key=lambda item: item.crabPosition).crabPosition + 1):
		crabsTemp = copy.deepcopy(crabs)
		fuelSums = 0
		for crab in crabsTemp:
			crab.moveToPositionConstantFuel(position)
			fuelSums += crab.fuel
		fuels.append((position, fuelSums))

	fuelMin = min(fuels, key = lambda i : i[1])[1]
	print("The crabs must spend at minimum " + str(fuelMin) + " of fuel to align.")

def partTwo(crabs):
	fuels = []
	for position in range(min(crabs, key=lambda item: item.crabPosition).crabPosition,max(crabs, key=lambda item: item.crabPosition).crabPosition + 1):
		crabsTemp = copy.deepcopy(crabs)
		fuelSums = 0
		for crab in crabsTemp:
			crab.moveToPositionRisingFuel(position)
			fuelSums += crab.fuel
		fuels.append((position, fuelSums))

	fuelMin = min(fuels, key = lambda i : i[1])[1]
	print("The crabs must spend at minimum " + str(fuelMin) + " of fuel to align.")

if __name__ == "__main__":
	print("AdventOfCode - Day 6")
	print("********************")
	
	with open("input.txt") as f:
		crabsPositions = map(int, f.read().split(","))
		crabs = []
		for crabPosition in crabsPositions:
			crabs.append(Crab(crabPosition))

	print("\nPart one")
	print("========")
	partOne(copy.deepcopy(crabs))
	
	print("\nPart two")
	print("========")
	partTwo(copy.deepcopy(crabs))