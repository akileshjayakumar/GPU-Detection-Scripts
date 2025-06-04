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
  - Number of GPUs detected.

## Requirements

Ensure you have the necessary libraries installed. The scripts will notify you
if either library is missing. Install them individually with:

```bash
pip install torch tensorflow pytest
```

Alternatively, install everything from the provided requirements file:

```bash
pip install -r requirements.txt
```

## Testing

This project uses [pytest](https://pytest.org/) for its test suite. After
installing the required packages, run:

```bash
pytest
```

This command executes the tests under the `tests` directory and verifies that
each GPU detection script runs without errors.

## Acknowledgments

Thanks to the open-source community for the tools and libraries used.
