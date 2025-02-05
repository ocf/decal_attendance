FROM python:3.11

WORKDIR /server

COPY requirement.txt .
COPY server.py .

RUN pip install -r requirement.txt

EXPOSE 80

CMD ["fastapi", "run", "server.py", "--port", "80"]
