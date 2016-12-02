import requests
import bs4
import csv

 

root = 'http://www.shanghairanking.com'

discipline = ['/FieldENG2016.html', '/FieldSCI2016.html', '/FieldLIFE2016.html', '/SubjectCS2015.html', '/SubjectChemistry2015.html', '/SubjectPhysics2015.html', '/SubjectMathematics2015.html']

schoolsAll = 'ARWU2016.html'

i = 0
while i < len(discipline):
 
	res = requests.get(root + discipline[i])
	soup = bs4.BeautifulSoup(res.text, "html.parser")
	tableAll = soup.select('#UniversityRanking')

	i = 0
	while i < len(tableAll[0].select('a[href^="World-University-Rankings"]')):
		for item in tableAll[0].select('a[href^="World-University-Rankings"]'):
			name = tableAll[0].select('a[href^="World-University-Rankings"]')[i].get_text()
			print(name)
			i += 1
			
			
			
			
			i = 0
			while i < len(tableAll[0]):
				for item in tableAll[0].select('[href*="../World-University-Rankings/"]'):
					print(item.get_text())
					
			http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/Mechanical-Engineering-2016.html
			http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/Materials-Science-Engineering-2016.html
			
			http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/Environmental-Science-Engineering-2016.html
			
			http://www.shanghairanking.com/Shanghairanking-Subject-Rankings/Chemical-Engineering-2016.html
			
			
			tableAll[0].select('[href*="../World-University-Rankings/"]')