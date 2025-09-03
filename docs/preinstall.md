# Before Installing

Before installing Ritsu-Pi with all of it's containers, I encountered several problems with running it after hitting a number of containers and virtual network interfaces. Follow this guide first to avoid this possible problems.

## IP lease is lost when Pi is using DHCP

This happens when I installed all Ritsu-Pi components. It turns out the `dhcpcd` service can overflow and causes the `eth0` interface of your Pi to lose it's IP address. Note that this only becomes a problem if you're using DHCP to configure your Pi IP address. Apparently this is because Docker creates many virtual network adapter and it's messing up with `dhcpcd` service. To solve this, the easiest way is to ignore `veth*` interfaces, which are created by Docker.

Steps:

1. `sudo vim /etc/dhcpcd.conf`
2. Add this line at the TOP of the file: `denyinterfaces veth*`
3. Save the config file
4. `sudo systemctl daemon-reload`
5. `sudo systemctl restart dhcpcd.service`

Source: https://github.com/raspberrypi/linux/issues/4092#issuecomment-774512217

## No internet when using DNSCrypt + Pi-Hole after Pi reboot

This is also a problem with DHCP. If your Pi is configured using DHCP, when you set your Pi IP address as DHCP server in your router, that means your Pi will also use it's own IP to resolve DNS queries. See the problem? In the end your Pi can't do any DNS resolution because it doesn't have a working upstream DNS resolver.

The solution again is to make your Pi DNS static by editing the `/etc/dhcpcd.conf`.

1. `sudo vim /etc/dhcpcd.conf`
2. Add this line: `static domain_name_servers=1.1.1.1`
3. Save and `sudo systemctl restart dhcpcd.service`

You can also change your `/etc/resolv.conf` but this settings usually gets overwritten by `dhcpcd`.

So in the end, the DHCP service is the root of all the problems above. Make sure to configure your DHCP settings correctly or make your Pi network settings static.

## Disabling `systemd-resolved` to free up port 53 for Pi-Hole

You can follow the answer described in this [Unix Stackexchange](https://unix.stackexchange.com/questions/676942/free-up-port-53-on-ubuntu-so-custom-dns-server-can-use-it).
