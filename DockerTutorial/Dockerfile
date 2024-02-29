FROM python:alpine
WORKDIR /app
RUN pip install flask
COPY . /app
ENV FLASK_APP=app.py
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]