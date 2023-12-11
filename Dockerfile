FROM python:3.11.6-slim-bullseye

WORKDIR /flaskapi

RUN pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118
RUN pip3 install ultralytics
RUN pip3 install opencv-python-headless
RUN pip3 install flask

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]