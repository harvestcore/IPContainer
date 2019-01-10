Vagrant.configure("2") do | config |

  # Defino máquina "ipcontainer"
  config.vm.define "ipcontainer" do | ipcontainer |
    
    # Máquina base.
    config.vm.box = "google/gce"
    
    # Versión de la máquina.
    config.vm.box_version = "0.1.0"
    
    # Evito que Vagrant busque actualizaciones de la máquina base.
    config.vm.box_check_update = false

    # Configuración de la máquina.
    ipcontainer.vm.provider "google" do | gcloud, override |

      # Configuración de las credenciales de Google Cloud.
      gcloud.google_project_id = ENV['PROJECT_ID']
      gcloud.google_client_email = ENV['CLIENT_EMAIL']
      gcloud.google_json_key_location = ENV['JSON_KEY_LOCATION']
      
      # Configuración básica de la VM
      gcloud.image_family = 'ubuntu-1604-lts'
      gcloud.zone = 'europe-west2-a'
      gcloud.name = 'ipcontainer'
      gcloud.machine_type = 'g1-small'
      
      # Configuración usuario y clave privada SSH.
      override.ssh.username = "aagomezies"
      override.ssh.private_key_path = '~/.ssh/id_rsa'
    end
  
    # Provisionamiento con Ansible.
    config.vm.provision "ansible" do | ans |
      ans.playbook = "provision/playbook.yml"
    end
  end
end