import requests
import warnings
requests.packages.urllib3.disable_warnings()

headers={'Host':'www.linkedin.com', 'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.115 Safari/537.36'}

def crawl_employees(company, title):
	responses = []
	try:

		response = requests.get("https://www.linkedin.com/title/{}-at-{}".format(title.replace(' ', '-'), company.replace(' ', '-')), timeout=3, headers=headers)
		responses.append(response.text)
	
	except requests.exceptions.Timeout as e:
		warnings.warn("Warning: Timed out attempting to crawl {}".format(title))
	except Exception as e:
		print(e)

	return responses
