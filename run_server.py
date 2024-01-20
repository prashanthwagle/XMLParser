import subprocess
import sys

try:
    import flask
except ImportError:
    pip_command = "pip3" if sys.platform.startswith(
        "linux") or sys.platform.startswith("darwin") else "pip"
    subprocess.run([pip_command, "install", "Flask"])

try:
    import unittest
except ImportError:
    pip_command = "pip3" if sys.platform.startswith(
        "linux") or sys.platform.startswith("darwin") else "pip"
    subprocess.run([pip_command, "install", "unittest2"])

from app import app
if __name__ == "__main__":
    app.run(port=3456)
