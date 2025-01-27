# Use Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
COPY app.py /app/
COPY style.css /app/
COPY index.html /app/
COPY cart.html /app/
COPY checkout.html /app/

RUN mkdir static && mv style.css static/
RUN mkdir templates && mv index.html cart.html checkout.html templates/
RUN pip install -r requirements.txt


# Expose port
EXPOSE 5000

# Run Flask app
CMD ["python", "app.py"]
