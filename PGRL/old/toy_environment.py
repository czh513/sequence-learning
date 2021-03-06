#!/usr/bin/python
import numpy as np


class simple_maze():
	def __init__(self, state_dim, start, goal, pits, action_space): 
		self.state_dim = state_dim
		self.rows = state_dim[0]
		self.columns = state_dim[1]
		self.pits = pits
		self.start = start
		self.next_state = []
		self.goal = goal
		self.action_space = action_space
		self.state = start

	def take_action(self, action):
		self.done = 0 
		s = self.state
		if action == 0: # down
			self.state = [self.state[0] + 1, self.state[1]]
		if action == 1: # up
			self.state = [self.state[0] - 1, self.state[1]] 
		if action == 2: # left
			self.state = [self.state[0], self.state[1] - 1]
		if action == 3: # right
			self.state = [self.state[0], self.state[1] + 1]  
	
		if self.state[0] < 0 or self.state[1] < 0 or self.state[0] >= self.columns or self.state[1] >= self.rows: 
			self.state = s

		self.reward = 0
		if self.state[0] == self.goal[0] and self.state[1] == self.goal[1]: 
			self.reward = 1
			self.done = 1
		elif self.state in self.pits:
			self.reward = -1
			self.done = 1
		
		return self.state, self.reward, self.done

	def print_maze(self, vis=1): 
		M = np.chararray((self.rows, self.columns))
		M[:] = '-'
		M[self.start[0]][self.start[1]] = 'S'
		M[self.goal[0]][self.goal[1]] = 'G'
		M[self.state[0]][self.state[1]] = '*'
		for p in self.pits: 
			M[p[0], p[1]] = 'X'
		if vis:	
			print M
