import os
import json
from tqdm import tqdm

def make_emoji(file_name: str, text: str):
    os.system(
      "convert -pointsize 140" +
      " -font /usr/share/fonts/TTF/mplus-1c-black.ttf" +
      " -annotate 0 " + str(text) +
      " -gravity center -fill black -size 128x128 xc:none"  +
      " out/" + str(file_name) + ".png"
      )

if __name__ == '__main__':
    os.system("mkdir out")
    with open("json/alpha.json", "r") as file:
        alpha_list = json.load(file)
        for char in tqdm(alpha_list):
            make_emoji('zzz_'+char, char)

    with open("json/hiragana.json", "r") as file:
        kana_list = json.load(file)
        for char in tqdm(kana_list):
            make_emoji(char, char)

    with open("json/jis1.json", "r") as file:
        kanji_list = json.load(file)
        for char in tqdm(kanji_list):
            make_emoji(char, char)

    with open("json/katakana.json", "r") as file:
        katakana_list = json.load(file)
        for char in tqdm(katakana_list):
            make_emoji(char, char)

