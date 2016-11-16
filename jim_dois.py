import json
import csv
import requests


#Open csv file to read from
f = open('dois.csv')
csv_f = csv.reader(f)
citations = open('citations.txt', 'w')
citationsTwo = open('citations2.txt', 'w')

for number in csv_f:
	doi = number[0]
	
	results = requests.get('http://api.crossref.org/works/' + doi).json()
	res = results['message']
	
	i = 0
	names = []
	for name in res['author']:
		authorSurname = res['author'][i]['family']
		authorFirstname = res['author'][i]['given']
		names.append([str(authorSurname.encode('utf-8')), str(authorFirstname.encode('utf-8'))])
		i += 1
	if 'page' not in res:
		page = 'no pages'
	else:
		page = res['page']
	type = res['type']
	date = res['issued']['date-parts'][0][0]
	title = res['title'][0]
	url = res['URL']
	if 'volume' not in res:
		volume = 'no volume'
	else:
		volume = res['volume']



	citations.write('TY - ' + str(type) + '\nAU - ' + str(authorSurname.encode('utf-8')) + ', ' + str(authorFirstname.encode('utf-8')) + '\nDO - ' + str(doi) + '\nPY - ' + str(date) + '\nTI - ' + str(title.encode('utf-8')) + '\nUR - '  + str(url) + '\nSP - ' + str(page) + '\nVL - ' + str(volume) + '\n\n')
	
	citationsTwo.write('TY - ' + str(type) + '\nAU - ' + str(names) + '\nDO - ' + str(doi) + '\nPY - ' + str(date) + '\nTI - ' + str(title.encode('utf-8')) + '\nUR - '  + str(url) + '\nSP - ' + str(page) + '\nVL - ' + str(volume) + '\n\n')
