#!/usr/bin/env sh
# Create the imagenet lmdb inputs
# N.B. set the path to the imagenet train + val data dirs
set -e

EXAMPLE=/media/hunhpc/bak/FPdataset/build_lmdb
#生成模型训练数据的文件夹，此脚本文件所在的文件夹
DATA=/media/hunhpc/bak/FPdataset
#生成的文件列表，txt文件所在的文件夹
TOOLS=/home/hunhpc/caffe/build/tools
#caffe的工具库

TRAIN_DATA_ROOT=/media/hunhpc/bak/FPdataset/
#待处理的训练数据
VAL_DATA_ROOT=/media/hunhpc/bak/FPdataset/
#待处理的验证数据

rm -rf $EXAMPLE/train_lmdb
rm -rf $EXAMPLE/val_lmdb
# Set RESIZE=true to resize the images to 256x256. Leave as false if images have
# already been resized using another tool.
#是否需要对图片进行resize
RESIZE=true
if $RESIZE; then
  RESIZE_HEIGHT=360
  RESIZE_WIDTH=256
else
  RESIZE_HEIGHT=0
  RESIZE_WIDTH=0
fi

if [ ! -d "$TRAIN_DATA_ROOT" ]; then
  echo "Error: TRAIN_DATA_ROOT is not a path to a directory: $TRAIN_DATA_ROOT"
  echo "Set the TRAIN_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet training data is stored."
  exit 1
fi

if [ ! -d "$VAL_DATA_ROOT" ]; then
  echo "Error: VAL_DATA_ROOT is not a path to a directory: $VAL_DATA_ROOT"
  echo "Set the VAL_DATA_ROOT variable in create_imagenet.sh to the path" \
       "where the ImageNet validation data is stored."
  exit 1
fi

echo "Creating train lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $TRAIN_DATA_ROOT \
    $DATA/FPtrain1.txt \
    $EXAMPLE/train_lmdb

echo "Creating val lmdb..."

GLOG_logtostderr=1 $TOOLS/convert_imageset \
    --resize_height=$RESIZE_HEIGHT \
    --resize_width=$RESIZE_WIDTH \
    --shuffle \
    $VAL_DATA_ROOT \
    $DATA/FPval1.txt \
    $EXAMPLE/val_lmdb

echo "Done."
