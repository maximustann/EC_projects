#!/bin/sh
echo It might take a while...
echo Sobel Edge detecting
python ./program/sobel.py ./pics/test.tif ./pics/result/sobel_test.png

echo Mean filtering
python ./program/mean_3.py ./pics/ckt.png ./pics/result/mean_3_ckt.png
python ./program/mean_5.py ./pics/ckt.png ./pics/result/mean_5_ckt.png

echo Median filtering
python ./program/median.py ./pics/ckt.png ./pics/result/median_ckt.png

echo Picture shapen using Laplace filtering
python ./program/laplace.py ./pics/blurry-moon.tif ./pics/result/shape_moon.png

echo Finished
