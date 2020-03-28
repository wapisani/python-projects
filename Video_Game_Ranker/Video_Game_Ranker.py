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
    

