# Scitran Apps

- clone this repo
- build the nipa_base image.
    `docker build --tag scitran/nipa-base:latest ./nipa_base`
- build the dcm2nii image.
    `docker build --tag scitran/dcm2nii:latest ./dcm2nii`

## Neuro Image Processing Apps
Words, words, words.  Something, something, something dark side.  Put useful words here.

## Note
Neuro Image Processing apps can share a common base image that has several common tools pre-installed.
The downside to this is that every container is HUGE. Most containers will only use some, most likely one, of the tools installed.
