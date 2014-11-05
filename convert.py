from PIL import Image
import tools
import glob
import os
import atexit
from time import time
import sys, getopt
from multiprocessing import Pool


def endlog():
    end = time()
    elapsed = end-start
    print "Elapsed time in sec: " + str(elapsed)
    if elapsed > 0:
        print "Images per sec: " + str(processedImages / elapsed)
    print "======================"

def processImage(infile):
    path, ext = os.path.splitext(infile)
    file = os.path.basename(path)
    im = Image.open(infile)
    im.save("results/" + file + "." + toExt, format)

input = ''
fromExt = ''
toExt = ''
format = ''
processes = 1

try:
    opts, args = getopt.getopt(sys.argv[1:], "i:f:t:p:", ["input=", "from=", "to=", "processes="])
except getopt.GetoptError:
    sys.exit(2)
for opt, arg in opts:
    if opt == '-i':
        input = arg
    elif opt == '-f':
        fromExt = arg
    elif opt == '-t':
        toExt = arg
        if toExt == 'jpg':
            format = 'JPEG'
        elif toExt == 'png':
            format = 'PNG'
    elif opt == '-p':
        processes = int(float(arg))

tools.clear("results/")

files = glob.glob(input + "*." + fromExt)
processedImages = len(files)

print "======================"
start = time()
atexit.register(endlog)

if processes == 1:
    for infile in files:
        processImage(infile)
else:
    pool = Pool(processes=processes)
    pool.map(processImage, files)
    pool.close()
    pool.join()