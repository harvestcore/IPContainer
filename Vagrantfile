Vagrant.configure("2") do |config|
  config.vm.box = "google/gce"

  config.vm.provider :google do |google, override|
    google.google_project_id = ENV['PROJECT_ID']
    google.google_client_email = ENV['CLIENT_EMAIL']
    google.google_json_key_location = ENV['JSON_KEY_LOCATION']
    
    google.image_family = 'ubuntu-1604-lts'
    google.zone = 'europe-west2-a'
    google.name = 'ipcontainer'
    google.machine_type = 'g1-small'
    
    override.ssh.username = 'aagomezies'
    override.ssh.private_key_path = '~/.ssh/id_rsa'
    # override.ssh.private_key_path = '~/.ssh/google_compute_engine'
  end

end