FROM python:3.7
WORKDIR /opt/ask-google
RUN pip install --upgrade pip
RUN	pip install pipwin
# RUN apt-get install python-gnuradio-audio-portaudio
RUN apt-get update \
        && apt-get install libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1-dev -y \
        && pip3 install pyaudio
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY audio/* audio/
COPY audio.py .
COPY commands.py .
COPY get_answer.py .
CMD python audio.py
EXPOSE 5000/tcp