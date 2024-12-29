# Use the official Apache Flink base image
FROM apache/flink:1.17.2

# Install Python3 and Pip
RUN apt-get update && apt-get install -y --no-install-recommends python3 python3-pip

# (Optional) Verify Python installation
RUN python3 --version

# Copy requirements.txt (if you have one) and install Python dependencies
COPY requirements.txt /tmp/
RUN python3 -m pip install -r /tmp/requirements.txt

# Set Python3 as the default Python executable
RUN ln -s /usr/bin/python3 /usr/bin/python
