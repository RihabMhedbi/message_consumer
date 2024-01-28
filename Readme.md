# Running the Consumer Project

## Prerequisites

Before running the project, ensure you have the following installed on your system:

- Python 3.8 or higher
- Pip (Python package installer)
- RabbitMQ (Message broker for Celery)

## Setup Instructions

1. **Clone the Repository:**
   ```bash
    cd consumer_project
    python3 -m venv env
    source env/bin/activate
    pip install -r requirements.txt
   ```

2. **Run migrations:**
    ```bash
    python manage.py makemigrations
    python manage.py migrate
   ```
3. **Create super user:**
   ```bash
    python manage.py createsuperuser
   ```
4. **Run Celery worker:**
   ```bash
      celery -A consumer_project worker -l info
    ```

5. **Environment variables:**
   
   - PRODUCER_URL: url of the producer project instance
   - PRODUCER_API_KEY: api key created in producer project admin dashboard