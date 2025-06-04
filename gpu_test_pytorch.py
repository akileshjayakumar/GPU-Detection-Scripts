# gpu_test_pytorch.py
try:
    import torch
except ModuleNotFoundError:
    torch = None
    print("PyTorch is not installed.")

if torch is None:
    print("PyTorch not available.")
else:
    print("CUDA available: ", torch.cuda.is_available())
    print("CUDA device count: ", torch.cuda.device_count())
    if torch.cuda.is_available() and torch.cuda.device_count() > 0:
        print("CUDA device name: ", torch.cuda.get_device_name(0))
