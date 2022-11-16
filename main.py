from skimage import io
from collections import OrderedDict
import arrayhelper
import alphabet

xlen = alphabet.xlen
test = arrayhelper.parse_image(io.imread('test.png'), xlen)
results = {}
for img in alphabet.dictionary:
    curr = alphabet.dictionary[img]
    sum = 0
    for i in range(xlen):
        for j in range(xlen):
           sum += abs(curr[i][j] - test[i][j])
    results[img] = sum

print()
print("Test:")
arrayhelper.show(test)
print()
sortedres = {k: results[k] for k in sorted(results, key=results.get)}
print(sortedres)
print("It is", list(sortedres)[0] + "!")
