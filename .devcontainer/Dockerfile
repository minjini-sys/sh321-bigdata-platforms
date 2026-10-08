FROM bitnamilegacy/spark:3.5

USER 0

RUN install_packages curl ca-certificates \
    && pip install --no-cache-dir \
        "jupyterlab>=4.2" "tornado==6.5.8" "pandas==2.3.2" "numpy==2.3.3" "matplotlib>=3.8" \
        "pyarrow==21.0.0" "ipywidgets>=8.1" findspark \
    && ln -sf /opt/bitnami/python/bin/jupyter /usr/local/bin/jupyter

ENV PYSPARK_PYTHON=python
ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS="lab --ip=0.0.0.0 --no-browser --NotebookApp.token='' --NotebookApp.password=''"

WORKDIR /workspace

USER 1001

CMD ["python", "-m", "jupyterlab", "--ip=0.0.0.0", "--no-browser", "--ServerApp.token=", "--ServerApp.password="]
