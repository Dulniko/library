# library

## Code formatting
The code is formatted using yapf. To format the code, run the following command:
```bash
yapf -i <file_name>
```
To format all the files in a directory, run the following command:
```bash 
yapf -ri <directory_name>
```

## Unit tests
Unit tests are run using pytest. To run the tests, run the following command:
```bash
pytest
```

## Database
The database is a postgresql database. To create the database in container, run the following command:
```bash
invoke run-postgres
```

## Asynchronous tasks
Asynchronous tasks are run using celery and redis as the message broker. To run the redis server, run the following command:
```bash
docker run -d -p 6379:6379 redis
```
To run the celery worker, run the following command:
```bash
celery -A library worker --loglevel=info
```
