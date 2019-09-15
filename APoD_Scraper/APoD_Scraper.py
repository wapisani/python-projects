# -*- coding: utf-8 -*-
"""
Created on Sun Sep  1 00:17:35 2019

@author: Will Pisani

This script will scrape the Astronomy Picture of the Day and download either every image from the archive or just the current day's picture.

Program Usage:
Change the directory to a directory on your own PC.
Set the flag for archive or current picture of the day. Archive is 0. Current is 1
Run from the command line or using an IDE like Spyder
If you do the archive option, you have the additional option of starting at a certain date
and going backwards in time from there. This is a helpful option for when the program breaks while
you're trying to download the entire archive. Just put in the date in a yearyearmonthmonthdayday format
or yymmdd on line 49 and set the download_date_flag to 1.
    
Future improvements:
Option to download a date range
Option to download starting at a date and then moving forward through time
Command line options for archive or picture of the day

Python and library requirements
Tested on Python 2.7 and 3.7.4
requests, os, re, time, random, and bs4
"""

# Import necessary libraries
import requests
import os
import re
import time
import random
from bs4 import BeautifulSoup

# Set directory to download image(s) to
directory = "F:\Pictures\Space\APoD"
os.chdir(directory)

# Set flag for archive (0) or current day (1)
current_flag = 0

# Set APoD web URLs
apod_archive = "http://apod.nasa.gov/apod/archivepix.html"
apod_current = "http://apod.nasa.gov/apod/astropix.html"

# Local versions of html files for testing
#apod_archive = "F:\Code\Python\python-projects\APoD_Scraper\Astronomy Picture of the Day Archive.html"
#apod_current = "F:\Code\Python\python-projects\APoD_Scraper\Astronomy Picture of the Day.html"

# Set date to start downloading back in time from
download_date = "090825" # Nov 18, 2014
download_date_flag = 0 # 0 if downloading entire archive

# Scrape the appropriate web page
if current_flag == 1:
    
    # Query web server for web page, think I got blocked
    apod_result = requests.get(apod_current)
    
    # Using local web page for testing
#    with open(apod_current,'r') as html_file:
#        apod_content = html_file.read()
        
    # Store content
    apod_content = apod_result.content
    
    # Start parsing
    soup = BeautifulSoup(apod_content,'html.parser')
    
    # All image links
    image_links = [link['href'] for link in soup.findAll("a")]
    
    # Prefix the link with http://apod.nasa.gov/apod/
    for index,link in enumerate(image_links):
        
        if link.find('.jpg') > -1 and link.find('apod.nasa.gov') > -1:
            # Get filename of image
            filename = link.split('/')[-1]           
        
            # Download image
            apod_image = requests.get(link).content
            with open(filename, 'wb') as image:
                image.write(apod_image)
        
    
  
    
else:
    # Going through archive and downloading images
    
    # Using local web page for testing
#    with open(apod_archive) as html_file:
#        apod_content = html_file.read()
        
    # Open web page
    print("Getting the archive web page now....")
    apod_result = requests.get(apod_archive)
    
    # Store content
    apod_content = apod_result.content
    
    print("Got the contents of the archive web page!\nNow moving on to downloading...")
    # Start parsing
    soup = BeautifulSoup(apod_content,'html.parser')
    
    # Get all links to the individual posts
    # Pattern of APoD html links is apyymmdd
    regex = re.compile('ap\d\d\d\d\d\d')
    page_links = [link['href'] for link in soup.findAll("a") if re.match(regex,link['href'])]
    
    # Iterate through pages to find the date to start from
    if download_date_flag == 1:
        
        # Get index of requested date in page_links
        date_index = page_links.index('https://apod.nasa.gov/apod/ap'+download_date+'.html')
        
        # Replace page_links with slice of page_links going from download_date to the past
        page_links = page_links[date_index:]
        
                    
    # Iterate through pages and download the image
    for page in page_links:
        
        # Check for existence of https://apod.nasa.gov/apod/ in page link
        if "https://apod.nasa.gov/apod/" in page:
            print("Attempting to get page {}\n".format(page))
            
            # Query web server for web page
            result = requests.get(page)
        else:
            page = "https://apod.nasa.gov/apod/" + page
            
            print("Attempting to get page {}\n".format(page))
            
            # Query web server for web page
            result = requests.get(page)
            
        
        # Store content
        content = result.content
        
        print("Got the page {} successfully\n".format(page))
        
        print("Starting parsing")
        # Start parsing
        soup = BeautifulSoup(content,'html.parser')
        
        # Get year and month from page name
        pagename = page.split('/')[-1].split('.')[0]
        page_year_month = pagename[2:-2]
        
        # All image links
        image_links = []
        
        # Start loop
        for link in soup.findAll("a"):
            try:
                image_links.append(link['href'])
                
            except KeyError:
                continue
        
        
        
        print("Parsing successful. Now iterating over found images")
        
        # Iterate over images
        for image in image_links:
            
            
            if image.find('.jpg') > -1 and image.find('image/'+page_year_month) > -1:
                
                # Just in case the image link is complete already
                if image.find("http") > -1:
                    new_link = image
                else:
                    # Need to prefix the image link with http://apod.nasa.gov/apod/
                    new_link = "http://apod.nasa.gov/apod/" + image
                    
                print("Attempting to download image {} now".format(new_link))
                
                # Get filename of image, combine it with the post number
                filename = pagename + "_" + image.split('/')[-1].rstrip().lstrip()
                
                # Strip out random newline characters
                filename.lstrip().rstrip()
                
                # Check if file already exists
                if os.path.isfile(filename) == True:
                    print("Image already exists. I will not re-download it. Moving on...\n")
                    continue
                else:
                    # Download image
                    apod_image = requests.get(new_link).content
                    with open(filename, 'wb') as img:
                        img.write(apod_image)
                        
                    print("Downloaded {} successfully!!\n".format(filename))
                    
        # Sleep for somewhere between 30 and 75 seconds between page requests, 
        time_to_sleep = random.randint(30,75)
        print("Sleeping for {} seconds ".format(time_to_sleep))
        time.sleep(time_to_sleep)