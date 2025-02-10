FROM python:3.10-slim
LABEL maintainer=CodeRyo-Ryo
# Install cron job package
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    build-essential \
    gcc \
    libffi-dev \
    libssl-dev \
    linux-headers-generic \
    libx11-6 \
    libx11-dev \
    libxtst6 \
    git \
    vim \ 
    curl \
    postgresql-client

RUN apt-get update && apt-get install -y cron
# Set environment variable
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
# Set work directory
COPY requirements.txt /tmp/
RUN pip install --no-cache-dir -r /tmp/requirements.txt
# Copy project
WORKDIR /web/
COPY . /web/
RUN  apt-get clean && rm -rf /var/lib/apt/lists/*
CMD ["python", "manage.py", "migrate", "&&", "python", "manage.py", "runserver"]