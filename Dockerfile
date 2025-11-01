FROM ubuntu:22.04

# Install Python
RUN apt-get -y update && \
    apt-get install python3.13

# Install project dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY src ./src
COPY train.py .

COPY app ./app
RUN chmod +x app/api.sh

CMD ["bash", "app/api.sh"]
