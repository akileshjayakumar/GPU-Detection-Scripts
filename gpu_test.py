# gpu_test.py
try:
    import torch
except ModuleNotFoundError:
    torch = None
    print("PyTorch is not installed.")

try:
    import tensorflow as tf
except ModuleNotFoundError:
    tf = None
    print("TensorFlow is not installed.")

# Check PyTorch GPU
print("PyTorch:")
if torch is None:
    print("PyTorch not available.")
else:
    print(f"CUDA available: {torch.cuda.is_available()}")
    print(f"CUDA device count: {torch.cuda.device_count()}")
    if torch.cuda.is_available() and torch.cuda.device_count() > 0:
        print(f"CUDA device name: {torch.cuda.get_device_name(0)}")

# Check TensorFlow GPU
print("\nTensorFlow:")
if tf is None:
    print("TensorFlow not available.")
else:
    num_gpus = len(tf.config.experimental.list_physical_devices('GPU'))
    print(f"Num GPUs Available: {num_gpus}")
