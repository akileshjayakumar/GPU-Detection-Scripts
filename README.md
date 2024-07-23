# GPU Detection Scripts

This repository contains Python scripts to check the availability and status of GPU devices on your system using PyTorch and TensorFlow.

## Files

- **gpu_test.py**: A script to check GPU availability and details using both PyTorch and TensorFlow.
- **gpu_test_pytorch.py**: A script to check GPU availability and details using PyTorch only.
- **gpu_test_tf.py**: A script to check GPU availability and details using TensorFlow only.

## Usage

### gpu_test.py

This script will check for GPU availability using both PyTorch and TensorFlow.

```bash
python gpu_test.py
```

### gpu_test_pytorch.py

This script will check for GPU availability using PyTorch.

```bash
python gpu_test_pytorch.py
```

### gpu_test_tf.py

This script will check for GPU availability using TensorFlow.

```bash
python gpu_test_tf.py
```

## Output

The scripts will output the following information:

- For PyTorch:
  - Whether CUDA is available.
  - The number of CUDA devices.
  - The name of the first CUDA device (if available).

- For TensorFlow:
  - The number of GPUs available.

## Requirements

Make sure you have the necessary libraries installed before running the scripts. You can install them using pip:

```bash
pip install torch tensorflow
```

## Acknowledgements

Thanks to the open-source community for providing the tools and libraries used in this repo.
