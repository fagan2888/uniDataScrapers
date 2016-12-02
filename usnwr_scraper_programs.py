import csv
import requests
import bs4

def getSchools(names):
#get list of school names

	i = 0
	while i < len(names):
		for name in names:
			schoolname = names[i].get_text()
			i += 1
			schools.append(schoolname)

def getScores(tableAll):
#get list of program scores

	i = 0
	while i < len(tableAll[0].select('.rankscore-bronze')):
		for score in tableAll[0].select('.rankscore-bronze'):
			number = tableAll[0].select('.rankscore-bronze')[i].get_text()
			i += 1
			scores.append(number)


schools = []
scores = []
					
nationalUrl = 'http://grad-schools.usnews.rankingsandreviews.com/best-graduate-schools/'

program = [ 'top-engineering-schools/eng-rankings/', 
			'top-science-schools/biological-sciences-rankings', 
			'top-science-schools/chemistry-rankings', 
			'top-science-schools/computer-science-rankings', 
			'top-science-schools/mathematics-rankings', 
			'top-science-schools/physics-rankings'
			]
i = 0
while i < len(program): 
	results = requests.get(nationalUrl + program[i])
	reqSoup = bs4.BeautifulSoup(results.text, "html.parser")
	tableAll = reqSoup.find_all('tbody') #save entire webpage table as bs object
	names = reqSoup.select('.school-name')  #save school name classes as bs object
	getSchools(names)
	getScores(tableAll)
	i += 1

			
print(schools, scores)

with open('usnwr_schools.csv', 'w', newline='') as f:
	writer = csv.writer(f)
	for school, score in zip(schools, scores):
		writer.writerow([school.encode('utf-8'), score])

		
