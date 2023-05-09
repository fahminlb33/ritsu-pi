# ritsu-pi

:construction: THIS PROJECT IS STILL WORK IN PROGRESS. :construction:

ritsu-pi is a collectioin of Ansible playbook to build your own Raspberry Pi cluster with various monitoring and apps. You can build a home media server, download servers, seedbox, or even create a kubernetes cluster (in the future, I hope!).

To allow an easy deployment and maintenance, *almost* all of the apps included in ritsu-pi is running on top of Docker. With this approach you can easily update and customize your setup. But this also comes with a down side, you will need a recent version of Raspberry Pi because it is power hungry and I personally use Pi 4 Model B. You can use older version but you might experience some performance degradation.

> This project is heavily inspired from [internet-pi](https://github.com/geerlingguy/internet-pi), cheers to [@geerlingguy](https://github.com/geerlingguy) for his awesome project!

## :battery: Batteries included

ritsu-pi packed quite a bunch of apps for your pi server. Docker is mandatory and everything else is optional and can be configured via `config.yml`.

- [x] Docker
- [x] Prometheus
- [x] Grafana
- [x] Portainer
- [x] Node Exporter
- [x] Blackbox Exporter
- [x] cAdvisor Exporter
- [x] SpeedTest Exporter
- [x] Suhu Server Exporter :interrobang:
- [ ] DNSCrypt
- [ ] Pi-Hole
- [ ] JDownloader
- [ ] qBittorrent
- [ ] Jellyfin
- [ ] Samba Server

Note: unchecked items means I want to implement them and I already have a plan but I haven't got the time to write and test the playbook yet.

### :eyes: Maybe in the future

I'm also planning to include other apps especially for home entertainment:tv:

- [ ] Radarr
- [ ] Sonarr
- [ ] Lidarr
- [ ] Bazarr
- [ ] Jackett/Prowlarr

## :tea: Setup

Everything is automated using Ansible, so rest easy:smile:

1. [Install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html). If you're on Linux (especially Debian-based) you can install it via Pip `pip3 install ansible`
2. `ansible-galaxy collection install -r requirements.yml`
3. `git clone https://github.com/fahminlb33/ritsu-pi.git`
4. Copy the `config.yml.example` to `config.yml` and pick what app you want to install
5. Edit the `inventory.yml` and add your Pi hosts
6. `ansible-playbook -i inventory.yml site.yml` to install Ritsu-Pi

### :put_litter_in_its_place: Uninstall Guide

:construction: Uninstall guide is still work in progress :construction:

The current playbook does not include the ability to uninstall Ritsu-Pi, you have to stop and delete the container manually.
This feature will be included in the next release when all the roles are working properly.

### :question: Why is it named "ritsu?"

I'm glad you asked.

Ritsu is a name inspired by two characters from two anime I have watched.

- Ritsu: a computer AI character from Assasination Classroom designed to kill Koro-sensei (military AI computer).
- Ritsuko: a scientist from Neon Genesis Evangelion who created the MAGI super computer.

I like the idea of building smart devices and AI and stuff and the name *ritsu* just comes to mind one day:laughing:

## License

Apache License version 2.0

## Author

Created in 2022 by [Fahmi Noor Fiqri](https://www.kodesiana.com/).
