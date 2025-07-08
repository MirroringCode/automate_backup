from pathlib import Path
import os
from datetime import date
import calendar
import locale

locale.setlocale(locale.LC_ALL, '')

STANDARD_DIRECTORIES = {
    'root': 'C:\\Users\\mdmartinez\\Desktop\\RESPALDOS SISTEMAS CEBM\\',
    
}

CURRENT_DATE = date.today()
MONTH = calendar.month_name[CURRENT_DATE.month]

target_directory = 'C:\\Users\\mdmartinez\\Desktop\\RESPALDOS SISTEMAS CEBM\\'



print(Path.cwd())

os.chdir(target_directory)
if(not os.path.isdir(f"{MONTH}_{CURRENT_DATE}")):
    print(f"Creating directory: RESPALDO_{MONTH}_{CURRENT_DATE}")
    os.mkdir(f"{MONTH}_{CURRENT_DATE}")

if(not os.path.isdir('sia')):
    print("Creating directory: sia")
    os.mkdir('sia')



print(Path.cwd())





