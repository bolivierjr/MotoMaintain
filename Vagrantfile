# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure(2) do |config|
  config.vm.box = "ubuntu/trusty64"

  # Flask
  config.vm.network "forwarded_port", guest: 5000, host: 8000

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  # Provision python development environment
  config.vm.provision "shell", inline: <<-SHELL
    export HOME=/home/vagrant
    sudo apt-get update
    sudo apt-get install -yq \
      python3.6
      python-dev \
      postgresql-contrib
      postgresql \
      libpq-dev
    su vagrant -c 'cd /vagrant &&
                   make venv/setup &&
                   source venv/bin/activate &&
                   make pip/update &&
                   make db/create'
  SHELL
end
