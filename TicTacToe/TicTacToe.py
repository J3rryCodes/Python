import numpy as np
import string
import random

class TicTacToe:

	moveCount = 0
	def __init__(self,size,noPlayer):
		self.size = size
		self.noPlayer = noPlayer
		self.bord = np.zeros((size,size), dtype=int)


	def gameManagerCPU(self):
		#First Turn Human
		while True:
			if self.moveCount % 2 == 0:
				self.humanMove()
			else:
				self.cpuMove()

	def cpuMove(self):
		x = random.randint(0, self.size-1)
		y = random.randint(0, self.size-1)

		self.move(x, y)

	def humanMove(self):
		flag = True
		x=y=0
		while flag:
			self.printBord()
			x = int(input("Enter X : "))
			y = int(input("Enter Y : "))
			if x<=self.size and y<=self.size:
				flag = False
		self.move(x-1, y-1)


	def move(self,x,y):
		#set not zero id for players
		if self.bord[x][y] != 0:
			return
		currentPlayer = self.moveCount%self.noPlayer
		if currentPlayer == 0:
			currentPlayer = self.noPlayer

		self.bord[x][y] = currentPlayer
		self.moveCount += 1

	def printBord(self):
		print('\x1bc')
		for i in range(0,self.size*2+6):
			print("_",end='')
		print() #New Line

		print(end="|   |")
		for i in range(0,self.size):
			print(i+1,end=" ")
		print(end="|")
		print() #New Line

		for i in range(0,self.size*2+6):
			print("-",end='')
		print() #New Line

		for i in range(0,self.size):
			print("|",i+1,"|",end="")
			for j in range(0,self.size):
				if self.bord[i][j] != 0:
					print(string.ascii_uppercase[self.bord[i][j]-1],end=" ")
				else:
					print(end="  ")
			print("|")

		for i in range(0,self.size*2+6):
			print("-",end='')
		print() #New Line


TicTacToe(8, 2).gameManagerCPU()