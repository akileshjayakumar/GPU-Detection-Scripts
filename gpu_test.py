# gpu_test.py
import torch
import tensorflow as tf

# Check PyTorch GPU
print("PyTorch:")
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA device count: {torch.cuda.device_count()}")
if torch.cuda.is_available():
    print(f"CUDA device name: {torch.cuda.get_device_name(0)}")

# Check TensorFlow GPU
print("\nTensorFlow:")
print(f"Num GPUs Available: {len(tf.config.experimental.list_physical_devices('GPU'))}")
