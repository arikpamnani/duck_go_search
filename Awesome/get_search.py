import urllib2
import requests
import csv
import json
import os
import inspect
import time
import xlsxwriter
from get_duck_search import get_search
file_name = "/home/arik/Voter_Data_Analysis/Voter_Dataset_Analysis/Dataset/Dataset_CSV/RQ7503 - 2016 Primary.csv"
path = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))	
all_names = []
with open(file_name, 'rb') as csv_file:
	file_reader = csv.reader(csv_file, delimiter=',')
	for row in file_reader:	
		name = [row[2], row[3], row[1]]
		all_names.append(name)
for i in range(0, len(all_names)):
	all_names[i] = all_names[i][0].capitalize() + " " + all_names[i][1].capitalize() + " " + all_names[i][2].capitalize()
all_names = all_names[1:]
API_KEY = "AIzaSyBDueIxRjyf7mlziSXn7Xw-K5lmZoAeIVM"
cx = "001127494544831080190:gigbkjql3ni"
def query(name):
	google_custom_url = "https://www.googleapis.com/customsearch/v1?key=" + API_KEY + "&cx=" + cx + "&q=" + name
	return google_custom_url
# building proxy
proxy = {'http': 'proxy.iiit.ac.in:8080', 'https': 'proxy.iiit.ac.in:8080'}
num_user = 0
party = ['Democrat', 'Republican', 'Independent']
county = 'Madison'
workbook = xlsxwriter.Workbook("DuckDuckGo.xlsx")
worksheet = workbook.add_worksheet()
row = 1
col = 0
max_users = 100
for name in all_names:
	for j in range(0, 3):
		# building the query
		q = [name, party[j], county]
		try:
			top_three = get_search(q)
		except:
			break
		mend = len(top_three)
		while(mend < 5):
			top_three.append(["", ""])
			mend += 1
		# writing PERSON NAME and PARTY NAME
		worksheet.write(row, col, name)
		worksheet.write(row, col + 1, party[j])
		worksheet.write(row, col + 2, top_three[0][0])
		worksheet.write(row, col + 3, top_three[0][1])
		worksheet.write(row, col + 4, top_three[1][0])
		worksheet.write(row, col + 5, top_three[1][1])
		worksheet.write(row, col + 6, top_three[2][0])
		worksheet.write(row, col + 7, top_three[2][1])
		worksheet.write(row, col + 8, top_three[3][0])
		worksheet.write(row, col + 9, top_three[3][1])
		worksheet.write(row, col + 10, top_three[4][0])
		worksheet.write(row, col + 11, top_three[4][1])
		row += 1
	row += 1
	num_user += 1
	print("Number of Users completed - " + str(num_user))
	time.sleep(3)
	if(num_user >= max_users):
		break
workbook.close()

