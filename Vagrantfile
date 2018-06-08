# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "bento/ubuntu-17.10"

  # Flask
  config.vm.network "forwarded_port", guest: 5000, host: 5000

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  # Provision python development environment
  config.vm.provision "shell", inline: <<-SHELL
    export HOME=/home/vagrant
    apt-get update
    apt-get install -yq \
      build-essential \
      python3 \
      python3-dev \
      postgresql-contrib \
      postgresql \
    
    curl https://bootstrap.pypa.io/get-pip.py | sudo -H python3

    curl -sL https://deb.nodesource.com/setup_10.x | sudo -E bash -
    apt-get install -y nodejs

    su vagrant -c 'cd /vagrant &&
                   make venv/setup &&
                   source venv/bin/activate &&
                   make pip/update &&
                   make db/create &&
                   make npm/update &&
                   make npm/build &&
                   make flask/app'
  SHELL
end
