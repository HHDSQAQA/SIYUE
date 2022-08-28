from lzma import FILTER_LZMA1
import os
import re

read_path='txt_processed'
save_path='txt_processeded'
if not os.path.exists(save_path):
    os.makedirs(save_path)

def merge(file1, file2):
    f1 = open(file1, 'a+', encoding='utf-8')
    with open(file2, 'r', encoding='utf-8') as f2:
        f1.write('\n')
        for i in f2:
            f1.write(i)

txts=[file for file in os.listdir(read_path) if re.search('\d+.+.txt$', file)]
for txt in txts:
    file2 = os.path.join(read_path,txt)
    file1 = os.path.join(save_path,'all.txt')
    merge(file1,file2)