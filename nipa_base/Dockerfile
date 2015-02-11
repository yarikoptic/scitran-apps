FROM ubuntu-debootstrap:trusty

# Configures neurodebian repositories for all software packages, which includes softare that may not be
# Debian Free Software Guidelines (DFSG) compliant.
RUN echo 'deb http://neurodeb.pirsquared.org data main contrib non-free' > /etc/apt/sources.list.d/neurodebian.sources.list
RUN echo '#deb-src http://neurodeb.pirsquared.org data main contrib non-free' >> /etc/apt/sources.list.d/neurodebian.sources.list
RUN echo 'deb http://neurodeb.pirsquared.org trusty main contrib non-free' >> /etc/apt/sources.list.d/neurodebian.sources.list
RUN echo '#deb-src http://neurodeb.pirsquared.org trusty main contrib non-free' >> /etc/apt/sources.list.d/neurodebian.sources.list
RUN apt-key adv --recv-keys --keyserver hkp://pgp.mit.edu:80 2649A5A9

RUN apt-get update && apt-get -y install python-dev \
   python-virtualenv \
   git \
   libjpeg-dev \
   octave \
   afni \
   fsl-core \
   ants \
   itksnap \
   python-numpy \
   python-scipy \
   python-nipype \
   python-nibabel \
   python-dipy \
   python-nitime \
   python-nipy \
   mrtrix \
   mrtrix-doc \
   mricron \
   mriconvert \
   gifti-bin \
   dicomnifti \
   nifti2dicom \
   qnifti2dicom

# pillow jpeg support hack
RUN ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib

# install scitran.data dependencies
RUN pip install \
    numpy==1.9.0 \
    pymongo \
    pillow \
    git+https://github.com/scitran/pydicom.gitmirror.git@value_mismatch \
    git+https://github.com/nipy/nibabel.git \
    git+https://github.com/moloney/dcmstack.git \
    git+https://github.com/scitran/data.git

# clone scripts
RUN git clone https://github.com/scitran/scripts.git /root/scripts

ENTRYPOINT ["/bin/bash"]
