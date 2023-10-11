
```bash
cat << 'EOF' | sudo tee /etc/yum.repos.d/tuxclocker-nvidia-plugin.repo
[tuxclocker-nvidia-plugin]
name=repo for tuxclocker-nvidia-plugin owned by solopasha
baseurl=https://github.com/solopasha/tuxclocker-nvidia-plugin/raw/master/repo/fedora-$releasever-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://github.com/solopasha/tuxclocker-nvidia-plugin/raw/master/RPM-GPG-KEY-pmanager
repo_gpgcheck=0
enabled=1
enabled_metadata=1
EOF

sudo dnf in tuxclocker-nvidia-plugin
```
