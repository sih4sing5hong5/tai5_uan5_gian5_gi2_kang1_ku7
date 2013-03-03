from 音標介面 import 音標介面

# 教會系羅馬音標聲調符號表 = dict(á = ('a', 2), à = ('a', 3), â = ('a', 5), ǎ = ('a', 6), ā = ('a', 7), a̍ = ('a', 8), a̋ = ('a', 9),
# é = ('e', 2), è = ('e', 3), ê = ('e', 5), ě = ('e', 6), ē = ('e', 7), e̍ = ('e', 8), e̋ = ('e', 9),
# í = ('i', 2), ì = ('i', 3), î = ('i', 5), ǐ = ('i', 6), ī = ('i', 7), i̍ = ('i', 8), i̋ = ('i', 9),
# ó = ('o', 2), ò = ('o', 3), ô = ('o', 5), ǒ = ('o', 6), ō = ('o', 7), o̍ = ('o', 8), ő = ('o', 9),
# ú = ('u', 2), ù = ('u', 3), û = ('u', 5), ǔ = ('u', 6), ū = ('u', 7), u̍ = ('u', 8), ű = ('u', 9),
# ḿ = ('m', 2), m̀ = ('m', 3), m̂ = ('m', 5), m̌ = ('m', 6), m̄ = ('m', 7), m̍ = ('m', 8), m̋ = ('m', 9),
# ń = ('n', 2), ǹ = ('n', 3), n̂ = ('n', 5), ň= ('n', 6), n̄ = ('n', 7), n̍ = ('n', 8), n̋ = ('n', 9),)
教會系羅馬音標聲調符號表 = {'á': ('a', 2), 'à': ('a', 3), 'â': ('a', 5), 'ǎ': ('a', 6), 'ā': ('a', 7), 'a̍': ('a', 8), 'a̋': ('a', 9),
'é': ('e', 2), 'è': ('e', 3), 'ê': ('e', 5), 'ě': ('e', 6), 'ē': ('e', 7), 'e̍': ('e', 8), 'e̋': ('e', 9),
'í': ('i', 2), 'ì': ('i', 3), 'î': ('i', 5), 'ǐ': ('i', 6), 'ī': ('i', 7), 'i̍': ('i', 8), 'i̋': ('i', 9),
'ó': ('o', 2), 'ò': ('o', 3), 'ô': ('o', 5), 'ǒ': ('o', 6), 'ō': ('o', 7), 'o̍': ('o', 8), 'ő': ('o', 9), 'ő': ('o', 9),
'ú': ('u', 2), 'ù': ('u', 3), 'û': ('u', 5), 'ǔ': ('u', 6), 'ū': ('u', 7), 'u̍': ('u', 8), 'ű': ('u', 9),
'ḿ': ('m', 2), 'm̀': ('m', 3), 'm̂': ('m', 5), 'm̌': ('m', 6), 'm̄': ('m', 7), 'm̍': ('m', 8), 'm̋': ('m', 9),
'ń': ('n', 2), 'ǹ': ('n', 3), 'n̂': ('n', 5), 'ň': ('n', 6), 'n̄': ('n', 7), 'n̍': ('n', 8), 'n̋': ('n', 9), 'ň' : ('n', 6), }

class 教會系羅馬音標(音標介面):
	聲 = None
	韻 = None
	調 = 1
	輕 = False
	音標 = None
	def 分析聲韻調(self, 音標):
		self.聲調符號表 = 教會系羅馬音標聲調符號表
		self.音標 = ''
# 		if 音標[0:2] == '--':
# 			音標 = 音標[2:]
# 			self.輕 = True
		一開始 = True
		for 字元 in 音標:
			if 一開始:
				字元 = 字元.lower()
				一開始 = False
			if 字元 == '.' and self.音標[-1:] == 'o':
				字元 = 'o'
			elif 字元 == 'o͘':
				字元 = 'oo'
			elif 字元 == 'N':
				字元 = 'nn'
			elif 字元 == 'ⁿ':
				字元 = 'nn'
			else:
				字元 = 字元.lower()
			self.音標 += 字元
		無調號音標 = ''
		前一字元 = ''
		前一音調 = ''
		愛結束矣 = False
		音標是著的 = True
		for 字元 in self.音標 :
# 			print(無調號音標 + '  ' + 前一字元 + '  ' + 字元)
			if 前一音調 == '1' and 字元 == '0':
				self.調 = 10
				愛結束矣 = True
			elif 字元.isnumeric():
				if self.調 == 1:
					self.調 = int(字元)
				else:
					音標是著的 = False
				愛結束矣 = True
				前一音調 = 字元
			elif 愛結束矣:
				音標是著的 = False
			elif 字元 in self.聲調符號表:
				無調字元 , self.調 = self.聲調符號表[字元]
				無調號音標 += 前一字元 + 無調字元
				前一字元 = ''
			elif 前一字元 + 字元 in self.聲調符號表:
				無調字元 , self.調 = self.聲調符號表[前一字元 + 字元]
				無調號音標 += 無調字元
				前一字元 = ''
# 			elif 無調號音標[-1:] + 前一字元 + 字元 in self.聲調符號表:
# 				無調字元 , self.調 = self.聲調符號表[前一字元 + 字元]
# 				無調號音標 = 無調號音標[:-1] + 無調字元
# 				前一字元 = ''
			else:
				無調號音標 += 前一字元
				前一字元 = 字元
		無調號音標 += 前一字元
# 		print(無調號音標)
		聲韻符合 = False
		for 聲母 in self.聲母表:
			for 韻母 in self.韻母表:
				if 聲母 + 韻母 == 無調號音標:
					self.聲 = 聲母
					self.韻 = 韻母
					聲韻符合 = True
		if not 聲韻符合:
			音標是著的 = False
		elif self.韻.endswith('p') or self.韻.endswith('t') or self.韻.endswith('k') or self.韻.endswith('h'):
			if self.調 == 1:
				self.調 = 4
			elif self.調 != 0 and self.調 != 4 and self.調 != 8 and self.調 != 10:
				音標是著的 = False
		self.調 = str(self.調)
		if 音標是著的:
			self.音標 = self.聲 + self.韻 + self.調
		else:
			self.音標 = None
		return self.音標
# 聲 介 韻 調，韻含元音跟韻尾

