## Firewall

Configure a firewall on container server

|          *Filenames*            |            *Descriptions*                                               |
|---------------------------------|-------------------------------------------------------------------------|
| 0-firewall_ABC                  | Answer file                                                             |
| 1-block_all_incoming_traffic_but| Commands used to configure UFW on remote server                         |
| 100-port_forwarding             | UFW config file with port forwarding from :8080 to :80                  |

Reference links: 
https://linode.com/docs/security/firewalls/configure-firewall-with-ufw/

https://serverfault.com/questions/238563/can-i-use-ufw-to-setup-a-port-forward

## Author
Henry Hsu
