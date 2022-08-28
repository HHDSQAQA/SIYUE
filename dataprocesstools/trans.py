import sys
import os
import re

read_allpath=os.listdir()
save_path='txt_processed'
n = 0

if not os.path.exists(save_path):
    os.makedirs(save_path)

for read_path in read_allpath:
    files_to_read=[file for file in os.listdir(read_path) if re.search('\d+.txt$', file)]

    lineList = []
    matchPattern = re.compile(r'null|%|子宮|「……」|～～っ|ぁっ|……っ|】|ぁ、ぁ|膣|愛液|ぅっ|さ……っ|んん|ぁ～|中に|ん……')

    for file_name in files_to_read: 
        n = n + 1
        with open(f'{read_path}/{file_name}','r',encoding='utf-8') as file:  
            while 1:
                line = file.readline()
                if not line:
                    print("Read file End or Error")
                    break
                elif matchPattern.search(line):
                    pass
                else:
                    lineList.append(line)
            file.close()
            
            exp_path = os.path.join(save_path,str(n)+f'{file_name}')
            with open(f'{exp_path}', 'w',encoding='UTF-8') as file:
                for i in lineList:
                    file.write(i)
                file.close()








