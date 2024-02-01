from contextlib import contextmanager
from django.core.management import call_command


@contextmanager
def load_fixture(fixtures):
    for fixture in fixtures:
        call_command("loaddata", fixture, verbosity=0)
    yield
    call_command("flush", verbosity=0, interactive=False)