import os
import collections

from char_set import alphabet, katakana, hiragana,  mark
from char_set import kanji1, kanji2, kanji3, kanji4

"""
auther:
    Sohei Yamaga <me@eliza.link>
licence: 
    MIT LICENCE
dependents:
    ImageMagick, Python3
shell: 
    convert -pointsize 140
            -font /usr/share/fonts/TTF/Mplus1p-Black.ttf 
            -annotate 0 $1
            -gravity center
            -fill black
            -size 128x128
            xc:none
            $1.png
"""

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
    print("creating emoji: "+path+" case", end="")
    os.system("mkdir " + path)
    already = collections.defaultdict(lambda: 0)
    cnt = 0
    for char_data in data:
        key = char_data[0]
        value = char_data[1]
        if(0<already[value]):
            value= value + str(already[value])
        make_emoji(path, pre+value, key)
        print('.', end='')
    print("")

os.system("mkdir " + "Out")
create_img("Out/Lower"    , "l"        , alphabet.alpha    )
create_img("Out/Upper"    , "u"        , alphabet.ualpha   )
create_img("Out/Hiragana" , "j"        , hiragana.hiragana )
create_img("Out/Katakana" , "k"        , katakana.katakana )
create_img("Out/Mark"     , "m"        , mark.mark     )
create_img("Out/Kanji1rd" , "kanji_"   , kanji1.kanji1   )
create_img("Out/Kanji2rd" , "kanji_2_" , kanji2.kanji2   )
create_img("Out/Kanji3rd" , "kanji_3_" , kanji3.kanji3   )
create_img("Out/Kanji4rd" , "kanji_4_" , kanji4.kanji4   )

