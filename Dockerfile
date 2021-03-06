FROM python:3

RUN pip install --upgrade pip
RUN pip install torch==1.5.1+cpu torchvision==0.6.1+cpu -f https://download.pytorch.org/whl/torch_stable.html
RUN apt-get update
RUN apt-get install 'ffmpeg' 'libgl1-mesa-glx'\
    'libsm6'\ 
    'libxext6'  -y
    
# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python app.py
