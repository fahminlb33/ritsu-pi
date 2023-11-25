# Port Mappings

The published port follows these convention:

- Web UI: 80xx
- Prometheus exporters: 81xx

| Service            | Container Port             | Published Port |
|--------------------|----------------------------|----------------|
| cAdvisor           | 8080                       | 8101           |
| DNSCrypt           | 5053 (UDP)                 | -              |
| Blackbox Exporter  | 9115                       | 8102           |
| Mikrotik Exporter  | 9115                       | 8103           |
| Node Exporter      | Not in container           | 8104           |
| Speedtest Exporter | 9798                       | 8105           |
| Grafana            | 3000                       | 8001           |
| Jellyfin           | 80                         | 8002           |
| Pi-Hole            | 80 (Web), 53 (UDP)         | 8003, 53       |
| Portainer          | 9000 (Web), 8000 (API)     | 8004           |
| Prometheus         | 9090                       | 8005           |
| qBittorrent        | 8080 (Web), 6881 (TCP/UDP) | 8006, 6881     |
| JDownloader 2      | 3129 (API), 5800           | 8007           |
| Samba Share        | Not in container           | 139, 445       |
