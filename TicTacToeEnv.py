import gym
import numpy as np
import random

class TicTacToeEnv(gym.Env):
    
    def __init__(self):
        
        self.done = False
        self.observation = np.zeros([9, 1])
    
    def step(self, action):
        
        reward = 0
        self.observation[action, 0] = 1
        
        if self.observation[0, 0] == 1 and self.observation[1, 0] == 1 and self.observation[2, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[3, 0] == 1 and self.observation[4, 0] == 1 and self.observation[5, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[6, 0] == 1 and self.observation[7, 0] == 1 and self.observation[8, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[0, 0] == 1 and self.observation[3, 0] == 1 and self.observation[6, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[1, 0] == 1 and self.observation[4, 0] == 1 and self.observation[7, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[2, 0] == 1 and self.observation[5, 0] == 1 and self.observation[8, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[0, 0] == 1 and self.observation[4, 0] == 1 and self.observation[8, 0] == 1:
            self.done = True
            reward = 1
        if self.observation[2, 0] == 1 and self.observation[4, 0] == 1 and self.observation[6, 0] == 1:
            self.done = True
            reward = 1
        
        if reward != 1:
            if np.nonzero(self.observation==0)[0].shape[0] > 0:
                move = np.random.choice(np.nonzero(self.observation==0)[0])
                self.observation[move, 0] = -1
                print(f'Env: {move}')
        
            if self.observation[0, 0] == -1 and self.observation[1, 0] == -1 and self.observation[2, 0] == -1:
                self.done = True
                reward = -1
            if self.observation[3, 0] == -1 and self.observation[4, 0] == -1 and self.observation[5, 0] == -1:
                self.done = True
                reward = -1
            if self.observation[6, 0] == -1 and self.observation[7, 0] == -1 and self.observation[8, 0] == -1:
                self.done = True
                reward = -1
            if self.observation[0, 0] == -1 and self.observation[3, 0] == -1 and self.observation[6, 0] == -1:
                self.done = True
                reward = -1
            if self.observation[1, 0] == -1 and self.observation[4, 0] == -1 and self.observation[7, 0] == -1:
                self.done = True
                reward = -1
            if self.observation[2, 0] == -1 and self.observation[5, 0] == -1 and self.observation[8, 0] == -1:
                self.done = True
                reward = -1
            if self.observation[0, 0] == -1 and self.observation[4, 0] == -1 and self.observation[8, 0] == -1:
                self.done = True
                reward = -1
            if self.observation[2, 0] == -1 and self.observation[4, 0] == -1 and self.observation[6, 0] == -1:
                self.done = True
                reward = -1 
        if np.nonzero(self.observation==0)[0].shape[0] == 0:
            self.done = True
            
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
        
        