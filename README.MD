# ritsu-pi

ritsu-pi is a collectioin of Ansible playbook to build your own homelab with various monitoring and apps. You can build a home media server, download servers, seedbox, or just about anything. To allow an easy deployment and maintenance, *almost* all of the apps included in ritsu-pi is running on top of Docker. With this approach you can easily update and customize your setup.

> This project is heavily inspired from [internet-pi](https://github.com/geerlingguy/internet-pi), cheers to [@geerlingguy](https://github.com/geerlingguy) for his awesome project!

> **September 2025 Update** I'm upgrading my homelab and no longer use Raspberry Pi for my main server. Rest assured, this project should still work with Raspberry Pi.

## :battery: Batteries included

ritsu-pi packed quite a bunch of apps for your pi server. Docker is mandatory and everything else is optional and can be configured via `config.yml`.

- [x] Docker
- [x] AdBlock
  - [x] DNSCrypt
  - [x] Pi-Hole
- [x] Downloaders
  - [x] Gluetun VPN
  - [x] JDownloader
  - [x] qBittorrent
  - [x] Sabnzbd
- [x] Arr Stack
  - [x] Prowlarr
  - [x] Lidarr
  - [x] Sonarr
  - [x] Radarr
  - [x] Bazarr
- [x] Jellyfin
- [x] Immich
- [x] Monitoring
  - [x] Portainer
  - [x] Grafana
  - [x] Prometheus
  - [x] Node Exporter
  - [x] cAdvisor Exporter
  - [x] Blackbox Exporter
  - [x] SpeedTest Exporter
  - [x] Mikrotik Exporter
  - [x] apcupsd Exporter
  - [x] Smartctl Exporter
- [x] Flame Dashboard
- [x] MLflow
- [x] PostgreSQL
- [x] Samba Server

See [the docs](./docs/install.md) for step by step installation guide.

### :question: Why is it named "ritsu?"

I'm glad you asked.

Ritsu is a name inspired by two characters from two anime I have watched.

- Ritsu: a computer AI character from Assasination Classroom designed to kill Koro-sensei (military AI computer).
- Ritsuko: a scientist from Neon Genesis Evangelion who created the MAGI super computer.

I like the idea of building smart devices and AI and stuff and the name *ritsu* just comes to mind one day:laughing:

## License

Apache License version 2.0

## Author

Created by [Fahmi Noor Fiqri](https://www.kodesiana.com/).
