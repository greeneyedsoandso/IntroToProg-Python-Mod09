#!/usr/bin/env python3
# ------------------------------------------------------------------------ #
# Title: Assignment 09
# Description: Working with Modules
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added pseudo-code to start assignment 9
# JDSmith,3.21.2020,Modified code to complete assignment 9
# ------------------------------------------------------------------------ #
if __name__ == "__main__":
    from DataClasses import Employee as Emp
    import ProcessingClasses as P  # processing classes
    import IOClasses as IO  # IO classes
else:
    raise Exception("This file was not created to be imported")
# Main Body of Script  ---------------------------------------------------- #
# Load data from file into a list of employee objects when script starts
str_filename = "EmployeeData.txt"
lstTable = []
lstFileData = P.FileProcessor.read_data_from_file(str_filename)
for line in lstFileData:
    lstTable.append(Emp(line[0], line[1], line[2].strip()))
while True:
    # Show user a menu of options
    IO.EmployeeIO.print_menu_items()
    # Get user's menu option choice
    choice = IO.EmployeeIO.input_menu_options()
    # Show user current data in the list of employee objects
    if choice == "1":
        IO.EmployeeIO.print_current_list_items(lstTable)
    # Let user add data to the list of employee objects
    elif choice == "2":
        try:
            obj_emp = IO.EmployeeIO.input_employee_data()
            lstTable.append(obj_emp)
        except Exception as e:
            print(str(e))
    # let user save current data to file
    elif choice == "3":
        P.FileProcessor.save_data_to_file(str_filename, lstTable)
    # Let user exit program
    elif choice == "4":
        break
# Main Body of Script  ---------------------------------------------------- #
