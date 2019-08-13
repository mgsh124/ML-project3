# Use an official Python runtime as an image
FROM python:3.7.3

# The EXPOSE instruction indicates the ports on which a container # # will listen for connections
# Since Flask apps listen to port 5000  by default, we expose it
EXPOSE 8080

# Sets the working directory for following COPY and CMD instructions
# Notice we haven’t created a directory by this name - this
# instruction creates a directory with this name if it doesn’t exist
WORKDIR /app

# Install any needed packages specified in requirements.txt
#COPY requirements.txt /app
#RUN pip install --upgrade pip
#RUN pip install -r requirements.txt
RUN pip install flask
RUN pip install requests
RUN pip install Werkzeug
RUN pip install gTTS

# Copy files
COPY app.py /app/
COPY static/ /app/static/
COPY templates/ /app/templates/

## THE LIFE SAVER
ADD https://github.com/ufoscout/docker-compose-wait/releases/download/2.2.1/wait /wait
RUN chmod +x /wait

## Launch the wait tool and then your application
CMD /wait && python app.py