from mlxtend.data import loadlocal_mnist

X, y = loadlocal_mnist(
        images_path='train-images.idx3-ubyte',
        labels_path='train-labels.idx1-ubyte')

print('Dimensions: %s x %s' % (X.shape[0], X.shape[1]))
print('\n1st row', X[0])
