import os
import collections
from tqdm import tqdm

from char_set import alphabet, katakana, hiragana,  mark
from char_set import kanji1, kanji2, kanji3, kanji4, kanji5, kanji6

def make_emoji(path: str, file_name: str, text: str):
    os.system(
      "convert" +
      " -pointsize 140" +
      " -font /usr/share/fonts/TTF/Mplus1p-Black.ttf" +
      " -annotate 0"  +
      " " + str(text) + " " +
      " -gravity center" +
      " -fill black -size 128x128 xc:none"  +
      " " + str(path) + "/" + str(file_name) + ".png"
      )

def create_img(path ,pre ,data):
    os.system("mkdir " + path)
    already = collections.defaultdict(lambda: 0)
    cnt = 0
    for char_data in tqdm(data):
        key = char_data[0]
        value = char_data[1]
        if(0<already[value]):
            value= value + str(already[value])
        make_emoji(path, pre+value, key)

os.system("mkdir " + "Out")
create_img("Out/Lower"    , "l"        , alphabet.alpha    )
create_img("Out/Upper"    , "u"        , alphabet.ualpha   )
create_img("Out/Hiragana" , "j"        , hiragana.hiragana )
create_img("Out/Katakana" , "k"        , katakana.katakana )
create_img("Out/Mark"     , "m"        , mark.mark     )
create_img("Out/Kanji1" , "kanji_"   , kanji1.kanji1   )
create_img("Out/Kanji2" , "kanji_2_" , kanji2.kanji2   )
create_img("Out/Kanji3" , "kanji_3_" , kanji3.kanji3   )
create_img("Out/Kanji4" , "kanji_4_" , kanji4.kanji4   )
create_img("Out/Kanji5" , "kanji_5_" , kanji5.kanji5   )
create_img("Out/Kanji6" , "kanji_6_" , kanji6.kanji6   )

