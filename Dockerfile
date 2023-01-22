from python:3.8-slim-buster

# Install dependencies
ARG DEBIAN_FRONTEND=noninteractive
RUN apt update && apt install -y ffmpeg portaudio19-dev python3-pip git

# Install python dependencies
COPY requirements.txt .
RUN pip3 install -r requirements.txt

# Copy the code
COPY . .

# Expose the port
EXPOSE 8000

# Run the server
CMD ["uvicorn", "whisper_server:app", "--host", "0.0.0.0", "--port", "8000"]