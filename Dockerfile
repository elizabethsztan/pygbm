# Use a base image with Python installed
FROM python:3.9  

# Set the working directory in the container
WORKDIR /app

# Copy your pygbm package to the working directory
COPY . /app

# Install any dependencies specified in requirements.txt
# Ensure a requirements.txt file lists all dependencies, or install manually below
RUN pip install --upgrade pip
RUN pip install -r requirements.txt  # or replace with specific packages if no requirements.txt

# Install pygbm package itself
RUN pip install .  # or RUN pip install pygbm==0.1.0 if pygbm is in PyPI

# Command to run the package or an interactive shell
CMD ["python"]
