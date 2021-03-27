#!/usr/bin/python

import os
import sys
import urllib.request
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument(action='store', dest='csvname', help="CSV Filename")
parser.add_argument(action='store', dest='urlname', help="Column name with URL")
args = parser.parse_args()
opener = urllib.request.build_opener()
opener.addheaders = [('User-Agent','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/74.0.3729.169 Safari/537.36')]
urllib.request.install_opener(opener)

try:
	csvname = args.csvname
	urlname = args.urlname
except:
	print ("\nERROR: Please specify csvname and url column name to download\n")	
	print ("Usage:")
	print (" $ <.py> data.csv image_url\n")
	print ("- First param should be the csv file path")
	print ("- Second param should be the column name that has image urls to download\n")	
	sys.exit(0)	

# open csv file to read
with open("{0}.csv".format(csvname), 'r') as csvfile:
	csv_reader = csv.reader(csvfile)
	# iterate on all rows in csv
	for row_index,row in enumerate(csv_reader):
		# find the url column name to download in first row
		if row_index == 0:
			FILE_URL_COL_NUM = None
			for col_index,col in enumerate(row):
				# find the index of column that has urls to download
				if col == urlname:
					FILE_URL_COL_NUM = col_index 				
			if FILE_URL_COL_NUM is None:
				print ("\nERROR: url column name '"+urlname+"' not found, available options:")	
				for col_index,col in enumerate(row):
					print (" " + col)	
				print ("\nUsage:")
				print (" $ <.py> data.csv image_url\n")
				sys.exit(0)
			continue
		# find image urls in rows 1+
		file_url = row[FILE_URL_COL_NUM]
		# check if we have an image URL and download
		if file_url != '' and file_url != "\n":
			file_name = file_url.split('/')[-1].split('?')[0]
			directory = csvname.split('.csv')[0] + '/' + row[0]
			if not os.path.exists(directory):
				os.makedirs(directory)
			try:
				urllib.request.urlretrieve(file_url, directory+'/'+file_name)
				print ("["+str(row_index)+"] File saved: " + file_name)
			except:
				# second attempt to download if failed
				try:
					urllib.request.urlretrieve(file_url, directory+'/'+file_name)
					print ("["+str(row_index)+"] File saved: " + file_name)
				except:
					print ("["+str(row_index)+"] Could not download url: " + file_url)
		else:
			print ("["+str(row_index)+"] No " + urlname)
