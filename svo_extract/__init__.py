name = "extract_svo"
from ckiptagger import data_utils, construct_dictionary, WS, POS, NER


class svo():
    def __init__(self):
        try:
            self.ws = WS("./data")
            self.pos = POS("./data")
        except FileNotFoundError:
            print("Downloading data set....")
            data_utils.download_data_gdown("./") # gdrive-ckip
            print("Done")
            self.ws = WS("./data")
            self.pos = POS("./data")

    
    def find_word(self, w_list, pos_list, target = "N",back=True):
        """
        從尾/頭開始尋找某個連續詞性的詞語
        
        w_list: 斷詞完的list
        pos_list: 詞性list，長度需和w_list相同
        target: "N" 或 "V"
        back: 
            + True: 從尾部搜尋
            + False: 從頭部搜尋

        回傳：
            詞語(str), 開始位置(in w_list)(int), 結束位置

        """
        # 前處理一些詞語
        preprocess_list = ["Neu","Nf","VH"]
        for _pre in preprocess_list:
            pos_list = list(map(lambda x: "x" if x==_pre else x, pos_list))

        if back:
            N_index = [index for index, item in enumerate(pos_list) if target in item]
            # print(N_index)
            N_s = len(N_index)-1
            for i in range(len(N_index)-1, 0, -1):
                if N_index[i-1] == N_index[i] - 1:
                    N_s -= 1
                else:
                    break
            # print(N_s)
            # print(N_index[N_s:])
            index_i = N_index[N_s]
            index_f = N_index[-1]
            return "".join( w_list[ index_i: index_f+1 ] ), index_i, index_f
        else:
            N_index = [index for index, item in enumerate(pos_list) if target in item]
            # print(N_index)
            N_e = 0
            for i in range(1,len(N_index)):
                if N_index[i-1] == N_index[i] - 1:
                    N_e += 1
                else:
                    break
            # print(N_e)
            index_i = N_index[0]
            index_f = N_index[N_e]
            return "".join( w_list[ index_i: index_f+1 ] ), index_i, index_f

    def extract(self, w_list, pos_list):
        # 被動式
        if "P" in pos_list:
            Pi = pos_list.index("P")
            O, Oi, Oj = self.find_word(w_list[:Pi], pos_list[:Pi], "N", True)
            w_list = w_list[Pi+1:]
            pos_list = pos_list[Pi+1:]
            S, Si, Sj = self.find_word(w_list, pos_list, "N", False)
            w_list = w_list[Sj+1:]
            pos_list = pos_list[Sj+1:]
            V, Vi, Vj = self.find_word(w_list, pos_list, "V", False)
            pass
        # 主動式
        else:
            O, Oi, Oj = self.find_word(w_list, pos_list, "N", True)
            w_list = w_list[:Oi]
            pos_list = pos_list[:Oi]
            V, Vi, Vj = self.find_word(w_list, pos_list, "V", True)
            w_list = w_list[:Vi]
            pos_list = pos_list[:Vi]
            S, Si, Sj = self.find_word(w_list, pos_list, "N", True)
        return S,V,O

    def sent2svo(self, sent):
        sent_list = [sent]
        ws_list = self.ws(sent_list)
        pos_list = self.pos(ws_list)

        ws_list, pos_list = ws_list[0], pos_list[0]
        for _word, _pos in zip(ws_list, pos_list):
            print(_word, _pos)

        return extract(ws_list, pos_list)
    
    def svo(self, sent_list):
        ws_list_list = self.ws(sent_list)
        pos_list_list = self.pos(ws_list_list)
        svo_list = []
        for ws_list, pos_list in zip(ws_list_list, pos_list_list):
            print("-"*10)
            for _word, _pos in zip(ws_list, pos_list):
                print(_word, _pos)
            print("\n\n")
            svo_list.append(self.extract(ws_list, pos_list))
        return svo_list
    