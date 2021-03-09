FROM continuumio/miniconda

RUN apt-get update 
RUN apt-get install -y git
RUN apt-get install -y gcc

WORKDIR /app354
RUN git clone https://github.com/Masetto97/Symbolic-Melody-Identification.git

WORKDIR ./Symbolic-Melody-Identification
RUN git pull

RUN conda init bash

RUN conda env create -f requirements.yml

RUN  conda run -n IA pip install --upgrade https://github.com/Theano/Theano/archive/master.zip
RUN  conda run -n IA pip install --upgrade https://github.com/Lasagne/Lasagne/archive/master.zip
RUN  conda run -n IA pip install scikit-learn==0.20.4
RUN  conda run -n IA pip install matplotlib==2.2.5

RUN  conda run -n IA ./terminal_client.py --rebuild nn_kernels_mozart.pkl cnn_parameters.json model.pkl
EXPOSE 10000
EXPOSE 8888



#CMD ["python","terminal_client.py --rebuild nn_kernels_mozart.pkl cnn_parameters.json model.pkl"]
