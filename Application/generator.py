from PIL import Image, ImageDraw, ImageFont
import config

font = ImageFont.truetype("calibrib.ttf", size=int(130))

eng_all = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_lowercase = 'abcdefghijklmnopqrstuvwxyz'
eng_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_uppercase_singlewidth = 'АБВГДЕЁЗИЙКЛНОПРСТУХЦЧЪЬЭЯ'
ru_uppercase_doublewidth = 'ЖМФШЩЫЮ'

def save(letter, xy):
    img = Image.open('empty.png')
    ID = ImageDraw.Draw(img)
    ID.text(xy, letter, fill=(0, 0, 0),font=font,align='center')
    img.save(config.ALPHABET_FOLDER + letter +".png")
    #todo fix alignments!

for i in ru_uppercase_singlewidth:
    save(i, (10, -5))
font = ImageFont.truetype("calibrib.ttf", size=int(110))
for i in ru_uppercase_doublewidth:
    save(i, (0, 5))
     
