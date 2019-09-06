# FCTP-Net

This is a code for our paper "***Fingerprint Pattern Identification and Classification Approach Based on Convolutional Neural Networks***", published on "***Neural Computing and Applications***".

In this paper, we use a six-category fingerprint database instead four-category, which is not suitable for researching human personalities. We classified fingerprints into Arc(A), Whorl(W), Double Whorl(DW), Ulnar Loop(UL), Radial Loop(RP) and Peacock Wye(PE). Some details of datasets are as follows:

![Loading failed](https://github.com/VictorZoo/FCTP-Net/blob/master/demo_image/1567746772(1).jpg)

We uploaded netfiles (**Alexnet**, **Lenet**, **Caffenet** and our **FCTP-Net**). 

Hope that will be helpful for you!

### Installation

* ####Caffe

  We used **Caffe** framwork, you can clik [here](https://github.com/BVLC/caffe) to get the instruction to build it.
  
* ####Datasets (for demo)

  For privacy, we put some data of six-category in project and you should turn the images to ```.lmdb```. You also can download the [four-category](https://www.nist.gov/srd/nist-special-database-4) on NIST for more investigation.
