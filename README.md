# Lighthouse-Properties-QA-Automation
QA automation suite for the real estate company Lighthouse Properties.

# Overview
This project contains automated tests for Lighthouse Properties' website, which can be run either locally or within a Docker container for a consistent environment setup.

## Running the Project Locally
If you prefer to run everything locally rather than using a Docker container, make sure to install the following dependencies with the specified versions to ensure compatibility.

## Dependencies
- **Python**: 3.12.3
- **Pytest**: 8.3.3
- **Selenium**: 4.25.0
- **Google Chrome**: 130.0.6723.69
- **ChromeDriver**: 130.0.6723.69

## Running the Project in a Docker Container
### Prerequisites
1. **Docker Desktop:** Ensure Docker Desktop is installed and running.
2. **WSL 2 (if you're on Windows):** Make sure WSL 2 is installed with **Ubuntu** (or another Linux distribution), and **Docker integration** is enabled. You can verify this in Docker Desktop settings under **Resources > WSL Integration**.
**Note:** Before running the Docker image, ensure you are in the correct directory: C:\Users\(Your Name)\Desktop\ **Lighthouse-QA-Automation\Lighthouse-Properties-QA-Automation**

Running the project in a Docker container allows you to skip the process of manually installing dependencies.If  you’d like to view the logs in the **testing.log** file located at **tests/logs/testing.log**, use the following command in your terminal:
**docker run -it --rm -v "$(pwd)/tests/logs:/app/tests/logs" lighthouse-qa-image**

**Important:** Logs are recorded only in the testing.log file and are not outputted in the terminal.

## Running the Docker Container Using a Shell Script
For added convenience, you can use the provided shell script to automate the Docker container build and run steps.
**Using the shell script**
1. **Ensure Execute Permissions:** Before running the script, make sure it has execute permissions: **chmod +x run_docker_tests.sh**
2. **Run the Shell Script:**: **sudo ./run_docker_tests.sh**
The shell script will automatically **build the Docker image** and **run the container** with the log mounting setup. This method is ideal for quickly starting the container without manually entering Docker commands.

## Note on Permissions:
If you encounter any permission errors while using Docker in WSL, make sure to use **sudo** when running the shell script, as shown above.
