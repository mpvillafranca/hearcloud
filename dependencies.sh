#!/bin/bash

sudo apt-get -y install libjpeg-dev zlib1g-dev

sudo apt-get remove ffmpeg x264 libav-tools libvpx-dev libx264-dev

sudo apt-get update
sudo apt-get -y install build-essential checkinstall git libfaac-dev libgpac-dev libjack-jackd2-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev librtmp-dev libsdl1.2-dev libtheora-dev libva-dev libvdpau-dev libvorbis-dev libx11-dev libxfixes-dev pkg-config texi2html yasm zlib1g-dev

git clone --depth 1 git://git.videolan.org/x264
cd x264
./configure --enable-static
make
sudo checkinstall --pkgname=x264 --pkgversion="3:$(./version.sh | awk -F'[" ]' '/POINT/{print $4"+git"$5}')" --backup=no --deldoc=yes --fstrans=no --default

cd ..
wget http://downloads.sourceforge.net/opencore-amr/fdk-aac-0.1.4.tar.gz
tar xzvf fdk-aac-0.1.4.tar.gz
cd fdk-aac-0.1.4
./configure
make
sudo checkinstall --pkgname=fdk-aac --pkgversion="0.1.4" --backup=no --deldoc=yes --fstrans=no --default

cd ..
git clone --depth 1 https://chromium.googlesource.com/webm/libvpx
cd libvpx
./configure
make
sudo checkinstall --pkgname=libvpx --pkgversion="1:$(date +%Y%m%d%H%M)-git" --backup=no --deldoc=yes --fstrans=no --default

cd ..
git clone --depth 1 git://source.ffmpeg.org/ffmpeg
cd ffmpeg
./configure --enable-gpl --enable-libfaac --enable-libmp3lame --enable-libopencore-amrnb --enable-libopencore-amrwb --enable-librtmp --enable-libtheora --enable-libvorbis --enable-libvpx --enable-libx264 --enable-nonfree --enable-version3 --enable-x11grab
make
sudo checkinstall --pkgname=ffmpeg --pkgversion="5:$(date +%Y%m%d%H%M)-git" --backup=no --deldoc=yes --fstrans=no --default
hash x264 ffmpeg ffplay ffprobe
