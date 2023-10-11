#!/bin/bash
set -euxo pipefail
shopt -s nullglob
shopt -s extglob

mkdir -p repo/fedora-$(rpm -E %fedora)-$(uname -m)
package=$1
VERSION="$(rpmspec -q --qf "%{version}-%{release}\n" "$package.spec" | head -1)"
echo "VERSION=$VERSION" >> $GITHUB_ENV
sudo -s -u builduser -- <<EOF
echo "%_gpg_name solopasha" >> ~/.rpmmacros
echo -n "$GPG_KEY" | base64 --decode | gpg --import
spectool -g "$package.spec"
rpmbuild -bs --define "_sourcedir ${PWD}" --define "_specdir ${PWD}" \
		--define "_builddir ${PWD}" --define "_srcrpmdir ${PWD}" --define \
		"_rpmdir ${PWD}" --define "_buildrootdir ${PWD}/.build" "$package.spec"
mock -r fedora-$(rpm -E %fedora)-$(uname -m)-rpmfusion_nonfree --rebuild "$package"-*.src.rpm
EOF
mv /var/lib/mock/fedora-$(rpm -E %fedora)-x86_64/result/!(*.src.rpm|*.log) repo/fedora-$(rpm -E %fedora)-$(uname -m)

createrepo_c repo/fedora-$(rpm -E %fedora)-$(uname -m)

git add repo/fedora-$(rpm -E %fedora)-$(uname -m)
git commit -am "update $VERSION"
git pull --rebase
git push
