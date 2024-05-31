
# File Summary Backend

This is the backend repository of the project File Summary. This project is created for internship assignmnet. The project accepts csv/xslxx/xlxx file from the user and generates data and displays in record formate.


## Features

- Acceptes csv and xlsxx files
- Fast execution
- File storage


## Tech Stack

**Client:** React, Css

**Server:** Django


## Run Locally

Clone the project

```bash
  git clone https://github.com/KaustubhVaidya404/file_summary_backend.git
```

Go to the project directory

```bash
  cd src/
```

Install dependencies


```bash
  py -m pip -r requirements.txt
```

Start the server

```bash
  py ./manage.py runserver
```


## Installation

Please create virtual environment to avoid conflicts

```bash
  py -m venv env
```
    
## API Reference


#### POST item

```
  POST /api/v1/upload/

  {"headers": {"Content-Type": "multipart/form-data"}}
```