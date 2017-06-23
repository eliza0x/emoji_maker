import os
import collections
import json
import sys

from char_set import alphabet, katakana, hiragana,  mark
from char_set import kanji1, kanji2, kanji3, kanji4, kanji5, kanji6

def append_dic(dic, pre, char_set):
    print("create dic:" + pre)
    count = collections.defaultdict(lambda: 0)
    for (value, key) in char_set:
        if count[value] == 0:
            dic[value] = pre+ key
        else:
            dic[value] = pre + key + str(count[value])
        count[value] = count[value] + 1
    print("done:" + pre)
    return dic

dic = {}
json_path = "char_set.json"
if os.path.exists(json_path):
    with open(json_path, mode='r') as f:
        dic = json.load(f)
else: 
    print(json_path + " is not found...")
    dic = append_dic(dic, "l", alphabet.alpha)
    dic = append_dic(dic, "u", alphabet.ualpha)
    dic = append_dic(dic, "k", katakana.katakana)
    dic = append_dic(dic, "j", hiragana.hiragana)
    dic = append_dic(dic, "m", mark.mark)
    dic = append_dic(dic, "kanji_", kanji1.kanji1)
    dic = append_dic(dic, "kanji_2_", kanji2.kanji2)
    dic = append_dic(dic, "kanji_3_", kanji3.kanji3)
    dic = append_dic(dic, "kanji_4_", kanji4.kanji4)
    dic = append_dic(dic, "kanji_5_", kanji5.kanji5)
    dic = append_dic(dic, "kanji_6_", kanji6.kanji6)
    with open(json_path, mode='w') as f:
        json.dump(dic, f)

out = ""
args = sys.argv
for char in list(args[1]):
    emoji =  dic.get(char, "not found")
    if emoji != "not found":
        out = out + ":" + emoji + ":"
    else:
        out = out + char
print(out)

