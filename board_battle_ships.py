# -*- coding: utf-8 -*-
"""
Created on Wed Dec 13 11:50:28 2017

@author: ucapy

Class Board
"""
class Board(object):
    
    
    def __init__(self, num_x, num_y):
        self.num_x = num_x
        self.num_y = num_y
        global board_list
        board_list =[]
        
    def set_board_size(self):
        self.num_x = input("Please enter the number of X boxes you would like: ")
        self.num_x = int(self.num_x)
        while self.num_x < 4:
            print("Min board size is 3x3")
            self.num_x = input("Please choose board size wisely: ")
            self.num_x = int(self.num_x)
        while self.num_x > 10:
            print("Max board size is 10x10")
            self.num_x = input("Please chose board size more wisely: ")
            self.num_x = int(self.num_x)
        
            
        self.num_y = input("Please enter the number of Y boxes you would like: ")
        self.num_y = int(self.num_y)
        while self.num_y < 4:
            print("Min board size is 3x3")
            self.num_y = input("Please choose board size wisely: ")
            self.num_y = int(self.num_y)
        while self.num_y > 10:
            print("Max board size is 10x10")
            self.num_y = input("Please chose board size more wisely: ")
            self.num_y = int(self.num_y)


        for i in range(1, self.num_x + 1):
            board_list.append(["O"] * int(self.num_y))
            
    def __getitem__(self, key):
        return board_list[key]

    def print_board(self):
       for i in board_list:
           print (i)
    
    def create_board(self):
        self.set_board_size()
        self.print_board()
    

      
