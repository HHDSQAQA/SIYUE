# scenario.py
功能:将{read_path}(default=./scn)中`json`格式剧本中的文本数据提取出来
生成的文件名格式为./{save_path}/{ch_name}/{chapter_name}.txt
文件内容是{voice}|{character}|{content}
## 常见问题
- 如遇`txt.json` 文件自行将代码中`ks.json`->`txt.json`
- 生成文件名为`.txt` 则在`with open(f'{save_path}/{ch_name}/{chapter_name}.txt','a',encoding='utf-8') as scenario:`的`{chapter_name}`后面随意加个文件名
- **原作者是谁我忘了，真的大佬**
  
# trans.py
功能:自动去除上一个文件生成的文本中的**部分**HS，无语音句子和无法被vits读取的内容（例如`%F`）~~ *欢迎提issue，pr完善去H计划* ~~
若要自定义请更改Line 16的正则

# merge.py
功能：将trans.py的产物合成为一个文件
**注意**：要手动创建`{save_path}/all.txt` 且在对生成文件运行`preprocess.py`前要检查内容，删除空行
