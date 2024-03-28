from library.celery import celery_app

@celery_app.task
def test_task():
    print("Hello World Celery!")