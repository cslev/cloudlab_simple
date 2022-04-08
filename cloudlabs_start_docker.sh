#!/bin/bash
#COLORIZING
none='\033[0m'
bold='\033[01m'
disable='\033[02m'
underline='\033[04m'
reverse='\033[07m'
strikethrough='\033[09m'
invisible='\033[08m'

black='\033[30m'
red='\033[31m'
green='\033[32m'
orange='\033[33m'
blue='\033[34m'
purple='\033[35m'
cyan='\033[36m'
lightgrey='\033[37m'
darkgrey='\033[90m'
lightred='\033[91m'
lightgreen='\033[92m'
yellow='\033[93m'
lightblue='\033[94m'
pink='\033[95m'
lightcyan='\033[96m'

#change this if needed
USERNAME="csikorl"

DEPS="libc6 tshark tcpdump nano tar bzip2 wget lsb-release screen procps apt-transport-https ca-certificates curl gnupg-agent software-properties-common mc git ethtool"

PYTHON_DEPS="python3 libpython3-dev"

sudo echo -e "\n\n${reverse}${red}Installing is still in progess...!${disable}${none}" | sudo tee /etc/motd
sudo echo -e "tail -f /tmp/install.log" | sudo tee -a /etc/motd

echo -e "Installing requirements..." | sudo tee -a /tmp/install.log


sudo dpkg-reconfigure debconf --frontend=noninteractive

sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends $DEPS
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends $PYTHON_DEPS

#installing docker
echo -e "Installing docker..." | sudo tee -a /tmp/install.log

arch=$(dpkg -l |grep linux-image-generic|awk '{print $4}')
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo apt-key add -
sudo add-apt-repository \
   "deb [arch=$arch] https://download.docker.com/linux/ubuntu \
   $(lsb_release -cs) \
   stable"
sudo apt-get update
sudo DEBIAN_FRONTEND=noninteractive apt-get install -y --no-install-recommends docker-ce docker-ce-cli containerd.io

#create dir /mnt to obtain more disk space
sudo mkdir -p /mnt/extra

echo -e "Installing docker-compose..." | sudo tee -a /tmp/install.log


if [ "$arch" == "arm64" ] 
then
  sudo DEBIAN_FRONTEND=noninteractive apt-get install -y docker-compose
  sudo ln -s /usr/bin/docker-compose  /usr/local/bin/docker-compose
  #there is no extra TB storage for ARMs, but we still work in /mnt/extra
else
  #installing docker-compose
  sudo curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
  sudo chmod +x /usr/local/bin/docker-compose

  echo -e "Requesting extra 1TB storage..." | sudo tee -a /tmp/install.log

  #request more space (random around 1TB)
  sudo /usr/local/etc/emulab/mkextrafs.pl /mnt/extra
fi

# get into /mnt/extra
cd /mnt/extra
sudo mkdir -p /mnt/extra/docker

echo -e "Cloning quic_doh_docker github repo for docker-compose.yml file..." | sudo tee -a /tmp/install.log

#get doh_docker source for docker-compose.yaml
sudo git clone https://github.com/cslev/quic_doh_docker

#build container
#sudo docker build -t cslev/doh_docker:arm64v8 -f Dockerfile.arm64 .

echo -e "Adjusting permissions on /mnt/extra..." | sudo tee -a /tmp/install.log
sudo chown -R $USERNAME /mnt/extra
sudo chmod -R 777 /mnt/extra
systemctl restart docker


echo -e "Adjusting docker system to use /mnt/extra instead of /var/lib to avoid consuming the root partition" | sudo tee -a /tmp/install.log
echo 'DOCKER_TMPDIR="/mnt/extra/docker-tmp"' >> /etc/default/docker
sudo cp /local/repository/source/others/daemon.json /etc/docker/
systemctl daemon-reload

echo -e "Downloading prebuilt image from docker hub..." | sudo tee -a /tmp/install.log

#get doh_docker image
sudo docker pull cslev/quic_doh_docker:latest

echo -e "Final minor adjustments..." | sudo tee -a /tmp/install.log

sudo cp /local/repository/source/others/bashrc_template /root/.bashrc
# sudo source /root/.bashrc
sudo cp /local/repository/source/others/bashrc_template /users/$USERNAME/.bashrc
sudo echo "${USERNAME}   ALL= NOPASSWD:/usr/sbin/tcpdump" | sudo tee -a /etc/sudoers
sudo apt-get install -f -y
sudo apt-get autoremove -y


sudo echo -e "\n\n${reverse}${green}Installation finished\n\$PATH=${PATH}!${disable}${none}" | sudo tee /etc/motd
sudo echo -e "\n\n${reverse}${green}Don't forget to disable NIC offloading features: \nethtool -K eno49 rx off tx off gso off tso off gro off \n(iface might be different!)${disable}${none}" | sudo tee -a /etc/motd

sudo echo -e "\n\n${reverse}${green}Installation finished\n\$PATH=${PATH}!${disable}${none}" | sudo tee -a /tmp/install.log
sudo echo -e "\n\n${reverse}${green}Don't forget to disable NIC offloading features: \nethtool -K eno49 rx off tx off gso off tso off gro off \n(iface might be different!)${disable}${none}" | sudo tee -a /tmp/install.log


