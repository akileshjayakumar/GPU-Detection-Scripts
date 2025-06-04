import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]


def run_script(script_name):
    script_path = ROOT / script_name
    subprocess.run([sys.executable, str(script_path)], check=True)


def test_gpu_test():
    run_script('gpu_test.py')


def test_gpu_test_pytorch():
    run_script('gpu_test_pytorch.py')


def test_gpu_test_tf():
    run_script('gpu_test_tf.py')
