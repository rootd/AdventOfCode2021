#!/usr/bin/env python

def partOne(lines):
	amountBigger = 0
	
	for i in range(len(lines)-1):
		amountBigger += 1 if lines[i+1] > lines[i] else 0

	print(str(amountBigger) + " measurements are larger than the previous measurement.")
	
def partTwo(lines):
	avg = []
	amountBigger = 0

	for i in range(len(lines)-2):
		avg.append(sum(lines[i:i+3])/3)
	
	for i in range(len(avg)-1):
		amountBigger += 1 if avg[i+1] > avg[i] else 0

	print(str(amountBigger) + " sums are larger than the previous sum.")

if __name__ == "__main__":
	print("AdventOfCode - Day 1")
	print("********************")

	with open("input.txt") as f:
		lines = [int(i) for i in f.read().splitlines()]

	print("\nPart one")
	print("========")
	partOne(lines)

	print("\nPart two")
	print("========")
	partTwo(lines)