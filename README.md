# svo-extract
利用CKIP套件將句子中的核心結構抓出(主詞S，動詞V，受詞O)

## 安裝及使用
### 使用pip安裝
```bash
pip install svo-extract
```

### 使用方式
```python
from svo_extract import svo

SVO = svo()
SVO.svo(sent_list=sentence_list)

sentence_list = [
    "我看見小豬殺了他爸爸",
    "我買了一杯大杯的珍珠奶茶",
    "包子被我吃掉了",
]

SVO.svo(sent_list=sentence_list)
```


輸出：
```
[('豬', '殺', '他爸爸'), ('我', '買', '珍珠奶茶'), ('我', '吃掉', '包子')]
```


## 目的
將句子中的核心主體元素提取出來，而根據所需場景的情況下有絕大多數情況可以透過核心三元素——動作主體、動作、動作客體這三個來表達。


## 方法
使用[CKIP](https://ckip.iis.sinica.edu.tw/)中的POS方式將輸入句子進行詞性標注，之後根據句子主被動格式區分不同提取方式
