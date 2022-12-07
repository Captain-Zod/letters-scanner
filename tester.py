from skimage import io
import arrayhelper
import alphabet

div = alphabet.div
test = arrayhelper.parse_image(io.imread('test.png'), div, 255)
results = {}
for img in alphabet.dictionary:
    curr = alphabet.dictionary[img]
    sum = 0
    for i in range(div):
        for j in range(div):
           sum += abs(curr[i][j] - test[i][j])
    results[img] = sum

print("Test:")
arrayhelper.show(test)
print()
sortedres = {k: results[k] for k in sorted(results, key=results.get)}
print(sortedres)
print("It is", list(sortedres)[0] + "!")
