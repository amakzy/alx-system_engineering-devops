# This is a comment explaining what the Puppet manifest does
# 0-create_a_file.pp

file { '/tmp/school':
  ensure     => 'file',
  mode      => '0744',
  owner     => 'www-data',
  group     => 'www-data',
  content   => 'I love Puppet',
}
