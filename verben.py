import openpyxl
from pathlib import Path

input_file='Grammer_Verven_Wort.xlsx'
verven_tab='Verben'

xlsx_file = Path(input_file)
wb_obj = openpyxl.load_workbook(xlsx_file) 

vbn_sheet = wb_obj[verven_tab]
print("========= start =========")
row_count = 1
prepend_first = 1
default_first = prepend_first+1
default_last = 30

input_first_row = input("select first row number:")
input_last_row = input("select last row number:")

if input_first_row != "" and input_first_row != 0 :
	input_first_row = int(input_first_row)
else:
	input_first_row = default_first
	
if input_last_row != "" and input_last_row != 0 :
	input_last_row = int(input_last_row) - 1
else:
	input_last_row = default_last


for row in vbn_sheet.iter_rows(values_only=True,
								min_row= int(input_first_row) ,
								max_row= int(input_last_row),
								max_col=3):
	print("##### row:"+str(row_count))
	while True:	
		score = 0	
		print("INFINITIV:"+row[0])
		ptr = input("PRÄTERITUM:")
		ptz = input("PARTIZIPII:")
		
		ptr = ptr.replace(" ","")
		ptz = ptz.replace(" ","")
		
		if ptr != row[1].replace(" ",""):
			print("NIEN!! PRÄTERITUM="+row[1])
		else:
			print("Correct!")
			score = score + 1
			
		if ptz != row[2].replace(" ",""):
			print("NIEN!! PARTIZIPII="+row[2])
		else:
			print("Correct!")
			score = score + 1
		
		if score == 2 : break
			
		next = input("Next?(y)/(n):") 
		
		if next != ("n") or next != ("N"):
			break
		else:
			continue
			
	row_count=row_count+1
		