# C:\Users\username>cd weatherapp
# C:\Users\username\weatherapp>python manage.py migrate
# C:\Users\username\weatherapp>python manage.py runserver
# Browse on internet: http://127.0.0.1:8000/

import os
import sys


def main():
    """Run administrative tasks."""
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weatherapp.settings")
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == "__main__":
    main()
