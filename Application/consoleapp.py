from skimage import io
import arrayhelper, alphabet, config



def start():
    img = io.imread(input("Введите путь к файлу: "))
    find(img)

def find(img):
    test = arrayhelper.parse_image(img, config.DIVISIONS, config.PIX_COLOR)
    results = {}
    for img in alphabet.dictionary:
        curr = alphabet.dictionary[img]
        sum = 0
        for i in range(config.DIVISIONS):
            for j in range(config.DIVISIONS):
                sum += abs(curr[i][j] - test[i][j])
        results[img] = sum

    arrayhelper.show(test)
    print()
    sortedres = {k: results[k] for k in sorted(results, key=results.get)}
    print(sortedres)
    print("It is", list(sortedres)[0] + "!")
    return list(sortedres)[0]

start()