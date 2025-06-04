# GPU Detection Scripts

This repository contains Python scripts to check GPU availability and status using PyTorch and TensorFlow.

## Files

- **gpu_test.py**: Checks GPU availability using PyTorch and TensorFlow.
- **gpu_test_pytorch.py**: Checks GPU availability using PyTorch only.
- **gpu_test_tf.py**: Checks GPU availability using TensorFlow only.

## Usage

To check for GPU availability, run the appropriate script:

- **For both PyTorch and TensorFlow:**
  ```bash
  python gpu_test.py
  ```
- **For PyTorch only:**
  ```bash
  python gpu_test_pytorch.py
  ```
- **For TensorFlow only:**
  ```bash
  python gpu_test_tf.py
  ```

## Output

Each script will display the following information:

- **PyTorch**: 
  - If CUDA is available.
  - Number of CUDA devices.
  - Name of the first CUDA device (if available).
  
- **TensorFlow**:
  - Number of GPUs available (prefixed with `Num GPUs Available:`).

## Requirements

Ensure you have the necessary libraries installed. The scripts will notify you
if either library is missing. Install them individually with:

```bash
pip install torch tensorflow pytest
```
