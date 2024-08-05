# Use the official Python image from the Docker Hub
FROM python:3.11

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the Django project into the working directory
COPY . /app/

# Copy the entrypoint.sh and wait-for-it.sh scripts
COPY entrypoint.sh /app/entrypoint.sh
COPY wait-for-it.sh /app/wait.sh

# Make the scripts executable
RUN chmod +x /app/entrypoint.sh
RUN chmod +x /app/wait.sh

# Expose the port that the app runs on
EXPOSE 8000

# Set entrypoint
ENTRYPOINT ["/app/entrypoint.sh"]

# Start the Gunicorn server
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "TODOLIST_API.wsgi:application"]

