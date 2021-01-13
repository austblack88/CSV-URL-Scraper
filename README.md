# CSV-URL-Scraper

A simple batch file scraper for use with CSV files.

This script works excellently with the [Web Scraper  Chrome extension](https://chrome.google.com/webstore/detail/web-scraper-free-web-scra/jnhgnonknehpejjnehehllkliplmbmhn), as it exports scraped URLs to a CSV file. 

## Usage
This script requires that the CSV file follows a format similar to this: 
```
================|=======================================|========
  SUBDIRECTORY  |               FILE-URLS               |  ...   
================|=======================================|========
    Folder 1    |  https://website.net/someimage1.png   |  ...   
================|=======================================|========
    Folder 1    |  https://website.net/someimage2.jpg   |  ...   
================|=======================================|========
    Folder 2    |  https://website.net/somevideo1.webm  |  ...   
================|=======================================|========
    Folder 3    |  https://website.net/somevideo2.mp4   |  ...   
================|=======================================|========
      ...       |                 ...                   |  ...
```

This script creates a new directory with the same name as the input CSV file.

The first row of the CSV serves as a header to identify which column contains the file URLs to be scraped. 

In the following rows, the first column of each row serves as the name of the subdirectory that the respective file will be downloaded to. 

Users will be prompted to enter the name of the CSV file to be used, followed by the name of the column that contains the desired file URLs.
From there, the files will be downloaded sequentially.
