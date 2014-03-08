"""
著作權所有 (C) 民國102年 意傳文化科技
開發者：薛丞宏
網址：http://意傳.台灣
語料來源：請看各資料庫內說明

本程式乃自由軟體，您必須遵照SocialCalc設計的通用公共授權（Common Public Attribution License, CPAL)來修改和重新發佈這一程式，詳情請參閱條文。授權大略如下，若有歧異，以授權原文為主：
	１．得使用、修改、複製並發佈此程式碼，且必須以通用公共授權發行；
	２．任何以程式碼衍生的執行檔或網路服務，必須公開該程式碼；
	３．將此程式的原始碼當函式庫引用入商業軟體，且不需公開非關此函式庫的任何程式碼

此開放原始碼、共享軟體或說明文件之使用或散佈不負擔保責任，並拒絕負擔因使用上述軟體或說明文件所致任何及一切賠償責任或損害。

臺灣言語工具緣起於本土文化推廣與傳承，非常歡迎各界用於商業軟體，但希望在使用之餘，能夠提供建議、錯誤回報或修補，回饋給這塊土地。

感謝您的使用與推廣～～勞力！承蒙！
"""
from 臺灣言語工具.字詞組集句章.解析整理工具.型態錯誤 import 型態錯誤
from 臺灣言語工具.字詞組集句章.基本元素.詞 import 詞

class 組:
	內底詞 = None
	def __init__(self, 詞陣列 = []):
		if not isinstance(詞陣列, list):
			raise 型態錯誤('傳入來的詞陣列毋是陣列：{0}'.format(str(詞陣列)))
		self.內底詞 = []
		for 詞物件 in 詞陣列:
			if not isinstance(詞物件, 詞):
				raise 型態錯誤('詞陣列內底有毋是詞的：詞陣列＝{0}，詞物件＝{1}'.format(str(詞陣列), str(詞物件)))
			self.內底詞.append(詞(詞物件.內底字))
	def __eq__(self, 別个):
		return isinstance(別个, 組) and self.內底詞 == 別个.內底詞
	def __hash__(self):
		return hash(tuple(self.內底詞))
	def __str__(self):
		return '組：{0}'.format(self.內底詞)
	def __repr__(self):
		return self.__str__()
