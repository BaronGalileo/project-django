FROM python



WORKDIR /django/src

COPY ./requirements.txt /django/requirements.txt
RUN pip install -r /django/requirements.txt

COPY . /django/src

# EXPOSE 8000
#
# CMD ["python", "manage.py", "migrate"]
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]