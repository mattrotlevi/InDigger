# InDigger
  
InDigger is a web scraping tool for LinkedIn. Given a company name, it goes through a predefined list of departments and returns the employees, their job title, their work experience, and their education.

### Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

Run the command:

```
git clone https://github.com/mattrotlevi/InDigger.git
```

Within the directory, run the command:

```
python InDigger.py -h
```
Your output will be
```
usage: InDigger.py [-h] [--company string] [--emps file]
                           [--emailformat string]

InDigger - A LinkedIn scraping tool by Matt Rotlevi

optional arguments:
  -h, --help            show this help message and exit

Company Name:
  --company string      Enter the company name you want to run the search on

Employee Harvesting:
  --emps file           Discover employees by title and/or department. Titles
                        and departments are imported from a new line delimited
                        file. [Default: title-list-small.txt]
  --emailformat string  Create email addresses for discovered employees using
                        a known format. [Accepted Formats: first.last@xyz.com,
                        last.first@xyz.com, firstl@xyz.com, lfirst@xyz.com,\
                        flast@xyz.com, lastf@xyz.com, first@xyz.com,
                        last@xyz.com]
```

As a demonstration of the program's ability, enter:

```
python InDigger.py --company "company name" --emps "/home/mattr/scraper/wordlists/title-list-small.txt" --emailformat first.last@company.com
```
The output will look like

```
---------------------------------------------------------------
FINANCE
---------------------------------------------------------------

NAME:Jane Doe
---------------------
Education:
-  ABC College
Experience:
-  Director, Financial Planning &amp; Analysis at Company Name
-  Manager - Finance at WTAS
-  Manager of Finance at The Madison Square Garden Company, Inc
-  Financial Analyst at Broadridge Financial Solutions, Inc
-  Intern at Merrill Lynch
Job Title:
-  Director, Financial Planning &amp; Analysis at Company Name
EMAIL: jane.doe@company.com 

NAME:John Doe
---------------------
Education:
-  ABC University
-  XYZ High School
Experience:
-  Finance Intern at Company Name
Job Title:
-  Intern at Company Name
EMAIL: john.doe@company.com
```
## Authors 
- Matt Rotlevi
