from bs4 import BeautifulSoup
import re
import pprint

def soupify(response):
	try:
		soup_dict = BeautifulSoup(response, 'lxml')
		#print soup_dict.prettify()
		return soup_dict
	except Exception as e:
		print(e)

def get_employees(soup):
	try: 
		employees = {}
		
		pro_cont = soup.findAll('li', class_='professionals__result-container')
		

		for div in range(len(pro_cont)):
			name = re.findall(re.escape('title-professional-name">')+"(.*?)"+re.escape('</a>'), str(pro_cont[div]))
			headline = re.findall(re.escape('<p class="professional__headline">')+"(.*?)"+re.escape('</p>'), str(pro_cont[div]))
			schools = re.findall(re.escape('<p class="professional__school-name">')+"(.*?)"+re.escape('</p>'), str(pro_cont[div]))
			companies = re.findall(re.escape('<p class="professional__company-name">')+"(.*?)"+re.escape('</p>'), str(pro_cont[div]))
			employee_info = {}
			employee_info["Job Title"] = headline[0]
			employee_info["Education"] = schools
			employee_info["Experience"] = companies
			
			employees[name[0]] = employee_info
	
		return employees

	except Exception as e:
		print(e)
