# python 3.8
import os,re
from pathlib import Path
import frozen_dir

#  pip install xlsxwriter
import xlsxwriter

# iteratre txt files' names
dir_path = frozen_dir.app_path()
path = dir_path + "/data/"
file_names = os.listdir(path)

# get all data
file_data = []
for file_name in file_names:
    # add prefix path
    file_name = path + file_name
    # regex
    f = open(file_name, "r", encoding='utf-8')
    data = f.read()
    f.close()
    pattern = re.compile(r'\d{1,4}\t\d{1,4}.\d{1,4}\t\n')
    matchObj = pattern.findall(data)
    file_data = file_data + matchObj

# get all number from data
nums = []
for line in file_data:
    pos = [pos for pos, char in enumerate(line) if char == '\t']
    num = line[pos[0]+1:pos[1]]
    nums = nums + [num]

# create excel
output_name = dir_path + '/results.xlsx'
my_file = Path(output_name)
if my_file.is_file():
    raise RuntimeError('Already exist file: "results.xlsx"')
else:
    workbook = xlsxwriter.Workbook(output_name)

# writing data to excel
worksheet = workbook.add_worksheet()
worksheet.write('A1', 'No.')
worksheet.write('B1', 'Value')
for i in range(0,len(nums)):
    worksheet.write('A'+str(i+2), str(i+1))
    worksheet.write('B'+str(i+2), nums[i])
    
# close the excel
workbook.close()
print("Finished!")
