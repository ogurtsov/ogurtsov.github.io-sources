Title: Vagrantfile for OpenCV and Python
Date: 2015-10-09 10:37
Category: Blog
Tags: opencv, python, vagrant

I use the following script to create an Ubuntu 15.04 Vagrant box with OpenCV with Python bindings support:

```
# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/vivid64"
  #config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.provision "shell", inline: <<-SHELL

    version="$(wget -q -O - http://sourceforge.net/projects/opencvlibrary/files/opencv-unix | egrep -m1 -o '\"[0-9](\.[0-9])+' | cut -c2-)"
    echo "Installing OpenCV" $version
    mkdir OpenCV
    cd OpenCV
    echo "Removing any pre-installed ffmpeg and x264"
    sudo apt-get -qq remove ffmpeg x264 libx264-dev
    sudo add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu vivid main multiverse"
    sudo add-apt-repository "deb http://us.archive.ubuntu.com/ubuntu precise main universe"
    sudo apt-get update
    echo "Installing Dependencies"
    sudo apt-get -qq install libopencv-dev build-essential checkinstall cmake pkg-config yasm libjpeg-dev libjasper-dev libavcodec-dev libavformat-dev libswscale-dev libdc1394-22-dev libxine-dev libgstreamer0.10-dev libgstreamer-plugins-base0.10-dev libv4l-dev python-dev python-numpy libtbb-dev libqt4-dev libgtk2.0-dev libfaac-dev libmp3lame-dev libopencore-amrnb-dev libopencore-amrwb-dev libtheora-dev libvorbis-dev libxvidcore-dev x264 v4l-utils ffmpeg libxvidcore4

    wget -O OpenCV-$version.zip http://sourceforge.net/projects/opencvlibrary/files/opencv-unix/$version/opencv-"$version".zip/download
    echo "Installing OpenCV" $version
    unzip OpenCV-$version.zip
    cd opencv-$version
    mkdir build
    cd build
    cmake -D CMAKE_BUILD_TYPE=RELEASE -D CMAKE_INSTALL_PREFIX=/usr/local -D WITH_TBB=ON -D BUILD_NEW_PYTHON_SUPPORT=ON -D WITH_V4L=ON -D INSTALL_C_EXAMPLES=ON -D INSTALL_PYTHON_EXAMPLES=ON -D BUILD_EXAMPLES=ON -D WITH_QT=ON -D WITH_OPENGL=ON ..
    make -j2
    sudo checkinstall
    sudo sh -c 'echo "/usr/local/lib" > /etc/ld.so.conf.d/opencv.conf'
    sudo ldconfig

    echo "OpenCV" $version "ready to be used"

    sudo apt-get install -y python-opencv
    sudo ln /dev/null /dev/raw1394

  SHELL
   
end
```