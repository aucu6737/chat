
lines = []
with open('3.txt', 'r', encoding = 'utf-8-sig') as f:
	for line in f:
		lines.append(line.strip())

for line in lines:
	s = line.split(' ')
	time = s[0][:5] # time是s[0]的第1個字母到第5個字母 (01234)
	name = s[0][5:]
	print(name)

# 因為python也可以把清單中的項目當成子清單，把項目中的所有字母當成子項目，所以可以直接按字母長度取出 (但不能分割)