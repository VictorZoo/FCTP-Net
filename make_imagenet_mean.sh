#!/usr/bin/env sh
# Compute the mean image from the imagenet training lmdb
# N.B. this is available in data/ilsvrc12

EXAMPLE=/media/hunhpc/bak/FPdataset/build_lmdb/
DATA=/media/hunhpc/bak/FPdataset/build_lmdb
TOOLS=/home/hunhpc/caffe/build/tools

$TOOLS/compute_image_mean $EXAMPLE/train_lmdb \
$DATA/mynet_mean.binaryproto

echo "Done."
