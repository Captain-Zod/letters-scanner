from PIL import Image, ImageDraw, ImageFont

img = Image.open('empty.png')
font = ImageFont.truetype("calibrib.ttf", size=int(130))
path = "Alphabet\\"

eng_all = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_lowercase = 'abcdefghijklmnopqrstuvwxyz'
eng_uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
ru_uppercase_singlewidth = 'АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
ru_uppercase_doublewidth = 'ЖМФЦШЩЫЮ'

for i in ru_uppercase_singlewidth:
    I1 = ImageDraw.Draw(img)
    I1.text((10, -5), i, fill=(0, 0, 0),font=font,align='center')
    img.save(path + i +".png")
    img = Image.open('empty.png')
    #todo fix alignments!

font = ImageFont.truetype("calibrib.ttf", size=int(110))
for i in ru_uppercase_doublewidth:
    I1 = ImageDraw.Draw(img)
    I1.text((0, 5), i, fill=(0, 0, 0),font=font,align='center')
    img.save(path + i +".png")
    img = Image.open('empty.png')
