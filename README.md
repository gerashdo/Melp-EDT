# Melp-EDT

Melp is an API designed to provide restaurant information.

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Python 3.10 or higher.
- PostgreSQL installed on your machine.

### Clone the Repository

Clone the project repository using the following command:
```
git clone https://github.com/gerashdo/Melp-EDT.git
```

### Set Up a Virtual Environment
It is recommended to use a virtual environment to manage project dependencies. Create a virtual environment named 'venv' with the following command:

```
python -m venv venv
```

Activate the virtual environment:
```
source venv/bin/activate
```

The requirements are listed in the **requirements.txt** file. Also you can install them with the following command:
```
pip install -r requirements.txt
```

### Database Setup
- Ensure PostgreSQL is installed on your machine.
- Create a PostgreSQL database with your preferred name.
- Enable the PostGIS extension in the newly created database with this SQL command:

```
CREATE EXTENSION postgis;
```
This allows to use the postgis functions in the database.


Set the database URL in the .env file following the format:

```
DATABASE_URL=postgresql://<user>:<password>@localhost:5432/<database_name>
```

### Run the project
Start the project with the following command:
```
uvicorn main:app --reload
```
The tables will be created automatically in the database.
Access to the url shown in the console to access the endpoints. It usually is:
```
http://127.0.0.1:8000
```

## API Documentation
When the project is running, access the API documentation at:
```
http://127.0.0.1:8000/docs
```

## Acknowledgments

- [FastAPI](https://fastapi.tiangolo.com/) - FastAPI framework.
- [PostgreSQL](https://www.postgresql.org/) - Database management system.
- [PostGIS](https://postgis.net/) - Spatial database extender for PostgreSQL.
