import pandas as pd
import os
from formatter import *
import csv

def csv_output(employees, emailformat, filename):
    columns = ["Department", "Name", "Education", "Experience", "Job Title", "Email"]
    df = pd.DataFrame(employees, columns=columns)
    big_list = []

    for department, value in employees.items():
        if employees[department] is not None:
            for name, value in employees[department].items():
                list = []
                big_list.append(list)
                list[:] = []
                list.append(department)
                list.append(name)
                for emp_info, value in employees[department][name].items():
                    if emp_info == "Job Title":
                        list.append(''.join(employees[department][name][emp_info]))
                    else:
                        if emp_info == "Education":
                            list.append(' , '.join(employees[department][name][emp_info]))
                        elif emp_info == "Experience":
                            list.append(' , '.join(employees[department][name][emp_info]))
                email_formatted = email_formatter(name, emailformat)
                list.append(email_formatted)
        else:
            print("nothing found for department", employees[department])


    for i in range(len(big_list)):
        df.loc[i] = big_list[i]

    df.to_csv(os.path.abspath(filename))

    print("CSV Output Success - filename:", filename)
