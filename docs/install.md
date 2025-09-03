# Installation Guide

Before installing, you MUST read the [pre-installation guide](./preinstall.md).

Everything is automated using Ansible, so rest easy:smile:

1. [Install uv](https://docs.astral.sh/uv/getting-started/installation/)
2. Clone the repo: `git clone https://github.com/fahminlb33/ritsu-pi.git`
3. Install Ansible using `uv sync`
4. Install Ansible roles from galaxy `ansible-galaxy collection install -r requirements.yml`
5. Copy the `secrets.yml.example` to `secrets.yml` and fill the passwords there
6. Edit the `inventory.yml` and add your server hosts
7. Optionally, you can edit the `site.yml` file to pick what app you want to install. Set the `state` to `present` to install it or `absent` to uninstall it.
8. Run the playbook: `ansible-playbook -i inventory.yml site.yml`

Even better, you can encrypt your `secrets.yml` using Ansible Vault.

```bash
touch secrets_pass
echo -n "my password" > secrets_pass

ansible-vault encrypt --vault-id production@secrets_pass secrets.yml

ansible-playbook --vault-id production@secrets_pass -i inventory.yml site.yml  
```

## Uninstall Guide

Usually you can just stop and delete the containers from Docker. But you can set the `state` to `absent` to uninstall it.
