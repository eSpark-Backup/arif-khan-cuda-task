# CGBN Key Sample

This repository contains a sample application that demonstrates the use of the CGBN (CUDA Generic Bignum) library. Before running the sample, ensure that you have the NVIDIA CUDA Toolkit installed on your system.

## Prerequisites

### 1. Install NVIDIA CUDA Toolkit

Ensure that you have the NVIDIA CUDA Toolkit installed on your machine. If not, you can download and install it from the [official NVIDIA CUDA Toolkit website](https://developer.nvidia.com/cuda-downloads).

### 2. Install GMP Library

Run the following commands to install the GMP (GNU Multiple Precision Arithmetic Library) development files:

```
sudo apt-get update
sudo apt-get install libgmp3-dev
```

## Build Instructions
Move to the key sample directory within the CGBN samples:
```
cd {path-to-repo}/Development/App/CGBN-master/samples/key
```
Build for RTX 4090 Architecture
Run the following command to build for the RTX 4090 (sm_89) architecture. Other supported architectures are mentioned in the Makefile.
```
make ada
```

##  Run the Program
Execute the following command to build and run the sample. You can specify the operand value and the number of iterations. Key, input bot file, and output file can be changed from Makefile.

### For addition (run_add):
```
make run_add value=1 iterations=20
```
### For subtraction (run_sub):
```
make run_sub value=1 iterations=20
```
