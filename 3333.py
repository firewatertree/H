#顯示特定位置的字串&串接
user='mother fucker'
user=user[0:6]+user[7:]+" Nick Zhong"
personality="He is rude"
s3=user,personality
print(s3)
f="\nghi\nsadsadqw\nasdasda"
print(s3,f)
#查詢字串數量&或關鍵字是否出現在字串
pq="kjljlkjlkjljljlkjljlk"
len(pq)
pq.startswith('kjljlkjlkjljljlkjljlk')
print(len(pq))
print(pq.startswith('kjljlkjlkjljljlkjljlk'))
#字串拆解替換
sting='Elden ring is my favorite game'
