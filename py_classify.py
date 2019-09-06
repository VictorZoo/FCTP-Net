#coding=utf-8

import numpy as np

import sys,os


caffe_root = '/your_caffe_dir/caffe/' 
sys.path.insert(0, caffe_root + 'python')
import caffe
os.chdir(caffe_root)

net_file=caffe_root + 'build/examples/cpp_classification/mynet_deploy.prototxt'
caffe_model=caffe_root + 'build/examples/cpp_classification/caffenet_train_iter_100000.caffemodel'
mean_file=caffe_root + './mynet_mean.npy'

net = caffe.Net(net_file,caffe_model,caffe.TEST)
transformer = caffe.io.Transformer({'data': net.blobs['data'].data.shape})
transformer.set_transpose('data', (2,0,1))
transformer.set_mean('data', np.load(mean_file).mean(1).mean(1))
transformer.set_raw_scale('data', 255) 
transformer.set_channel_swap('data', (2,1,0))

im=caffe.io.load_image('./val/test_A/e402420f-3f7b-11e7-b208-e09467e031f1.png')
net.blobs['data'].data[...] = transformer.preprocess('data',im)
out = net.forward()


imagenet_labels_filename = caffe_root + 'build/examples/cpp_classification/test.txt'
labels = np.loadtxt(imagenet_labels_filename, str, delimiter='\t')

top_k = net.blobs['prob'].data[0].flatten().argsort()[-1:-6:-1]
for i in np.arange(top_k.size):
    print ( top_k[i],labels[top_k[i]])

