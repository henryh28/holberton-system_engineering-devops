# Fixes the type in wp-settings.php to change from phpp to php
exec { 'Fix phpp typo':
  path    => '/usr/bin/:/usr/sbin/:/bin/',
  command => 'sed -i s/phpp/php/ /var/www/html/wp-settings.php'
}
