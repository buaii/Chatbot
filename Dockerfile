FROM python:latest

WORKDIR /usr/src/app

COPY requiremets.txt ./

RUN pip install --no-cache-dir -r requiremets.txt

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]