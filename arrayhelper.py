def parse_image(image, xlen):
    res = []
    slen = int(len(image) / xlen)
    for x in range(0,xlen):
        res.append([])
        for y in range(0,xlen):
            isWhite = True
            for i in range(0,slen):
                for j in range(0, slen):
                    #todo centralize like FirstRightColumn + FirstLeftColumn / 2? same for rows?
                    isWhite = is_white_pixel(image[i+(x*slen)][j+(y*slen)])
                    if not isWhite:
                        break
                if not isWhite:
                    break
            res[x].append(int(not isWhite))
    return res

def is_white_pixel(rgb):
    for i in rgb:
        if i != 255:
            return False
    return True

def show(list):
    for i in list:
        for j in i:
            print(j,end=' ')
        print()
