#imports

import xlsxwriter
import random

# format of the Location lists
# [id, name, coords, location, contact name, contact num, contact email, website,
# cost,	description, Tags(strings delim by ;), 
# Accessibility(strings delim by ;), picture, date, user_id
data = (
	[1, 'St. James the lass church hall 1', "55581, -4.292699",
	 "Penicuik", "Vestry Secretary", "01968768954", "phillg13@toucansurf.com",
	  "https://stjamesthelesspenicuik.org", "free",
	 "Hall for hire, welcome to use if available, contact us for more",
	"Sight;Hearing;sound;music;safe space;flexible;quiet;solitary;indoors;",
		"parking",
	"Wheelchair friendly;Safe", None, "10/10/1998", None],

	[2, 'St. James the lass church hall 2', "55.873581, -4.292699",
	 "Penicuik", "Vestry Secretary", "01968768954", "phillg13@toucansurf.com",
	  "https://stjamesthelesspenicuik.org", "free",
	 "Hall for hire, welcome to use if available, contact us for more",
	"Sight;Hearing;sound;music;safe space;flexible;quiet;solitary;indoors",
		"parking",
	"Wheelchair friendly", None, "10/10/1998", None],
	[3, 'St. James the lass church hall 3', "55.873581, -4.292699",
	 "Penicuik", "Vestry Secretary", "01968768954", "phillg13@toucansurf.com",
	  "https://stjamesthelesspenicuik.org", "£10 per hour",
	 "Hall for hire, welcome to use if available, contact us for more",
	"Sight;Hearing;sound;music;safe space;flexible;quiet;solitary;indoors",
		"parking",
	"Wheelchair friendly", None, "10/10/1998", None]
)

data = (
 [1, 2, 3],
 ['St. James the lass church hall 1', 'St. James the lass church hall 2', 'St. James the lass church hall 3'],
 ["55581, -4.292699", "55.873581, -4.292699", "55.873581, -4.292699"],
 ["Penicuik"],
 ["Vestry Secretary"],
 ["01968768954"],
 ["phillg13@toucansurf.com"],
 ["https://stjamesthelesspenicuik.org"],
 ["£10 per hour", "free", "£5 per hour"],
 ["Hall for hire, welcome to use if available, contact us for more"],
 ["Sight", "Hearing", "Sound", "Music", "safe space", "flexible", "quiet", "solitary", "indoors"],
 ["parking", "wheelchair", "safe"],
 [""],
 ["10/10/1998"],
 [""])
 


def populateNew(n):
	workbook = xlsxwriter.Workbook('Locations.xlsx')
	locations = workbook.add_worksheet()
	
	for row in range(n):
		for i in range(len(data)):
			locations.write(row,i, data[i][random.randint(0,len(data[i])-1)])
	workbook.close()
	return()
	

def populate():
	workbook = xlsxwriter.Workbook('Locations.xlsx')
	locations = workbook.add_worksheet()

	row = 0

	for location in data:
		col = 0
		for i in range(len(location)):
			locations.write(row, col, location[col])
			col += 1
		row += 1
		print("Created location " + str(row))

	workbook.close()


 # Execution

if __name__ == '__main__':
	print("Starting population script, This will take a few minutes...")
	populateNew(100)
	print("Population Script complete")
