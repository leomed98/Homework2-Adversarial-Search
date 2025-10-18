# -*- coding: utf-8 -*-


class GameStatus:

	def __init__(self, board_state, turn_O):
		self.board_state = board_state
		self.turn_O = turn_O
		self.oldScores = 0
		self.winner = ""

	def is_terminal(self):
		if (self.board_state == 0).any():
			return False
		
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
		return scores

	def get_moves(self):
		moves = []
		state = self.board_states
		state_rows, state_cols = state.shape
		for rows in range(state_rows):
			for cols in range(state_cols):
				if state[rows, cols] == 0: # this is a legal move = enpty cell
					moves.append((rows, cols))
		return moves

	def get_new_state(self, move):
		new_board_state = self.board_state.copy()
		x, y = move[0], move[1]
		new_board_state[x, y] = 1 if self.turn_O else -1
		return GameStatus(new_board_state, not self.turn_O)
