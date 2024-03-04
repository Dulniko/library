from invoke import task


@task
def run_postgres(c):
    c.run(
        "docker run --name library -e POSTGRES_USER=library -e POSTGRES_PASSWORD=library -e POSTGRES_DB=library -p 5432:5432 -d postgres"
    )
