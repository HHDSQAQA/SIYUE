import re,os,json

read_path='scn'
save_path='scn_processed'

if not os.path.exists(save_path):
    os.makedirs(save_path)

files_to_read=[file for file in os.listdir(read_path) if re.search('\d+.+.json$', file)]

for file_name in files_to_read:
    #获取章节名
    ch_name=re.search('(^.+)ver\d\.\d+\.ks.json$', file_name)
    if ch_name:
        ch_name=ch_name.group(1)
    else:
        ch_name=re.search('(^.+)\.ks.json$', file_name).group(1)
    print(ch_name)
    #读取台词
    if ch_name not in os.listdir(save_path):
        os.makedirs(f'{save_path}/{ch_name}')
    with open(f'scn/{file_name}','r',encoding='utf-8') as file:
        data=json.load(file)
        for scene in data['scenes']:
            if 'texts' not in scene.keys(): continue
            #统一成全角空格
            chapter=re.search('([a-zA-Z]+)\s+(\d+-\d+)',scene['title'])
            if chapter:
                chapter_name=chapter.group(1)+'\u3000'+chapter.group(2)
            else:
                chapter_name=scene['title']
            with open(f'{save_path}/{ch_name}/{chapter_name}.txt','a',encoding='utf-8') as scenario:
                for text in scene['texts']:
                    if text[3]:
                        line=text[3][0]['voice']
                    else:
                        line='null'
                    line+='｜'
                    if text[0]:
                        line+=text[0]
                    else:
                        line+='null'
                    line+='｜'+re.sub(r'(\\n)|\s|(%\d*;)','',text[2])+'\n'
                    scenario.write(line)