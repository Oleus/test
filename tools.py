import os

def clear(folder):
    if not os.path.exists(folder):
        try:
            os.makedirs(folder)
        except:
            if not os.path.exists(folder):
                print 'Failed creating results folder.'
                raise


    for root, dirs, files in os.walk(folder, topdown=False):
        for name in files:
            os.remove(os.path.join(root, name))
        for name in dirs:
            os.rmdir(os.path.join(root, name))

def chunkify(array, n):
    return [ array[i::n] for i in xrange(n) ]