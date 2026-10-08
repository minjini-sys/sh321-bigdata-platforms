FROM bitnamilegacy/spark:3.5
USER 0
RUN install_packages curl ca-certificates \
 && pip install --no-cache-dir \
      jupyterlab>=4.2 pandas>=2.2 numpy>=1.26 matplotlib>=3.8 \
      pyarrow>=15.0 ipywidgets>=8.1 findspark
ENV PYSPARK_PYTHON=python
ENV PYSPARK_DRIVER_PYTHON=jupyter
ENV PYSPARK_DRIVER_PYTHON_OPTS="lab --ip=0.0.0.0 --no-browser --NotebookApp.token='' --NotebookApp.password=''"
WORKDIR /workspace
USER 1001
CMD ["bash", "-lc", "jupyter lab --ip=0.0.0.0 --no-browser --NotebookApp.token='' --NotebookApp.password=''"]