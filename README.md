# Apache Airflow with Docker Compose

This repository contains a setup for running Apache Airflow using Docker Compose. It allows you to quickly spin up an Airflow environment, including a web server, scheduler, and PostgreSQL as the metadata database.

## Prerequisites

Before you begin, ensure you have the following installed:

- **Docker** (version 19.03.12+)
- **Docker Compose** (version 1.27.0+)

## Setup and Usage

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name

### 2. Initialize Airflow
Initialize the Airflow environment by running the following command:

```bash
docker-compose up airflow-init

### 3. Start Airflow
Once the initialization is complete, you can start all the Airflow services by running:
```bash
docker-compose up

### Airflow Services
- **Airflow Webserver**: Accessible at [http://localhost:8080](http://localhost:8080)
- **Airflow Scheduler**: Responsible for scheduling jobs
- **PostgreSQL**: Airflow's metadata database
- **Flower**: Airflow's monitoring tool (optional)

### 4. Access the Airflow UI
Open your browser and go to [http://localhost:8080](http://localhost:8080). The default login credentials are:

- **Username**: `airflow`
- **Password**: `airflow`

You can change these credentials in the `docker-compose.yaml` file under the `AIRFLOW__CORE__FERNET_KEY` and `AIRFLOW__CORE__SQL_ALCHEMY_CONN` variables.

### 5. Stopping Airflow
To stop the Airflow services, run:
```bash
docker-compose down
