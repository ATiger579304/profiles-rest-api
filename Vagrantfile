# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://vagrantcloud.com/search.
  config.vm.box = "ubuntu/bionic64"
  # Pin this to a specific version to avoid breakage from any new updates
  # Can change this later
  config.vm.box_version = "~> 20200304.0.0"
# Maps port from local machine to our server
# guest is development server
# host is our local machine [This laptop]
  config.vm.network "forwarded_port", guest: 8001, host: 8001
# Allows scripts to be run when server first created
# this disables auto update so it does not conflict with sudo below
  config.vm.provision "shell", inline: <<-SHELL
    systemctl disable apt-daily.service
    systemctl disable apt-daily.timer
# this keeps local repositories up to date with new available packages
    sudo apt-get update
    sudo apt-get install -y python3-venv zip
# Create bash aliases file and set Python as the default box_version

    touch /home/vagrant/.bash_aliases
    if ! grep -q PYTHON_ALIAS_ADDED /home/vagrant/.bash_aliases; then
      echo "# PYTHON_ALIAS_ADDED" >> /home/vagrant/.bash_aliases
      echo "alias python='python3'" >> /home/vagrant/.bash_aliases
    fi
  SHELL
end
