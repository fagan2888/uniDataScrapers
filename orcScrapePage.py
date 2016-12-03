import csv
from selenium import webdriver


driver = webdriver.PhantomJS() #headless WebKit scriptable with a JavaScript API
driver.implicitly_wait(2) #wait 2 seconds to poll DOM for element
workPlace = []
i = 0

f = open('jim_names_orcids.csv') #infile of orcid numbers
csv_f = csv.reader(f)

outfile = open('jim_names_orcids_compare2.csv', 'w') #outfile of names, numbers, work and edu. info
data = csv.writer(outfile)

for column in csv_f:
	orcidId = column[3] #edit according to infile data location
	firstName = column[2]
	lastName = column[1]
	number = column[0]
	institution = column[4]

	driver.get("http://orcid.org/" + orcidId)

	for item in driver.find_elements_by_xpath("//ul[@id='employments-list']"):
		personData = item.text
		if item is None:
			personData = 'no data'
			continue
	for item in driver.find_elements_by_xpath("//ul[@id='educations-list']"):
		eduData = item.text
		if item is None:
			eduData = 'no data'
			continue
		data.writerow([number, firstName, lastName, orcidId, institution, personData.encode('utf-8'), eduData.encode('utf-8')])


driver.quit()