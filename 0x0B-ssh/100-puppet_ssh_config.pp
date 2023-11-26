# Create a 

$data = "# Sample SSH Configuration File

Host alx_server
    HostName 100.25.46.33
    User ubuntu
    IdentityFile ~/.ssh/school
	
# Disable password authentication globally
PasswordAuthentication no"

file { 'ssh_config':
  ensure  => 'present',
  path => '~/.ssh/config',
  content => $data,
}
