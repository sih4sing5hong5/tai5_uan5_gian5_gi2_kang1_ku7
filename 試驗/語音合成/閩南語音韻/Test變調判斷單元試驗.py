# -*- coding: utf-8 -*-
from unittest.case import TestCase
from 臺灣言語工具.解析整理.拆文分析器 import 拆文分析器
from 臺灣言語工具.語音合成.閩南語變調 import 閩南語變調
from 臺灣言語工具.基本物件.句 import 句
from 臺灣言語工具.基本物件.公用變數 import 標點符號
from 臺灣言語工具.音標系統.閩南語.臺灣閩南語羅馬字拼音 import 臺灣閩南語羅馬字拼音


class 變調判斷單元試驗(TestCase):
    def test_句尾變調(self):
        章物件 = self.產生套用前物件('我愛媠媠', 'gua2 ai3 sui2-sui2')
        self.assertEqual(
            變調判斷.判斷(章物件),
            [實詞變調, 實詞變調, 實詞變調, 維持本調]
        )

    def test_仝詞攏輕聲(self):
        章物件 = self.產生套用前物件('我愛媠媠', 'gua2 ai3 0sui2-sui2')
        self.assertEqual(
            變調判斷.判斷(章物件),
            [實詞變調, 實詞變調, 實詞變調, 維持本調, '愛閣確定']
        )

    def test_的前無變調(self):
        章物件 = self.產生套用前物件(
            '我上愛媠媠的姑娘',
            'gua2 siong7 ai3 sui2-sui2 e5 koo1-niu5'
        )
        self.assertEqual(
            變調判斷.判斷(章物件),
            [實詞變調, 實詞變調, 實詞變調, 實詞變調, 維持本調, 實詞變調, 實詞變調, 維持本調]
        )

    def test_的前代名詞變調(self):
        章物件 = self.產生套用前物件(
            '我的媠媠',
            'gua2 e5 sui2-sui2'
        )
        self.assertEqual(
            變調判斷.判斷(章物件),
            [實詞變調, 實詞變調, 實詞變調, 維持本調]
        )

    def test_井前無變調(self):
        章物件 = self.產生套用前物件('我#愛媠媠', 'gua2 # ai3 sui2-sui2')
        self.assertEqual(
            變調判斷.判斷(章物件),
            [維持本調, 愛提掉的, 實詞變調, 實詞變調, 維持本調]
        )

    def test_標點符號句尾變調(self):
        章物件 = self.產生套用前物件('我愛媠媠。', 'gua2 ai3 sui2-sui2 .')
        self.assertEqual(
            變調判斷.判斷(章物件),
            [維持本調, 實詞變調, 實詞變調, 維持本調, 標點符號]
        )

    def 產生套用前物件(self, 漢字, 臺羅):
        return (
            拆文分析器.對齊章物件(漢字, 臺羅)
            .轉音(臺灣閩南語羅馬字拼音)
            .轉音(臺灣閩南語羅馬字拼音, 函式='音值')
        )
