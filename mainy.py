from skimage import io
import arrayhelper
import alphabet

DOFILTER = True
pix_color= 0 if DOFILTER else 255

def go(img):
    div = alphabet.div
    test = arrayhelper.parse_image(img, div, pix_color)
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
    return list(sortedres)[0]
