# -*- coding: utf-8 -*-
from 臺灣言語工具.系統整合.程式腳本 import 程式腳本
import os
from 臺灣言語工具.系統整合.外部程式 import 外部程式

_外部程式目錄=外部程式().目錄()
class 安裝摩西翻譯佮相關程式(程式腳本):
	def 安裝moses(self, mgiza安裝路徑=_外部程式目錄):
		with self._換目錄(mgiza安裝路徑):
			self._走指令('git clone --depth 1 https://github.com/sih4sing5hong5/mosesdecoder.git')
			moses程式碼目錄=os.path.join(mgiza安裝路徑,'mosesdecoder')
			with self._換目錄(moses程式碼目錄):
				self._走指令('./bjam -j2')
	def 安裝mgiza(self, mgiza安裝路徑=_外部程式目錄):
		with self._換目錄(mgiza安裝路徑):
			self._走指令('git clone --depth 1 https://github.com/moses-smt/mgiza.git')
			mgiza程式碼目錄=os.path.join(mgiza安裝路徑,'mgiza','mgizapp')
			with self._換目錄(mgiza程式碼目錄):
				self._走指令('cmake .')
				self._走指令('make')
				self._走指令('make install')
