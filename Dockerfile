# This Dockerfile sets up the environment for running QA tests with Selenium.
# It ensures all dependencies are isolated and reproducible across machines.

# Dependencies:
# - Python: 3.12.3
# - Pytest: 8.3.3
# - Selenium: 4.25.0
# - Chromedriver: 130.0.6723.69
# - Google Chrome: 130.0.6723.69

# To run the container and output logs to testing.log, use:
# docker run -it --rm -v "$(pwd)/tests/logs:/app/tests/logs" lighthouse-qa-image

# Base image
FROM selenium/standalone-chrome@sha256:f1143e4c6608ead5e14973ba8cc74d6fbe8a032b7cc94ae2e3f0cdf1bd8944e3

# Switch to root user to install additional packages
USER root

# Set up the working directory
WORKDIR /app

# Install Python's virtual environment package
RUN apt-get update && \
    apt-get install -y python3-venv && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Create a virtual environment for Python packages
RUN python3 -m venv /app/venv

# Activate the virtual environment and install pip
RUN /app/venv/bin/python -m ensurepip --upgrade

# Copy requirements.txt to install Python dependencies in the virtual environment
COPY requirements.txt .

# Install dependencies in the virtual environment
RUN /app/venv/bin/pip install -r requirements.txt

# Copy the application code
COPY . .

# Set the PATH to use the virtual environment's Python and pip
ENV PATH="/app/venv/bin:$PATH"

# Define the command to run tests
CMD ["pytest", "-v", "tests/test_main.py"]