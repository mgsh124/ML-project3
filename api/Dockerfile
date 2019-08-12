# Anaconda base image
FROM continuumio/miniconda3

RUN apt-get update && apt-get install -y python3
RUN apt-get install -y python3-pip
RUN apt-get install -y build-essential

# Create conda environment
# Same as RUN /opt/conda/bin/conda create -n myenv python=3.7
RUN ["conda", "create", "-n", "myenv", "python=3.7"]

# Install libraries inside conda environment
RUN /bin/bash -c "source activate myenv && pip install flask && pip install numpy && \
pip install keras && pip install pillow"

# Copy API file
COPY api.py /app/

WORKDIR /app
RUN ls .
CMD /bin/bash -c "source activate myenv && python api.py"