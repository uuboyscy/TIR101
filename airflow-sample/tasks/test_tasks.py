from airflow.decorators import task

# from utils.my_notifier import send_message


@task
def do_something(some_str: str) -> list[str]:
    # send_message()
    return list(some_str)
