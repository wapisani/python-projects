#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 14:43:40 2020

@author: wapisani

This script will run on the hour every hour during daytime hours and 
announce the number of days until Christmas. 
Instrumental Christmas choruses like bells, chipmunk-sounding
chipmunk-sounding voice for countdown
Starting at 9:00 Am on december 1st and repeating every hour on the hour until
11:00 PM on the same day. Repeat every day until Dec 26th.
Announcing the number of days until Christmas then playing a random Xmas
jingle and then be silent until the next hour.

This script will be scheduled with cron to only run during the month of 
December and only until Dec 26. https://www.adminschoice.com/crontab-quick-reference
On Xmas, it will say "Merry Christmas!"
On Dec 1, it will say "24 days until Christmas."
On Dec 24, it will say "1 day until Christmas."
"""

# Import necessary libraries
from datetime import date

############################
# Check the day
############################
today_date = date.today()
month = today_date.month
day = today_date.month
xmas_day = 25
print(f"Today is {today_date}")


############################
# Announce the day
############################
# The announcement_dict will contain key-value pairs of the date
# and a string of the filename of the announcement to play
announcement_dict = {}
# Placeholder code as an example
for key in range(1,25):
    day = 25-key
    announcement_dict[key] = f'{day} day(s) until Christmas' 

announcement_dict[25] = 'Merry Christmas!'

############################
# Play a random Xmas jingle
############################
# xmas_jingles will be a list of strings containing the filenames
# of random Xmas jingles.
xmas_jingles = ['jingle_bells.mp3','silent_night.mp3','run_run_rudolph.mp3']
# Get a random jingle and then play it




