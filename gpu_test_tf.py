# gpu_test_tf.py
try:
    import tensorflow as tf
except ModuleNotFoundError:
    tf = None
    print("TensorFlow is not installed.")

if tf is None:
    print("TensorFlow not available.")
else:
    num_gpus = len(tf.config.experimental.list_physical_devices('GPU'))
    print("Num GPUs Available: ", num_gpus)
