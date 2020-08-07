import gym
import numpy as np
import random

class TicTacToeEnv(gym.Env):
    
    def __init__(self):
        
        self.done = False
        self.observation = np.zeros([9, 1])
    
    def step(self, action):
        
        self.observation[action-1, 0] = 1
        reward = 0
        
        while True:
            
            move = random.randint(0, 8)
            
            if self.observation[move, 0] == 0:
                
                self.observation[move, 0] = -1
                
                break
            
        if self.observation[0, 0] == -1 and self.observation[1, 0] == -1 and self.observation[2, 0] and -1:
            self.done = True
            reward = -1
        if self.observation[3, 0] == -1 and self.observation[4, 0] == -1 and self.observation[5, 0] and -1:
            self.done = True
            reward = -1
        if self.observation[6, 0] == -1 and self.observation[7, 0] == -1 and self.observation[8, 0] and -1:
            self.done = True
            reward = -1
        if self.observation[0, 0] == -1 and self.observation[3, 0] == -1 and self.observation[6, 0] and -1:
            self.done = True
            reward = -1
        if self.observation[1, 0] == -1 and self.observation[4, 0] == -1 and self.observation[7, 0] and -1:
            self.done = True
            reward = -1
        if self.observation[2, 0] == -1 and self.observation[5, 0] == -1 and self.observation[8, 0] and -1:
            self.done = True
            reward = -1
        if self.observation[0, 0] == -1 and self.observation[4, 0] == -1 and self.observation[8, 0] and -1:
            self.done = True
            reward = -1
        if self.observation[2, 0] == -1 and self.observation[4, 0] == -1 and self.observation[6, 0] and -1:
            self.done = True
            reward = -1 
        
        if self.observation[0, 0] == 1 and self.observation[1, 0] == 1 and self.observation[2, 0] and 1:
            self.done = True
            reward = 1
        if self.observation[3, 0] == 1 and self.observation[4, 0] == 1 and self.observation[5, 0] and 1:
            self.done = True
            reward = 1
        if self.observation[6, 0] == 1 and self.observation[7, 0] == 1 and self.observation[8, 0] and 1:
            self.done = True
            reward = 1
        if self.observation[0, 0] == 1 and self.observation[3, 0] == 1 and self.observation[6, 0] and 1:
            self.done = True
            reward = 1
        if self.observation[1, 0] == 1 and self.observation[4, 0] == 1 and self.observation[7, 0] and 1:
            self.done = True
            reward = 1
        if self.observation[2, 0] == 1 and self.observation[5, 0] == 1 and self.observation[8, 0] and 1:
            self.done = True
            reward = 1
        if self.observation[0, 0] == 1 and self.observation[4, 0] == 1 and self.observation[8, 0] and 1:
            self.done = True
            reward = 1
        if self.observation[2, 0] == 1 and self.observation[4, 0] == 1 and self.observation[6, 0] and 1:
            self.done = True
            reward = 1
            
        return self.observation, reward, self.done
        
    def reset(self):
        
        self.done = False
        self.observation = np.zeros([9, 1])
        
        return self.observation
        
    def render(self):
        
        def letter(number):
        
            if number == 0:
                mark = " "
            elif number < 0:
                    mark = "O"
            elif number > 0:
                    mark = "X"
                
            return mark
        
        print(f'   |   |   ')
        print(f' {letter(self.observation[0, 0])} | {letter(self.observation[1, 0])} | {letter(self.observation[2, 0])} ')
        print(f'___|___|___')
        print(f'   |   |   ')
        print(f' {letter(self.observation[3, 0])} | {letter(self.observation[4, 0])} | {letter(self.observation[5, 0])} ')
        print(f'___|___|___')
        print(f'   |   |   ')
        print(f' {letter(self.observation[6, 0])} | {letter(self.observation[7, 0])} | {letter(self.observation[8, 0])} ')
        print(f'   |   |   \n')
        
        
