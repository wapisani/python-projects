#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 00:23:19 2020

@author: wapisani

This script will allow the user to rank their played video games in a 
similar manner as my "My Favorite Game Sorter". It will import a CSV file
with the games in the first column and the year of release in North America
in the second column.

Eventually the user will be able to rank games within a date range.
"""

# Import necessary libraries
import csv
import os
import random

# Define any functions here
def column(matrix, i):
    return [row[i] for row in matrix]

# It'd probably be more user-friendly to have command-line arguments
directory = "/home/wapisani/Documents/Programming/python-projects/Video_Game_Ranker"
os.chdir(directory)
filename = "Will_Pisani_List_of_Played_Video_Games.csv"

with open(filename,'r') as csvfile:
    reader = csv.reader(csvfile)
    game_year_list = list(reader)[1:]
    

# Get a list sorted by year
game_year_chrono_list = sorted(game_year_list, key=lambda x: x[1])


# Define minimum year and max year
min_year = 2000
max_year = 2010

# Define game list of games between the chosen years
game_year_daterange_list = []

# Iterate over chronological list and get sublist of specified date range
for game,year in game_year_chrono_list:
    year = int(year)
    
    if year >= min_year and year <= max_year:
        game_year_daterange_list.append([game,str(year)])
    
# Start ranking logic, maybe present them both in an ASCII interface
# similar to the online ranker and then have the user choose.
# The one chosen will have its value incremented by one
    
ranked_game_list = []
ranked_game_values = []
game1 = len(game_year_list) - 1
game2 = len(game_year_list) - 2

break_outer_loop = False

# Start iterating over games
for i in range(1,len(game_year_list)):
    for j in range(1,len(game_year_list)):
        game1_print = game_year_list[game1][0]
        game2_print = game_year_list[game2][0]
        print("\n-------------------------------\n")
        print(f"Battle No. {i*j}")
        print(f"For game 1: {game1_print}\nType 1 and press ENTER if you like this game better\n")
        print(f"For game 2: {game2_print}\nType 2 and press ENTER if you like this game better\n")
        print(f"For neither: Press ENTER if you like them equally\n")
        
        # Input validation
        input_value = input("Which do you like better? ")
        try:
            input_value = int(input_value)
        except ValueError:
            input_value = ''
                
        
        # Add both games to ranked game list, but change the value
        # according to what the user chose
        
        if game1_print in ranked_game_list:
            index = ranked_game_list.index(game1_print)
           
            if input_value == 1:
                ranked_game_values[index] += 1
        else:
            ranked_game_list.append(game1_print)
            if input_value == 1:
                ranked_game_values.append(1)
            else:
                ranked_game_values.append(0)
                
        if game2_print in ranked_game_list:
            index = ranked_game_list.index(game2_print)
            
            if input_value == 2:
                ranked_game_values[index] += 1
        else:
            ranked_game_list.append(game2_print)
            if input_value == 2:
                ranked_game_values.append(1)
            else:
                ranked_game_values.append(0)
                
        
        # Check the length of ranked_game_list
        # If it's the same length as the 
        rank_game_len = len(ranked_game_list)
        game_year_len = len(game_year_list)
        
        if rank_game_len == game_year_len:
            # Once the lists are the same length, set the game
            # indices to random values
            game1 = random.randint(0,len(game_year_list)-1)
            game2 = random.randint(0,len(game_year_list)-1)
            
            # If the loop has gotten to i > 3
            if i > 1 and i < 4:
                # Get all indices that have a value of zero
                zero_indices = []
                for index,value in enumerate(ranked_game_values):
                    if value == 0:
                        zero_indices.append(index)
                if len(zero_indices) > 1:
                    # Grab two indices at random
                    zero_index_len = len(zero_indices)
                    rand_index1 = random.randint(0,zero_index_len-1)
                    rand_index2 = random.randint(0,zero_index_len-1)
                    game1 = zero_indices[rand_index1]
                    game2 = zero_indices[rand_index2]
                else:
                    continue
            elif i > 5:
                break_outer_loop = True
                break
                
            # Now check if all games have unique values
            # If they all have unique values, chances are the user
            # has sorted the list.
            unique_values = list(set(ranked_game_values))
            if len(unique_values) == len(game_year_list):
                break_outer_loop = True
                break
            
        else:
            # Decrement game indices
            game1 = game1 - 2
            game2 = game2 - 2
    if break_outer_loop:
        break
        
# Print out list as ranked, but sort the lists first
ranked_game_value_sorted = []

# Organize ranked_game_list and ranked_game_values into a 
# list of tuples
for index, value in enumerate(ranked_game_values):
    game = ranked_game_list[index]
    ranked_game_value_sorted.append((game,value))
    

# Sort the list according to the value
ranked_game_value_sorted = sorted(ranked_game_value_sorted, key = lambda x: x[1])
ranked_game_value_sorted.reverse()

# Now print the list
for index,game in enumerate(ranked_game_value_sorted):
    print(f"{index+1}. {game[0]}")
        
        
        