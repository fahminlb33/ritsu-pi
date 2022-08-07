# ritsu-pi

:construction: THIS PROJECT IS STILL WORK IN PROGRESS. :construction: IT MAY NOT WORK CORRECTLY FOR THE TIME BEING. :construction:

ritsu-pi is a collectioin of Ansible playbook to build your own Raspberry Pi cluster with various monitoring and apps. You can build a home media server, download servers, seedbox, or even create a kubernetes cluster (in the future, I hope!).

To allow an easy deployment and maintenance, *almost* all of the apps included in ritsu-pi is running on top of Docker. With this approach you can easily update and customize your setup. But this also comes with a down side, you will need a recent version of Raspberry Pi because it is power hungry and I personally use Pi 4 Model B. You can use older version but you might experience some performance degradation.

> This project is heavily inspired from [internet-pi](https://github.com/geerlingguy/internet-pi), cheers to [@geerlingguy](https://github.com/geerlingguy) for his awesome project!

## :battery: Batteries included

ritsu-pi packed quite a bunch of apps for your pi server. Docker is mandatory and everything else is optional and can be configured via `config.yml`.

- [x] Docker :strawberry:
- [x] Prometheus :whale:
- [x] Node Exporter :strawberry:
- [ ] Blackbox Exporter :whale:
- [x] cAdvisor :whale:
- [x] Grafana :whale:
- [ ] DNSCrypt :whale:
- [ ] Pi-Hole :whale:
- [ ] JDownloader :whale:
- [ ] qBittorrent :whale:
- [ ] Ookla SpeedTest :whale:

Note: unchecked items means I want to implement them and I already have a plan but I haven't got the time to write and test the playbook yet.

### :eyes: Maybe in the future

I'm also planning to include other apps especially for home entertainment:tv:

- [ ] Kodi
- [ ] Radarr
- [ ] Sonarr
- [ ] Lidarr
- [ ] Bazarr
- [ ] Jacket/Prowlarr

## :tea: Setup

Everything is automated using Ansible, so rest easy:smile:

1. [Install Ansible](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html). If you're on Linux (especially Debian-based) you can install it via Pip `pip3 install ansible`
2. Install Ansible plugins `ansible-galaxy collection install -r ansible-requirements.yml`
3. Clone this repository `git clone https://github.com/fahminlb33/ritsu-pi.git`
4. Copy the `config.yml.example` to `config.yml` and pick what app you want to install
5. Copy the `inventory.yml.example` to `inventory.yml` and add your Pi hosts
6. Run the playbook with `ansible-playbook -i inventory.yml main.yml`

### :put_litter_in_its_place: Uninstall Guide

Because ritsu-pi is mostly installed on Docker, you can use Docker commands to delete all the containers, images, and volumes installed by ritsu-pi.

```sh
# stop the containers
docker stop grafana prometheus

# remove the containers
docker rm grafana prometheus

# delete volume used by the container
# the volume name is container name + '_data' suffix
docker volume rm grafana_data prometheus_data

# delete images from config.yml
docker image rm grafana/grafana:latest
```

Some tools are installed to your Pi host because it can't be containerized or it requires special permissions or access that is not optimal to be run inside containers. You have to delete those apps manually.

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
