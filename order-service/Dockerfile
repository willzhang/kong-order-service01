FROM python:3.9-slim
WORKDIR /app
COPY app.py .
RUN pip install flask requests
EXPOSE 5001
ENV GATEWAY_URL=http://192.168.73.11:8000
CMD ["python", "app.py"]
