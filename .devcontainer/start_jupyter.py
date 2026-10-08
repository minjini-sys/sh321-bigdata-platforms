"""Start Jupyter independently of the Dev Containers startup shell."""
import socket
import subprocess
import sys
import time
from pathlib import Path


def is_running():
    try:
        with socket.create_connection(("127.0.0.1", 8888), timeout=1):
            return True
    except OSError:
        return False


if is_running():
    print("Port 8888 is already listening; skipping Jupyter startup.")
    sys.exit(0)

with open("/tmp/jlab.log", "a") as log:
    process = subprocess.Popen(
        [sys.executable, "-m", "jupyterlab", "--ip=0.0.0.0",
         "--port=8888", "--ServerApp.port_retries=0", "--no-browser",
         "--allow-root", "--ServerApp.token=", "--ServerApp.password="],
        cwd=Path(__file__).resolve().parents[1],
        stdin=subprocess.DEVNULL, stdout=log, stderr=subprocess.STDOUT,
        start_new_session=True,
    )
    for _ in range(30):
        if is_running():
            print("Jupyter is ready on port 8888.")
            break
        if process.poll() is not None:
            raise RuntimeError("Jupyter exited. See /tmp/jlab.log")
        time.sleep(1)
    else:
        raise RuntimeError("Jupyter startup timed out. See /tmp/jlab.log")