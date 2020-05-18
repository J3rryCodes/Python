import numpy as np
import string
import random

class TicTacToe:

	playerFlag = 0
	moveCount = 0
	def __init__(self,size,noPlayer):
		self.size = size
		self.noPlayer = noPlayer
		self.bord = np.zeros((size,size), dtype=int)

	def checkWon(self):
		flag = self.checkBord()
		if flag == 0:
			return 0
		elif flag == self.playerFlag:
			return 1
		else:
			return -1
	def checkBord(self):
		cross01 = 0
		cross02 = 0
		h=0
		v=0
		temp1 = -100
		temp2 = -100
		for i in range(0,self.size):
			v = 0
			h = 0
			temp4 = -100
			temp3 = -100
			for j in range(0,self.size):
				if self.bord[i][j] != 0:
					#Horizontal check
					if self.bord[i][j] != temp4:
						temp4 = self.bord[i][j]
						h = 1
					else:
						h += 1
					#Vertical check
					if self.bord[j][i] != temp3:
						temp3 = self.bord[j][i]
						v = 1
					else:
						v += 1
					#Cross Check01
					if i == j:
						if self.bord[j][i] != temp2:
							temp2 = self.bord[i][j]
							cross02 = 1
						else:
							cross02+=1
					if i+j == self.size-1:
						if self.bord[j][i] != temp1:
							temp1 = self.bord[i][j]
							cross01 = 1
						else:
							cross02+=1
			#Check won H&V
			if h == self.size:
				return temp4
			if v == self.size:
				return temp3
		if cross01 == self.size:
			return temp1
		if cross02 == self.size:
			return temp2
		return 0


	def gameManagerCPU(self):
		
		while True:
			if self.moveCount % 2 == 0:
				self.playerFlag = self.getCurrentPlayer()
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

	def getCurrentPlayer(self):
		currentPlayer = self.moveCount%self.noPlayer
		if currentPlayer == 0:
			currentPlayer = self.noPlayer
		return currentPlayer
	def move(self,x,y):
		#set not zero id for players
		if self.bord[x][y] != 0:
			return
		self.bord[x][y] = self.getCurrentPlayer()
		self.moveCount += 1


		tempResult = self.checkWon()
		if tempResult != 0:
			if tempResult > 0:
				self.printBord()
				print(f'You won !')
			else:
				self.printBord()
				print(f'You Lose !')
			exit()

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


TicTacToe(3, 2).gameManagerCPU()