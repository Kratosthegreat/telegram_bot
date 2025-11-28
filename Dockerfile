FROM python:3.11
WORKDIR /app
COPY . .
RUN pip install fastapi uvicorn openai
EXPOSE 6400
CMD ["uvicorn","server:app","--host","0.0.0.0","--port","6400"]
