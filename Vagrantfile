Vagrant.configure(2) do |config|

  config.vm.box = "ubuntu/xenial64"

  config.vm.provider "virtualbox" do |vb|
    vb.memory = "2048"
  end

  config.vm.network "forwarded_port", guest: 8000, host: 8000

  config.vm.synced_folder "./", "/home/vagrant/packtpub"

  config.vm.provision "shell", inline: <<-SHELL
    apt-get update -o Acquire::CompressionTypes::Order::=gz
    apt-get upgrade -y
    apt-get update -y
    apt-get install tree -y
  SHELL

end
