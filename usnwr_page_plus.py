import itertools
import csv
import requests
import bs4

def getSchools(names):
#get list of school names
	schools = []
	i = 0
	while i < len(names):
		for name in names:
			schoolname = names[i].get_text()
			i += 1
			schools.append(schoolname.encode('utf-8'))
	return schools

def getScores(tableAll):
#get list of program scores
	scores = []
	i = 0
	while i < len(tableAll[0].select('.rankscore-bronze')):
		for score in tableAll[0].select('.rankscore-bronze'):
			number = tableAll[0].select('.rankscore-bronze')[i].get_text()
			i += 1
			scores.append(number)
	return scores


					
nationalUrl = 'http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/'

#change page number from 2 - 6 to get rankings 25 - 140; not published beyond 140
program = [ 'top-engineering-schools/eng-rankings/page+6', 
			'top-science-schools/biological-sciences-rankings/page+6', 
			'top-science-schools/chemistry-rankings/page+6', 
			'top-science-schools/computer-science-rankings/page+6', 
			'top-science-schools/mathematics-rankings/page+6', 
			'top-science-schools/physics-rankings/page+6'
			]

rankings = {}
headers = {"User-agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.80 Safari/537.36"}

i = 0
while i < len(program): 
	results = requests.get(nationalUrl + program[i], headers=headers)
	reqSoup = bs4.BeautifulSoup(results.text, "html.parser")
	tableAll = reqSoup.find_all('tbody') #save entire webpage table as bs object
	names = reqSoup.select('.school-name')  #save school name classes as bs object
	schools = getSchools(names)
	scores = getScores(tableAll)
	for j, school in enumerate(schools):
		if school not in rankings:
			rankings[school] = {'School': school, program[i]: scores[j]}
		else:
			rankings[school].update({program[i]: scores[j]})
	i += 1

			
print(rankings)

with open('usnwr_schools.csv', 'w') as f:
	writer = csv.DictWriter(f, fieldnames=['School'] + program)
	writer.writeheader()
	for row in rankings:
		writer.writerow(rankings[row])