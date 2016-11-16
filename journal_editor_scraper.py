import csv
import requests
import bs4

def getJGREditors():
#get editors from various JGR publications

	issns = {'JGR_Atmospheres' : '(ISSN)2169-8996',
			'JGR_Biogeosciences' : '(ISSN)2169-8961',
			'JGR_EarthSurface' : '(ISSN)2169-9011',
			'JGR_Oceans' : '(ISSN)2169-9291',
			'JGR_Planets' : '(ISSN)2169-9100',
			'JGR_SolidEarth' : '(ISSN)2169-9356',
			'JGR_SpacePhysics' : '(ISSN)2169-9402'
	}

	eds = []
	
	journalBaseUrl = 'http://agupubs.onlinelibrary.wiley.com/hub/jgr/journal/10.1002/'
	journalEditorBoard = '/editorial-board/editorial-board.html'
	
	for key, issn in issns.items():
		results = requests.get(journalBaseUrl + issn + journalEditorBoard)
		reqSoup = bs4.BeautifulSoup(results.text, "html.parser")
		res = reqSoup.select('.homepageFragment > table > tbody > tr > td > p > strong')
		
		i = 0
		while i < len(res):
			eds.append((key, res[i].text))
			i += 1
	
	with open('JGREeditors.csv', 'w') as f:
		writer = csv.writer(f, delimiter = ',', quotechar = '\'')
		for editor in eds:
			writer.writerow([editor])

def getACPEditors():
	
	eds_r = []
	eds_w = []
	
	journalBaseUrl = 'http://www.atmospheric-chemistry-and-physics.net/editorial_board.html'
	
	results = requests.get(journalBaseUrl)
	reqSoup = bs4.BeautifulSoup(results.text, "html.parser")
	eds_res = reqSoup.select('h3')
	eds_work = reqSoup.select('.get_users_by_group_result_affiliation')
	
	i = 0
	while i < len(eds_res):
		eds_r.append(eds_res[i].text)
		i += 1
	
	i = 0
	while i < len(eds_work):
		eds_w.append(eds_work[i].text)
		i += 1
		
	combined_data = [item for pair in zip(eds_r, eds_w + [0]) for item in pair][:-1]
	
	with open('ACPEditors.csv', 'w') as f:
		writer = csv.writer(f, delimiter = ',', quotechar = '\'')
		for item in combined_data:
			writer.writerow([item.encode('utf-8')])

def getAMSEditors():
	
	eds = []

	journalBaseUrl = 'https://www.ametsoc.org/ams/index.cfm/publications/'
	journals = {'AMS_climate' : 'journals/journal-of-climate/editors-and-staff-contacts/',
				'AMS_atmospheric' : 'journals/journal-of-the-atmospheric-sciences/editors-and-staff-contacts/',
				'AMS_monthly_weather' : 'journals/monthly-weather-review/editors-and-staff-contacts/',
				'AMS_app_meteor_climatology' : 'journals/journal-of-applied-meteorology-and-climatology/editors-and-staff-contacts/',
				'AMS_atmosph_and_ocean_tech' : 'journals/journal-of-atmospheric-and-oceanic-technology/editors-and-staff-contacts/',
				'AMS_hydrometeorology' : 'journals/journal-of-hydrometeorology/editors-and-staff-contacts/',
				'AMS_bulletin' : 'bulletin-of-the-american-meteorological-society-bams/bams-editors-and-staff-contacts/'
	}
				
	for key, root in journals.items():
		results = requests.get(journalBaseUrl + root)
		reqSoup = bs4.BeautifulSoup(results.text, "html.parser")
		if key != 'AMS_bulletin':
			email_res = reqSoup.select('p > a')
			no_email_res = reqSoup.select('p')
		else:
			email_res = reqSoup.select('p > strong')
			
	
		i = 0
		while i < len(email_res):
			eds.append((key, email_res[i].text))
			i += 1
		
		i = 0 
		while i < len(no_email_res):
			eds.append((key, no_email_res[i].text))
			i += 1
		
	with open('AMSEditors.csv', 'w') as f:
		writer = csv.writer(f, delimiter = ',', quotechar = '\'')
		for editor in eds:
			writer.writerow([editor])
 
def getTandFEditors():
	
	eds = []
	
	journalBaseUrl = 'http://www.tandfonline.com/action/'
	root = 'journalInformation?show=editorialBoard&journalCode=uast20'
	
	results = requests.get(journalBaseUrl + root)
	reqSoup = bs4.BeautifulSoup(results.text, "html.parser")
	res = reqSoup.select('div > b')
	
	i = 0
	while i < len(res):
		eds.append(res[i].text)
		i += 1
		
	with open('TandFEditors.csv', 'w') as f:
		writer = csv.writer(f, delimiter = ',', quotechar = '\'')
		for editor in eds:
			writer.writerow([editor.encode('utf-8')])
	
getJGREditors()
getACPEditors()
getAMSEditors()
getTandFEditors()