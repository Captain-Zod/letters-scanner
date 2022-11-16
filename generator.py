from PIL import Image, ImageDraw, ImageFont

img = Image.open('empty.png')
font = ImageFont.truetype("calibrib.ttf", size=int(110))
path = "Alphabet\\"

eng_all = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_lowercase = 'abcdefghijklmnopqrstuvwxyz'
eng_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

for i in eng_uppercase:
    I1 = ImageDraw.Draw(img)
    I1.text((5, 5), i, fill=(0, 0, 0),font=font)
    img.save(path + i +".png")
    img = Image.open('empty.png')
    #todo fix alignments!