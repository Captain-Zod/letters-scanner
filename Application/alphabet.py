from skimage import io
import arrayhelper, config
from os import listdir
from os.path import isfile, join

dictionary = {}

files = [f for f in listdir(config.ALPHABET_FOLDER) if isfile(join(config.ALPHABET_FOLDER, f))]
for f in files:
    file = io.imread(config.ALPHABET_FOLDER+f)
    image = arrayhelper.parse_image(file, config.DIVISIONS, 255)
    dictionary[f[0]] = image


