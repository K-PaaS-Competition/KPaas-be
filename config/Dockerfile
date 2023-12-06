FROM python:3
WORKDIR /usr/src/app

RUN python -m venv venv
ENV settings config.settings.prod
RUN /bin/bash -c "source venv/bin/activate"
COPY requirements.txt .
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "config.wsgi:application"]