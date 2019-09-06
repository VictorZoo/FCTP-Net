# FCTP-Net

This is a code for our paper "***Fingerprint Pattern Identification and Classification Approach Based on Convolutional Neural Networks***", published on "***Neural Computing and Applications***".

In this paper, we use a six-category fingerprint database instead four-category, which is not suitable for researching human personalities. We classified fingerprints into Arc (A), Whorl (W), Double Whorl (DW), Ulnar Loop (UL), Radial Loop (RP) and Peacock ye (PE). Some details of datasets are as follows:

![Loading failed](https://github.com/VictorZoo/FCTP-Net/blob/master/demo_image/1567746772(1).jpg)

We uploaded netfiles (**Alexnet**, **Lenet**, **Caffenet** and our **FCTP-Net**). 

Hope that will be helpful for you!

### Installation

* Caffe

  We used **Caffe** framwork, you can click [here](https://github.com/BVLC/caffe) to get the instruction to build it.
  
* Datasets (for demo)

  For privacy, we put some data of six-category in project and you should turn the images to ```.lmdb``` (click [here](https://blog.csdn.net/u010417185/article/details/52119863) for more infos). You also can download the [four-category](https://www.nist.gov/srd/nist-special-database-4) on NIST for more investigation.

### How to run a demo

In LINUX OS, you should create a ```.sh``` file, in which the content can be:

```
#!/usr/bin sh
set -e
TOOLS=/*your_caffe_dir*/build/tools
LOG=./*your_log_dir*/mynet.log
$TOOLS/caffe train --solver=./mynet_solver.prototxt -gpu 0 2>&1 |tee -a $LOG
```

Moreover, you should adjust some file directions according to your direction of data or something else.

### Results

|Model|Accuracy|
|:-:|:-:|
| Alexnet | 47.03% |
| Caffenet | 82.63% |
| Lenet | 16.64% |
| FCTP-Net | 93.14% |
