#!/bin/bash -e

# Prepare apt-get for usage
. /helper/scripts/apt-get/update.sh

packages=()
packages+=("python-dev")
packages+=("python-virtualenv")
packages+=("git")
packages+=("libjpeg-dev")
packages+=("zlib1g-dev")
apt-get install -y "${packages[@]}"

# pillow jpegi and zlib support hack
ln -s /usr/lib/x86_64-linux-gnu/libjpeg.so /usr/lib
ln -s /usr/lib/x86_64-linux-gnu/libz.so /usr/lib

# install scitran.data dependencies
pip install \
    numpy==1.9.0 \
    pytz \
    pillow \
    git+https://github.com/scitran/pydicom.git@0.9.9_value_vr_mismatch \
    git+https://github.com/nipy/nibabel.git \
    git+https://github.com/moloney/dcmstack.git@6d49fe01235c08ae63c76fa2f3943b49c9b9832d \
    git+https://github.com/scitran/data.git

# clone scripts
git clone https://github.com/scitran/scripts.git /root/scripts

# Bake script in for now
cp ./run ./scripts/run

# Cleanup
. /helper/scripts/apt-get/clean.sh
