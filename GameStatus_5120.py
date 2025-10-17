# -*- coding: utf-8 -*-
import numpy as np

class GameStatus:

	def __init__(self, board_state, turn_O):
		self.board_state = board_state
		self.turn_O = turn_O
		self.oldScores = 0
		self.winner = ""

	def is_terminal(self):
		#not terminal if empty cells remain
		if (self.board_state == 0).any():
			return False
		
		#board is full : decide winner by final triplet differnce
		score = self.get_scores(terminal=True)
		if score > 0:
			self.winner = "O"
		elif score < 0:
			self.winner = "X"
		else:
			self.winner = "Draw"
		return True

	def get_scores(self, terminal):
		"""
		YOUR CODE HERE TO CALCULATE THE SCORES. MAKE SURE YOU ADD THE SCORE FOR EACH PLAYER BY CHECKING 
		EACH TRIPLET IN THE BOARD IN EACH DIRECTION (HORIZONAL, VERTICAL, AND ANY DIAGONAL DIRECTION)
		
		YOU SHOULD THEN RETURN THE CALCULATED SCORE WHICH CAN BE POSITIVE (HUMAN PLAYER WINS),
		NEGATIVE (AI PLAYER WINS), OR 0 (DRAW)
		
		"""
		
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2

		#horizontal windows
		for r in range(rows): #r = rows
			for c in range(cols-2): #c=cols
				w = self.board_state[r, c:c+3]
				o = (w==1).sum()
				x = (w==-1).sum()
				z = ( w== 0).sum()
				if check_point == 3:
					if o ==3: scores += 1
					elif x ==3: scores -= 1
				else:
					if o ==2 and z==1 and x==0: scores += 1
					elif x == 2 and z ==1 and o ==0: scores -= 1

				
		#vertical windows
		for r in range(rows-2):
			for c in range(cols):
				w = self.board_state[r: r+3,c]
				o = (w ==1).sum()
				x = (w== -1).sum()
				z = (w== 0).sum()
				if check_point==3:
					if o == 3: scores += 1
					elif x ==3: scores -= 1
				else:
					if o ==2 and z ==1 and x==0: scores +=1
					elif x==2 and z==1 and o == 0: scores -= 1


		#diagonal (\)down, right
		for r in range(rows -2):
			for c in range(cols -2):
				w = [self.board_state[r+i, c+i] for i in range(3)]
				o = sum(v==1 for v in w)
				x = sum(v==-1 for v in w)
				z = sum(v==0 for v in w)
				if check_point ==3:
					if o ==3: scores +=1
					elif x==3: scores -=1
				else:
					if o == 2 and z ==1 and x == 0: scores += 1
					elif x==2 and z ==1 and o ==0: scores -=1 

		#diagonality (/) up, right
		for r in range(2, rows):
			for c in range (cols - 2):
				w = [self.board_state[r-i,c+i] for i in range(3)]
				o = sum(v ==1 for v in w)
				x = sum(v==-1 for v in w)
				z = sum(v ==0 for v in w)
				if check_point ==3:
					if o ==3: scores += 1
					elif x==3: scores -= 1
				else:
					if o ==2 and z ==1 and x ==0: scores +=1
					elif x==2 and z == 1 and o ==0: scores-=1


		return scores

	def get_negamax_scores(self, terminal):
		"""
		YOUR CODE HERE TO CALCULATE NEGAMAX SCORES. THIS FUNCTION SHOULD EXACTLY BE THE SAME OF GET_SCORES UNLESS
		YOU SET THE SCORE FOR NEGAMX TO A VALUE THAT IS NOT AN INCREMENT OF 1 (E.G., YOU CAN DO SCORES = SCORES + 100 
																			   FOR HUMAN PLAYER INSTEAD OF 
																			   SCORES = SCORES + 1)
		"""
		rows = len(self.board_state)
		cols = len(self.board_state[0])
		scores = 0
		check_point = 3 if terminal else 2

		#horizontal windows
		for r in range(rows):
			for c in range(cols-2):
				w = self.board_state[r, c:c+3]
				o = (w==1).sum()
				x = (w==-1).sum()
				z = ( w== 0).sum()
				if check_point == 3:
					if o ==3: scores += 1
					elif x ==3: scores -= 1
				else:
					if o ==2 and z==1 and x==0: scores += 1
					elif x == 2 and z ==1 and o ==0: scores -= 1

				
		#vertical windows
		for r in range(rows-2):
			for c in range(cols):
				w = self.board_state[r: r+3, c]
				o = (w ==1).sum()
				x = (w== -1).sum()
				z = (w== 0).sum()
				if check_point==3:
					if o == 3: scores += 1
					elif x ==3: scores -= 1
				else:
					if o ==2 and z ==1 and x==0: scores +=1
					elif x==2 and z==1 and o == 0: scores -= 1


		#diagonal (\)down, right
		for r in range(rows -2):
			for c in range(cols -2):
				w = [self.board_state[r+i, c+i] for i in range(3)]
				o = sum(v==1 for v in w)
				x = sum(v==-1 for v in w)
				z = sum(v==0 for v in w)
				if check_point ==3:
					if o ==3: scores +=1
					elif x==3: scores -=1
				else:
					if o == 2 and z ==1 and x == 0: scores += 1
					elif x==2 and z ==1 and o ==0: scores -=1 

		#diagonality (/) up, right
		for r in range(2, rows):
			for c in range (cols -2):
				w = [self.board_state[r-i,c+i] for i in range(3)]
				o = sum(v ==1 for v in w)
				x = sum(v==-1 for v in w)
				z = sum(v ==0 for v in w)
				if check_point ==3:
					if o ==3: scores += 1
					elif x==3: scores -= 1
				else:
					if o ==2 and z ==1 and x ==0: scores +=1
					elif x==2 and z == 1 and o ==0: scores-=1

		return scores

		

	def get_moves(self):
		moves = []
		state = self.board_state
		state_rows, state_cols = state.shape
		for r in range(state_rows):
			for c in range(state_cols):
				if state[r, c] == 0: # this is a legal move = empty cell
					moves.append((r, c))
		return moves

	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[x, y] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)
