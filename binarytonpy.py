# coding=UTF-8
import caffe
import numpy as np

MEAN_PROTO_PATH = './build_lmdb/mynet_mean.binaryproto'               

MEAN_NPY_PATH = './build_lmdb/mynet_mean.npy'                        


blob = caffe.proto.caffe_pb2.BlobProto()           

data = open(MEAN_PROTO_PATH, 'rb' ).read()         

blob.ParseFromString(data)                         


array = np.array(caffe.io.blobproto_to_array(blob))

mean_npy = array[0]                               

np.save(MEAN_NPY_PATH ,mean_npy)
