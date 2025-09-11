FROM python:3.12

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY regression.joblib .
COPY web_servers.py .
CMD ["fastapi", "dev", "web_servers.py" ,"--host=0.0.0.0", "--port=5024"]

EXPOSE 5024
