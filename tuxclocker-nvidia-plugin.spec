%global __provides_exclude_from ^(%{_libdir}/%{name}/plugins/.*\\.so)$

Name:           tuxclocker-nvidia-plugin
Version:        1.1.0
Release:        %autorelease
Summary:        The nvidia plugin for tuxclocker

License:        GPL-3.0-only
URL:            https://github.com/Lurkki14/tuxclocker
Source:         %{url}/archive/%{version}/%{name}-%{version}.tar.gz
Patch:          lib.patch

BuildRequires:  tuxclocker
BuildRequires:  boost-devel
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  libXNVCtrl-devel
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xext)
BuildRequires:  xorg-x11-drv-nvidia-cuda-libs
BuildRequires:  meson
BuildRequires:  pkgconfig(openssl)
BuildRequires:  cmake(FunctionalPlus)
BuildRequires:  cmake(mpark_patterns)

Requires:       tuxclocker%{?isa} = %{version}

%description
%{summary}.


%prep
%autosetup -n tuxclocker-%{version} -p1
mkdir -p src/include/deps/FunctionalPlus/include
mkdir -p src/include/deps/patterns/include
ln -svf %{_includedir}/mpark src/include/deps/patterns/include/mpark


%build
%meson \
    -Ddaemon=false \
    -Dinterfaces=false \
    -Dlibrary=false \
    -Dgui=false
%meson_build


%install
%meson_install


%files
%dir %{_libdir}/tuxclocker
%dir %{_libdir}/tuxclocker/plugins
%{_libdir}/tuxclocker/plugins/libnvidia.so


%changelog
%autochangelog
