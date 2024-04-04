from catalog.tasks import test_task


def test_test_task():
    async_result = test_task.delay(1, 2, 3, test="test").get()
    assert async_result == "args: (1, 2, 3), kwargs: {'test': 'test'}"
