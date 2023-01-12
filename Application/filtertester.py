from skimage import data, io, filters

image = io.imread('asdf.jpg')
# ... or any other NumPy array!
edges = filters.meijering(image)

#low = 0.1
#high = 0.35
#
#lowt = (edges > low).astype(int)
io.imshow(edges)
io.show()
