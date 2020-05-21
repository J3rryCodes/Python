from tabulate import tabulate
import numpy as np

class TicTacToe:
	flag = {0:' ',1:'X',2:'O'}
	count = 0
	depth = 3
	def __init__(self,size,firestPlay):
		self.bord = np.zeros((size,size))
		self.size = size 
		if firestPlay:
			self.humanFlag = 1
			self.cpuFlag = 2
		else:
			self.humanFlag = 2
			self.cpuFlag = 1

	def displayBord(self):
		#print('\x1bc')
		#header = [i for i in range(0,10)]
		#bord = tabulate([[self.flag[i] for i in self.bord[j]] for j in range(0,self.size)])
		#print(tabulate(bord,header,tablefmt="grid",showindex="always"))
		print(self.bord)

	def setFlag(self,x,y,flag):
		if self.bord[x][y] != 0:
			return
		print("Flag",flag)
		self.bord[x][y] = flag

		#Adding count by one ----
		self.count += 1

	#Returns who won in digit
	def checkBord(self):
		c1Count = 0
		c2Count = 0

		c1Val = self.bord[0][0]
		c2Val = self.bord[0][self.size-1]
		for i in range(0,self.size):
			vCount = 0
			hCount = 0
			vVal = 0
			hVal = self.bord[i][0]
			for j in range(0,self.size):
				#no need to check but atleast its help run faster 
				if self.bord[j][i] != 0:
					if j == 0:
						vVal = self.bord[0][i]
					#Vertical check
					if vVal == self.bord[j][i]:
						vCount+=1
					if vCount == self.size:
						return vVal
				#no need to check but atleast its help run faster 
				if self.bord[i][j] != 0:
					#Horizontal check
					if hVal == self.bord[i][j]:
						hCount += 1
					if hCount == self.size:
						return hVal
				#cross R -> L
				if i==j and self.bord[i][j] == c1Val:
					c1Count += 1
					if c1Count == self.size:
						return c1Val
				#Cross L -> R
				if i+j == self.size-1 and self.bord[i][j] == c2Val:
					c2Count+=1
					if c2Count == self.size:
						return c2Val
		return 0


	def gameManager(self):
		while True :
			if (self.count%2)+1 == self.humanFlag:
				self.humanMove()
			else:
				self.cpuMove()

	def humanMove(self):
		print("HUMAN")
		self.displayBord()
		x = int(input("X : "))
		y = int(input("Y : "))

		if x>self.size-1 or y>self.size-1:
			return
		self.setFlag(x, y, self.humanFlag)
		if self.checkBord() == self.humanFlag:
			print("Won HUMAN")
			exit()

	def cpuMove(self):
		#Forcing to set flag in center
		if self.count < 2 and self.size%2 != 0:
			mid = int((self.size-1)/2)
			if self.bord[mid][mid] == 0:
				self.setFlag(mid, mid, self.cpuFlag)
				return
		bestScore = -100
		bestPos = (0,0)
		for i in range(0,self.size):
			for j in range(0,self.size):
				if self.bord[i][j] == 0:
					self.bord[i][j] = self.cpuFlag
					if self.checkBord() == self.cpuFlag:
						#CPU Won!
						self.setFlag(i, j, self.cpuFlag)
						return
					else:
						score = self.minimax(self.depth,False)
					self.bord[i][j] = 0
					#Maximizing
					if bestScore < score:
						bestScore = score
						bestPos = (i,j)
		self.setFlag(bestPos[0], bestPos[1], self.cpuFlag)

		if self.checkBord() == self.cpuFlag:
			print("Won CPU")
			exit()

	def minimax(self,depth,isMax):
		if depth == 0:
			return 0
		bestScore = 100
		if isMax:
			bestScore = -100
		for i in range(0,self.size):
			for j in range(0,self.size):
				if self.bord[i][j] == 0:
					#Maximizing player
					if isMax:
						self.bord[i][j] = self.cpuFlag
						if self.checkBord() == self.cpuFlag:
							score = 1
						else:
							score = self.minimax(depth-1, not isMax)
						self.bord[i][j] = 0
						bestScore = max(score, bestScore)
					#Minimizing Player
					else:
						self.bord[i][j] = self.humanFlag
						if self.checkBord() == self.humanFlag:
							score = -1
						else:
							score = self.minimax(depth-1, not isMax)
						self.bord[i][j] = 0
						bestScore = min(score, bestScore)
		return bestScore


TicTacToe(3, False).gameManager()