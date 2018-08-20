import os, argparse, sys, time
from crawler import *
from soupifyer import *
from formatter import *
from outputter import *


def display(employees, emailformat):

	i = 0
	if args.csv:
		csv_output(employees, emailformat ,args.csv, )
	else:
		for department, value in employees.items():
			print("\n------------------------------------------------------------------------------------------------------------------------------")
			print(department.upper())
			print("------------------------------------------------------------------------------------------------------------------------------")
			if employees[department] is not None:
				for name, value in employees[department].items():
					i+=1
					print("\nNAME:", name)
					email_formatted = email_formatter(name, emailformat)
					print("---------------------")
					for emp_info, value in employees[department][name].items():
						print(emp_info + ":")
						if emp_info == "Job Title":
							print("- ", employees[department][name][emp_info])
						else:
							for emp_detail in employees[department][name][emp_info]:
								print("- ", emp_detail)
					print("EMAIL:", email_formatted)
			else:
				print("Nothing found for this department :(")
		print("+", i, "total hits")


def scraper(company, titles_file):
	titles = []
	with open(titles_file) as f:
		for title in f.readlines():
			titles.append(title.rstrip())
	titled_employees = {}
	employees_dict = {}
	for title in titles:
		for response in crawl_employees(args.company, title):
			employees_dict = get_employees(soupify(response))
			titled_employees[title] = employees_dict
	return titled_employees

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='InDigger - A LinkedIn scraping tool by Matt Rotlevi')
	company = parser.add_argument_group(title="Company Name")
	company.add_argument('--company', metavar="string", help="Enter the company name you want to run the search on")
	empgroup = parser.add_argument_group(title="Employee Harvesting")
	empgroup.add_argument('--emps', metavar='file', \
	help="Discover employees by title and/or department. Titles and departments are imported from a new line delimited file.")
	empgroup.add_argument('--emailformat', metavar='string', \
	help="Create email addresses for discovered employees using a known format. (replace xyz with company name) [Accepted Formats: first.last@xyz.com, last.first@xyz.com, firstl@xyz.com, lfirst@xyz.com,\\ 		flast@xyz.com, lastf@xyz.com, first@xyz.com, last@xyz.com]")
	csv_file = parser.add_argument_group(title="CSV Output")
	csv_file.add_argument('--csv', metavar="string", help="[Optional - will print to terminal if not specified] Enter the csv output file name")


	if(len(sys.argv) == 1):
		parser.print_help()
		sys.exit(1)

	args = parser.parse_args()
	if not args.emps:
		print("You need to supply a file with titles associated with the company")
		sys.exit(1)
	if not args.company:
		print("You need to supply the company")
		sys.exit(1)
	if not args.emailformat:
		print("You need to supply an email address scheme")
		sys.exit(1)

	name_mailbox = get_name_mailbox(args.emailformat)

	if args.emailformat and name_mailbox not in format_list:
		print("You need to supply a valid email address scheme")
		sys.exit(1)

	if args.csv:
		correct = check_if_csv(args.csv)
		if not correct:
			print("You need to supply a valid csv format")
			sys.exit(1)

	stime = time.time()
	if(os.path.exists(os.path.abspath(args.emps))):
		scraped = scraper(args.company, args.emps)
		display(scraped, args.emailformat)

	else:
		print("Not a valid file location")
		sys.exit(1)

	print("\nCompleted in", time.time()-stime, "secs")
