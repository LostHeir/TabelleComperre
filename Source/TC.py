import xlrd, sys, os

def open_file(path):
    # Open Excel file for reading
    wb = xlrd.open_workbook(path)
    # Get sheets
    sheet_comp = wb.sheet_by_index(0) #Table to Compare
    sheet_template = wb.sheet_by_index(1) #Template Table
    # List of changes definition
    ListOfChanges = []

    # Get row to compare with tempalte table
    for Comp_row_num in range(sheet_comp.nrows):
        Comp_row_value = sheet_comp.row_values(Comp_row_num)
        # Setting flag
        is_present = False

        # Compare selected row with template table
        for Temp_row_num in range (sheet_template.nrows):
            Temp_row_value = sheet_template.row_values(Temp_row_num)

            # If selected row is located in tamplate table - set the flag
            if Comp_row_value == Temp_row_value:
                is_present = True

        # If selected row is not located in template table - add it to the list
        if not  is_present:
            ListOfChanges.append(Comp_row_value)
            print (Comp_row_value) # to show in terminal, just for test
    
    # Write ListOfChanges to the Result.txt
    with open(filepath, 'w') as file_handler:

        if ListOfChanges == []:
            file_handler.write("No changes")
        else:
            file_handler.write("Differences:\n")
            for item in ListOfChanges:
                file_handler.write(f"{item}\n")

                       
# #### #
# MAIN #
# #### #             
if __name__ == "__main__":
    path = (os.path.dirname(sys.argv[0]) + r"\TabelleComperre.xlsx")
    filepath = (os.path.dirname(sys.argv[0]) + r"\Result.txt")
    open_file(path)
    print ("END") # to show in terminal, just for test