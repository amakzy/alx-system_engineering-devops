package { 'flask':
  ensure  => '2.1.0',
  provider => 'pip3',
  requires => [ Package['werkzeug'] ],  # Make sure werkzeug is installed first
}

package { 'werkzeug':
  ensure  => '2.1.1',  # Replace with compatible Werkzeug version
  provider => 'pip3',
}
