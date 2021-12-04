#!/usr/bin/env python

class BingoBoard:
	def __init__(self, boardLines):
		self.boardNumbers = []
		self.boardStatus = []

		for line in boardLines:
			self.boardNumbers.append(list(map(int, line.split())))
			self.boardStatus.append([False, False, False, False, False])

	def markNumber(self, number):
		for lineIndex in range(len(self.boardNumbers)):
			for numberIndex in range(len(self.boardNumbers[lineIndex])):
				if self.boardNumbers[lineIndex][numberIndex] == number:
					self.boardStatus[lineIndex][numberIndex] = True

	def calculateSum(self, winningNumber):
		unmarkedSum = 0
		for lineIndex in range(len(self.boardNumbers)):
			for numberIndex in range(len(self.boardNumbers[lineIndex])):
				if self.boardStatus[lineIndex][numberIndex] == False:
					unmarkedSum += self.boardNumbers[lineIndex][numberIndex]
		return unmarkedSum * winningNumber

	def checkWin(self):
		# Check if horizontal line is a win
		for lineIndex in range(len(self.boardStatus)):
			isLineWin = True
			for numberIndex in range(len(self.boardStatus[lineIndex])):
				isLineWin = self.boardStatus[lineIndex][numberIndex] and isLineWin == True
			if isLineWin == True:
				#print("\nHorizontal win")
				return True

		# Check if vertical line is a win
		for lineIndex in range(len(self.boardStatus)):
			isLineWin = True
			for numberIndex in range(len(self.boardStatus[lineIndex])):
				isLineWin = self.boardStatus[numberIndex][lineIndex] and isLineWin == True
			if isLineWin == True:
				#print("\nVertical win")
				return True
				
		# Check if diagonal line \ is a win
		isLineWin = True
		for lineIndex in range(len(self.boardStatus)):
			isLineWin = self.boardStatus[lineIndex][lineIndex] and isLineWin == True
		if isLineWin == True:
			#print("\nDiagonal \ win")
			return True

		# Check if diagonal line / is a win
		isLineWin = True
		for lineIndex in range(len(self.boardStatus)):
			isLineWin = self.boardStatus[lineIndex][4-lineIndex] and isLineWin == True
		if isLineWin == True:
			#print("\nDiagonal / win")
			return True

		return False

def partOne(bingoBoards, drawNumbers):
	for drawnNumber in drawNumbers:
		numberHasWins = False
		winnerSum = 0

		for bingoBoard in bingoBoards:
			bingoBoard.markNumber(drawnNumber)
			if bingoBoard.checkWin() == True:
				winnerSum = bingoBoard.calculateSum(drawnNumber)
				numberHasWins = True
		if numberHasWins == True:
			print("The winner board has a score of " + str(winnerSum))
			break

def partTwo(bingoBoards, drawNumbers):
	latestIndex = -1

	for bingoBoard in bingoBoards:
		for drawNumberIndex in range(len(drawNumbers)):
			bingoBoard.markNumber(drawNumbers[drawNumberIndex])
			if bingoBoard.checkWin() == True:
				if drawNumberIndex > latestIndex:
					latestIndex = drawNumberIndex
					latestSum = bingoBoard.calculateSum(drawNumbers[drawNumberIndex])
				break

	print("The final score will be " + str(latestSum))

if __name__ == "__main__":
	print("AdventOfCode - Day 4")
	print("********************")
	
	with open("input.txt") as f:
		lines = f.read().splitlines()
	
	drawNumbers = list(map(int, lines[0].split(",")))	

	bingoBoards = []
	for lineNr in range(2,len(lines),6):
		boardLines = []
		for boardLine in range(0,5):
			boardLines.append(lines[lineNr + boardLine])
		bingoBoards.append(BingoBoard(boardLines))

	print("\nPart one")
	print("========")
	partOne(bingoBoards, drawNumbers)
	
	print("\nPart two")
	print("========")
	partTwo(bingoBoards, drawNumbers)