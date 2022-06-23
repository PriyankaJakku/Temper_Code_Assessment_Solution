FROM python:3.10

WORKDIR /app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY Load_csv_data.py ./

CMD ["python","./Load_csv_data.py"]


