#  a manifest that kills a process named killmenow
exec { 'pkill':
  command => 'pkill -f killmenow',
  path    => '/bin/bash',
  return  => [0, 1],
}
