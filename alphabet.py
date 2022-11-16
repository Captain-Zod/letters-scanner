from skimage import io
import arrayhelper
from os import listdir
from os.path import isfile, join

dictionary = {}
xlen = 25
path = "Alphabet\\"
files = [f for f in listdir(path) if isfile(join(path, f))]
for f in files:
    file = io.imread(path+f)
    image = arrayhelper.parse_image(file, xlen)
    dictionary[f[0]] = image


