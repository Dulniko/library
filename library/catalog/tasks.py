from library.celery import celery_app


@celery_app.task
def test_task(*args, **kwargs):
    print("Hello from test_task")
    return f"args: {args}, kwargs: {kwargs}"
