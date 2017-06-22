echo "Create $1.png"
convert -pointsize 140 -font /usr/share/fonts/TTF/Mplus1p-Black.ttf -annotate 0 $1 -gravity center -fill black -size 128x128 xc:none $1.png
