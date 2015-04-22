FROM ubuntu-debootstrap:trusty

RUN apt-get update && apt-get -y install python-dev \
   python-virtualenv \
   git \
   libjpeg-dev

# pillow jpeg support hack
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib

# install scitran.data dependencies
RUN pip install \
    numpy==1.9.0 \
    pymongo \
    pillow \
    git+https://github.com/scitran/pydicom.git@0.9.9_value_vr_mismatch \
    git+https://github.com/nipy/nibabel.git \
    git+https://github.com/moloney/dcmstack.git@6d49fe01235c08ae63c76fa2f3943b49c9b9832d \
    git+https://github.com/scitran/data.git

# clone scripts
RUN git clone https://github.com/scitran/scripts.git /root/scripts

COPY ./dcm2nii /usr/bin/dcm2nii

ENTRYPOINT ["/usr/bin/dcm2nii"]
