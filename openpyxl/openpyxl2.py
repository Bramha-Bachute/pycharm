from openpyxl import workbook, load_workbook

wb = load_workbook("D:\My Videos\Programming Language\Python\Library\Hindi\Openpyxl Hindi 1 Excel automation using python\Insurance Data.xlsx")

print(wb.sheetnames)

#Remove the sheets
'''
wb.remove(wb['Instructions'])
wb.remove(wb['Sheet1'])
'''

ws = wb['PolicyData']

ws1 = wb.create_sheet("Filtered Data")

'''
for row in ws.values:
    if row[6]=='Frame' or row[6]=='Construction':
        ws1.append(row)
        
'''


#Move range of data

#Insert Excel formula from python

for i in range(ws.max_row):
    for j in range(ws.max_column):
        c = ws.cell(i+1,j+1).value
        ws1.cell(i+1, j+1).value = c
        ws1.cell(i+1,11).value = "=_xlfn.CONCAT(C{},D{},E{})".format(i+1, i+1, i+1)

#Merge Cells
'''
ws1.merge_cells(start_row=1,end_row=10,start_column=12, end_column=15)
ws1.unmerge_cells("K1:M1")

'''

# Hide and Unhide

ws1.row_dimensions.group(1,10,1,False)
ws1.column_dimensions.group("A","J",5,True)




# Insert, Delete Rows or column
'''

ws1.move_range("A1:J501",5,2)
ws1.insert_rows(5,5)
ws1.delete_rows(5,5)
ws1.insert_cols(3,5)
ws1.delete_cols(3,5)
'''

wb.save("D:\My Videos\Programming Language\Python\Library\Hindi\Openpyxl Hindi 2 Excel Data Manipulation using Python\Test.xlsx")