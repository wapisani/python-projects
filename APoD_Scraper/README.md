# Will Pisani's Astronomy Picture of the Day Bulk Image Downloader (APoDBID)

![APoD image of the day on Sept 6, 2019](https://github.com/wapisani/python-projects/blob/master/APoD_Scraper/Images/Chandrafirstlight_0_1024.jpg "APoD image of the day on Sept 6, 2019")

Astronomy Picture of the Day on September 6, 2019.

APoDBID will allow the user to download either the current APoD or to bulk download images from the archive. Currently, you can attempt to download the entire archive (which will takes days to weeks) or you can specify the date to go back in time from in a yymmdd format. If you specify the date, the code will download image from that date back in time. For example, if you specify "090909" (September 9, 2009), the script will download the APoD on that date and all APoD's before that date.

The code has been written to mimic a human browsing the archive and downloading images by pausing for a random period of time (between 30 and 75 seconds) between page pulls. This helps to decrease load on APoD's servers.