
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
	# 有時候txt之類的檔案存檔的時候會存一些編碼的資料，導致會印出亂碼，例如本例會跑出'\ufeff'，就需要在'utf-8'後面加上'sig'

def convert(lines):
	new = []
	person = None # 先宣告person為"無"，是一個預設值，先對person做宣告，後面可以防當機
	for line in lines:
		if line == 'Allen':
			person = 'Allen'
			continue
		elif line == 'Tom':
			person = 'Tom'
			continue
		# 用continue來控制person等於誰，並且會跳過人名那行，下一行就會是把上面的名字加上對話加入清單
		if person: # 如果person有值，不是虛無的，才會運行，防止person沒有被宣告會當機的狀況
			new.append(person + ': ' + line)
	return new

def write_file(filename, lines): # 此處的輸入值是產出檔案的檔名
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('input.txt')
	lines = convert(lines)
	write_file('output.txt', lines) 

main()