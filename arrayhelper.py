def parse_image(image, div, pixel):
    res = []
    slen = int(len(image) / div)
    for x in range(0,div):
        res.append([])
        for y in range(0,div):
            isWhites = 0
            for i in range(0,slen):
                for j in range(0, slen):
                    #todo centralize like FirstRightColumn + FirstLeftColumn / 2? same for rows?
                    isWhite = is_white_pixel(image[i+(x*slen)][j+(y*slen)], pixel)
                    if not isWhite:
                        isWhites += 1
            res[x].append(int(isWhites > 0))
    return res

def is_white_pixel(rgb, pixel):
    for i in rgb:
        if i != pixel:
            return False
    return True

def show(list):
    for i in list:
        for j in i:
            print(j,end=' ')
        print()

def a(div, alphabet, im):
    results = {}
    for img in alphabet:
        curr = alphabet[img]
        sum = 0
        for i in range(div):
            for j in range(div):
                sum += abs(curr[i][j] - im[i][j])
        results[img] = sum
    return results