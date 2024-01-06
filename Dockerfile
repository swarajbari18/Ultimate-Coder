FROM python:3.11.3-slim-buster
COPY . /coder
WORKDIR /coder
EXPOSE 6000
RUN apt update -y && python -m pip install --upgrade pip && pip install -r requirements.txt
CMD [ "streamlit", "run", "app.py", "--server.port=6000", "server.address=0.0.0.0" ]