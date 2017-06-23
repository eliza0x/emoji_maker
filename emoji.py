import os
import collections
import json
from pykakasi import kakasi
from tqdm import tqdm

from char_set import mark

def make_emoji(file_name: str, text: str):
    os.system(
      "convert -pointsize 140" +
      " -font /usr/share/fonts/TTF/Mplus1p-Black.ttf" +
      " -annotate 0 " + str(text) +
      " -gravity center -fill black -size 128x128 xc:none"  +
      " out/" + str(file_name) + ".png"
      )

def create_img(pre ,data, tail=False):
    count = collections.defaultdict(lambda: 0)
    for key, value in tqdm(data):
        if tail:
            make_emoji(pre+key+"_"+str(count[key]) , value)
        else:
            make_emoji(pre+key , value)
        count[key] = count[key] + 1

def add_romaji(list):
    pairs = []
    conv = kakasi()
    conv.setMode('H', 'a')
    conv.setMode('K', 'a')
    conv.setMode('J', 'a')
    conv = conv.getConverter()
    for kanji in list:
        romaji = conv.do(kanji)
        pairs.append((romaji, kanji))
    return pairs

def lowerPair(list):
    pair = []
    for char in list:
        pair.append((str(char), str(char)))
    return pair

def upperPair(list):
    pair = []
    for char in list:
        pair.append((str(char), str(char).upper()))
    return pair

if __name__ == '__main__':
    os.system("mkdir out")
    with open("json/alpha.json", "r") as file:
        list = json.load(file)
        pairs_l = lowerPair(list)
        pairs_u = upperPair(list)
        create_img("l" , pairs_l)
        create_img("u" , pairs_u)
    with open("json/jis1.json", "r") as file:
        list = json.load(file)
        pairs = add_romaji(list)
        create_img("kanji_" , pairs, True)
    with open("json/hiragana.json", "r") as file:
        list = json.load(file)
        pairs = add_romaji(list)
        create_img("h" , pairs)
    with open("json/katakana.json", "r") as file:
        list = json.load(file)
        pairs = add_romaji(list)
        create_img("k" , pairs)
    create_img("m" , mark.mark)

