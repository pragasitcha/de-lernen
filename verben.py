import openpyxl
from pathlib import Path

input_file='Grammer_Verven_Wort.xlsx'
verven_tab='Verben'

xlsx_file = Path(input_file)
wb_obj = openpyxl.load_workbook(xlsx_file) 

vbn_sheet = wb_obj[verven_tab]
print("========= start =========")
row_count = 1

for row in vbn_sheet.iter_rows(values_only=True,
								min_row=2,
								max_row=3,
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
			
	row_count=row_count+1
		