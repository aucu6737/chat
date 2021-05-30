
def read_file(filename):
	lines = []
	with open(filename, 'r', encoding = 'utf-8-sig') as f:
		for line in f:
			lines.append(line.strip())
	return lines
	# 有時候txt之類的檔案存檔的時候會存一些編碼的資料，導致會印出亂碼，例如本例會跑出'\ufeff'，就需要在'utf-8'後面加上'sig'

def convert(lines):
	allen_word_count = 0
	viki_word_count = 0
	allen_sticker_count = 0
	viki_sticker_count = 0
	allen_image_count = 0
	viki_image_count = 0
	for line in lines:
		s = line.split(' ') # 用空格拆分之後，放入s這個子清單，s0是時間，s1是名字，s2是對話
		time = s[0]
		name = s[1]
		if name == 'Allen':
			if s[2] == '貼圖':
				allen_sticker_count += 1 # 貼圖計數+1
			elif s[2] == '圖片':
				allen_image_count += 1
			else:
				for msg in s[2:]: #s[2]之後的每一項，也就是所有對話
					allen_word_count += len(msg)
		elif name == 'Viki':
			if s[2] == '貼圖':
				viki_sticker_count += 1
			elif s[2] == '圖片':
				viki_image_count += 1
			else:
				for msg in s[2:]: #s[2]之後的每一項，也就是所有對話
					viki_word_count += len(msg)
	print('Allen said', allen_word_count, 'words')
	print('Allen sent', allen_sticker_count, 'stickers')
	print('Allen sent', allen_image_count, 'images')
	print('Viki said', viki_word_count, 'words')
	print('Viki sent', viki_sticker_count, 'stickers')
	print('Viki sent', viki_image_count, 'images')


	
	# 但對話中可能有多餘的空格，例如第一句，所以不只是s[2]，還會被拆成更多塊，需要把s[2]後面全部加起來，python內就是
		# 舉例：n = [2, 6 ,6, 8, 4]
		# 用冒號表示前幾個，n[:3]表示0:3，也就是從0開始(包含)到3(不含)結束，此案例為012也就是[2, 6, 6]
		# 舉例 s[2:4] 表示 從2開始(包含)到4(不含)結束，此案例為23也就是[6, 8]
		# 舉例：倒數 s[-2:]，從倒數第2開始，結束值不寫就代表數到底，本案例為34也就是[8, 4]

def write_file(filename, lines): # 此處的輸入值是產出檔案的檔名
	with open(filename, 'w') as f:
		for line in lines:
			f.write(line + '\n')

def main():
	lines = read_file('LINE-Viki.txt')
	lines = convert(lines)
	#write_file('output2.txt', lines) 

main()