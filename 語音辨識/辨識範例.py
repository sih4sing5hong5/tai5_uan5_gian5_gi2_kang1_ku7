import os
from 語音辨識.辨識模型 import 辨識模型

if __name__ == '__main__':
	模型 = 辨識模型()
	這馬目錄 = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
	資料目錄 = os.path.join(這馬目錄, 'data')
	音檔目錄 = os.path.join(這馬目錄, 'wav')
	標仔目錄 = os.path.join(這馬目錄, 'labels')
	音節聲韻對照檔 = os.path.join(這馬目錄, 'Syl2Monophone.dic.ok')
	執行檔路徑 = ''
	聲韻類檔, 模型檔 = 模型.訓練(
		音檔目錄, 標仔目錄, 音節聲韻對照檔, 資料目錄,
		算特徵=False, 執行檔路徑=執行檔路徑)
	特徵檔, 音節檔, 聲韻檔 = 模型.處理試驗語料(音檔目錄, 資料目錄, 標仔目錄, 音節聲韻對照檔, 執行檔路徑=執行檔路徑)
	對齊聲韻結果檔 = 模型.對齊聲韻(聲韻類檔, 模型檔, 聲韻檔, 特徵檔, 資料目錄, 執行檔路徑=執行檔路徑)
	對齊音節結果檔 = 模型.對齊音節(音節聲韻對照檔, 聲韻類檔, 模型檔, 音節檔, 特徵檔, 資料目錄, 執行檔路徑=執行檔路徑)
	模型.辨識聲韻(聲韻類檔, 模型檔, 特徵檔, 資料目錄, 3, 執行檔路徑=執行檔路徑)
	模型.辨識音節(音節聲韻對照檔, 聲韻類檔, 模型檔, 特徵檔, 資料目錄, 3, 執行檔路徑=執行檔路徑)
