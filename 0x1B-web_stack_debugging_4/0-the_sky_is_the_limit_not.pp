# Increase Ulimit in /etc/default/nginx file
exec { 'increase_ulimit':
  command => 'sed -i "s/15/3000/g" /etc/default/nginx; sudo service nginx restart',
  path    => '/bin:/sbin:/usr/bin:/usr/sbin:/usr/local/bin:/usr/local/sbin'
}
# Ref: https://www.cyberciti.biz/faq/linux-unix-nginx-too-many-open-files
# (fix in article did not work, fix in comments by Ryan Pendergast worked)
