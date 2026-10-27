import sys,re
sys.stdout.reconfigure(encoding='utf-8')
from pathlib import Path
p=Path(__file__).resolve().parent/'texts'/sys.argv[1]
text=p.read_text(encoding='utf-8')
pages=re.split(r'===== PDF PAGE (\d+) =====',text)
start,end=map(int,sys.argv[2:4])
for i in range(1,len(pages),2):
 if start<=int(pages[i])<=end: print('\nPAGE '+pages[i]+'\n'+re.sub(r'\s+',' ',pages[i+1]))
