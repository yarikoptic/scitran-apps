FROM ubuntu-debootstrap:trusty

RUN apt-get update && apt-get -y install python-dev \
   python-virtualenv \
   git \
   libjpeg-dev \
   zlib1g-dev

# pillow jpegi and zlib support hack
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
RUN ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

# install scitran.data dependencies
RUN pip install \
    numpy==1.9.0 \
    pytz \
    pillow \
    git+https://github.com/scitran/pydicom.git@0.9.9_value_vr_mismatch \
    git+https://github.com/nipy/nibabel.git \
    git+https://github.com/moloney/dcmstack.git@6d49fe01235c08ae63c76fa2f3943b49c9b9832d \
    git+https://github.com/scitran/data.git

# clone scripts
RUN git clone https://github.com/scitran/scripts.git /root/scripts

COPY ./run ./scripts/run

ENTRYPOINT ["/scripts/run"]
