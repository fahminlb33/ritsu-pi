# ritsu-pi

> Ritsu-Pi almost reached it's first version! (1) One more component to implement (Samba), (2) fix idempotence in the playbook, and (3) better documentation before first release!
> That's still a lot I think :smile:

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
- [x] JDownloader
- [x] qBittorrent
- [x] DNSCrypt
- [x] Pi-Hole
- [x] Reverse proxy (nginx)
- [x] Jellyfin
- [x] Plex Media Server
- [x] Samba Server

See [INSTALL.MD](./INSTALL.MD) for step by step installation guide.

### :eyes: Maybe in the future

I'm also planning to include other apps especially for home entertainment:tv:

- [ ] Radarr
- [ ] Sonarr
- [ ] Lidarr
- [ ] Bazarr
- [ ] Jackett/Prowlarr

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
