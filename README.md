# theatre_service
This project provides an API for managing theatre halls, plays, and tickets.

# Installing

Clone the repository:
```shell
git clone https://github.com/DimaYankovskiy/theatre_service.git
cd theatre_service
```

Setup virtual environment:
```shell
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

Apply migrations:
```shell
python manage.py migrate
```

Run:
```shell
python manage.py runserver
```

## Demo

![swagger](demo.png)