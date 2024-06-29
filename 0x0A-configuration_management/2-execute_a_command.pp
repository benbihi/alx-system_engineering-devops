#!/usr/bin/env ruby

exec { 'kill_killmenow_process':
  command     => 'pkill -f killmenow',
  path        => ['/bin', '/usr/bin'],
  refreshonly => true,
  subscribe   => Service['killmenow_service'],
}
