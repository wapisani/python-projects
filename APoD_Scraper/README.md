# Will Pisani's Astronomy Picture of the Day Bulk Image Downloader (APoDBID)

![APoD image of the day on Sept 6, 2019](https://github.com/wapisani/python-projects/blob/master/APoD_Scraper/Images/Chandrafirstlight_0_1024.jpg "APoD image of the day on Sept 6, 2019")

Astronomy Picture of the Day on September 6, 2019.

APoDBID will allow the user to download either the current APoD or to bulk download images from the archive. Currently, you can attempt to download the entire archive or you can specify the date to go back in time from in a yymmdd format. If you specify the date, the code will download image from that date back in time. For example, if you specify "090909" (September 9, 2009), the script will download the APoD on that date and all APoD's before that date.

The code has been written to mimic a human browsing the archive and downloading images by pausing for a random period of time (between 30 and 75 seconds) between page pulls. This helps to decrease load on APoD's servers. This also increases the time it will take to download the archived images. With this delay, it took my computer and internet connection three days, nine hours, and one minute to download everything from September 1, 2019 to May 9, 2007. The total number of images from this date range is 4,234. 41% of these images are 1 MB or larger. The total size of all images between the aforementioned dates is **5.78 GB**. This [lifehacker article](https://lifehacker.com/download-the-entire-archive-of-nasas-astronomy-picture-5774707) says that the total size of images from the beginning of the archive (June 16, 1995) to around March 2, 2011 is about 2.64 GB. From what I downloaded, the total size of the images of the date range March 2, 2011 to September 6, 2019 is 4.24 GB. This puts the total size of the archive at around **6.88 GB**. Be sure you have at least that much space before attempting to download the entire archive.

## How do I use it?
You will need a Python 2.7/3.7.4 installation with the following libraries: requests, os, re, time, random, and beautifulsoup4.  requests and bs4 are not included in the standard Python 2.7/3.7.4 library so you will likely need to install them separately if you downloaded Python 2.7/3.7.4 through your package manager or [pip](https://docs.python.org/2.7/installing/index.html). If you don't have Python 2.7/3.7.4 installed already, I recommend the [Anaconda Python distribution](https://www.anaconda.com/distribution/). It has everything a scientist would need as well as everything needed to run APoDBID. If you do end up needing to install something, you can do so with [conda](https://conda.io/projects/conda/en/latest/user-guide/getting-started.html).

Once you have Python set up, download APoD_Scraper.py (right-click -> save as) to your computer. Before you run the file with ```python APoD_Scraper.py```, you need to open it up with the text editor of your choice and change a couple things. First, where do you want to save the images? Set the directory where the images will be saved on line 34 ```directory =``` by replacing the characters between the quotation marks "" with the path to your chosen directory. Second, do you want to only download the current picture of the day or do you want to download the entire archive? If the current picture only, set ```current_flag = 1```. If the entire archive, set ```current_flag = 0```.
Thirdly, maybe you want to only download images from a certain date then proceed backwards in time? (NOTE: this can be helpful if the code breaks after a certain period of time when downloading the entire archive.) If so, set the date on line 49 by replacing the characters between the "" with your yymmdd date. Then set ```download_date_flag = 1```. Lastly, save the file.

Once you've made the required changes, run the script with the command ```python APoD_Scraper.py```. If using the command prompt or terminal, you will first need to navigate to that directory using ```cd```. You can also use an IDE like Spyder to run it.

## Future Improvements
The script works well, but it could use improvement. I'd like to add in command line options for setting the current image or archive, date range, etc. I'd like to include the ability to specify a date range to download (say download all images between 2010 and 2019). I'd like to include another option to specify a date and then download all image newer than that date. A GUI wrapper for the script might be helpful, but may be troublesome to set up.

## License
MIT License

Copyright (c) 2019 Will Pisani

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
