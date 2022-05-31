FROM python:3.9

#RUN cd ~ && mkdir .deepface && cd .deepface && mkdir weights
#COPY ./weights/* ~/.deepface/weights/

WORKDIR /app

COPY requirements.txt ./
# RUN pip install --no-cache-dir -r requirements.txt
RUN pip uninstall opencv-python
RUN pip install -r requirements.txt

COPY . /app

CMD [ "python", "server.py" ]
