FROM python:3.9

WORKDIR /app/src

RUN python -m venv myenv
RUN /bin/bash -c "source myenv/bin/activate"



COPY . /app/src/
COPY requirements.txt /app/src/

RUN pip install -r requirements.txt

CMD ["python","House_app/manage.py" ,"runserver","0.0.0.0:9000"]


