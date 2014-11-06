Python Pillow
====
Pillow 2.6 was used in test scripts. It requires Python 2.7 or higher and Pip to easily install Pillow. You can find detailed instructions here https://pillow.readthedocs.org/installation.html.
Pillow requires several external libraries: libjpeg, zlib, libfreetype.
You can find sample command used to configure instances in ec2.config.txt.

Convert command:
====
python convert.py -i ${input} -f ${from} -t ${to} -p ${processes}

-i: input folder path.
-f: input format to convert images from [jpg, png].
-t: output format to convert images to [png, jpg].
-p: processes count for multiprocessing tests (1 by default).

You can find samples in ec2.config.txt.

Resize command:
====
python resize.py -i ${input} -e ${ext} -h ${height} -w ${width} -p ${processes}

-i: input folder path.
-e: input files extension [jpg, png].
-h: result images height.
-w: result images width.
-p: processes count for multiprocessing tests (1 by default).

You can find samples in ec2.config.txt.
