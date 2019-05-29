import numpy as np


scoretype = np.dtype({
  'names':['name','chinese','english','math'],
  'formats': ['U32','i','i','i'] 
})

scorelist = np.array([
  ('張飛',66,65,30),
  ('關羽',95,85,98),
  ('趙雲',93,92,96),
  ('黃忠',90,88,77),
  ('典韋',80,90,90),
],dtype = scoretype)

studentName = scorelist['name']
chineseScore = scorelist['chinese']
englishScore = scorelist['english']
mathScore = scorelist['math']

def show(name,cj):
  print('{} | {} | {} | {} | {} | {} '
  .format(name,np.mean(cj),np.min(cj),np.max(cj),np.var(cj),np.std(cj)))

print("科目 | 平均成绩 | 最小成绩 | 最大成绩 | 方差 | 標準差")
show("中文", chineseScore)
show("英語", englishScore)
show("數學", mathScore)

print("排名:", end='')
ranking = sorted(scorelist,key=lambda x:x[1]+x[2]+x[3], reverse=True)

for row in ranking:
  print(row[0], end='|')