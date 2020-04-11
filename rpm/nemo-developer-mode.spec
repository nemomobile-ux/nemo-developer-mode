Name:		nemo-developer-mode
Version:	0.1
Release:	1
Summary:	Developmer mode files

Group:		Development/Tools
License:	GPLv2
URL:		https://github.com/nemomobile/nemo-developer-mode
Source0:	%{name}-%{version}.tar.bz2
Requires:	coreutils
Requires:	sudo
Requires:	openssh-server
#Becouse name of DEVELOPER MODE hardcoded
Provides:	jolla-developer-mode
BuildArch:	noarch

%description
%{summary}.

%prep
%setup -q -n %{name}-%{version}

%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %{buildroot}/lib/systemd/system/multi-user.target.wants/
mkdir -p %{buildroot}/var/lib/jolla-developer-mode/preloaded/
mkdir -p %{buildroot}/usr/bin
mkdir -p %{buildroot}/etc/connman/firewall.d/
mkdir -p %{buildroot}/etc/usb-moded/dyn-modes/
mkdir -p %{buildroot}/etc/sudoers.d/

install -m 755 src/devel-su %{buildroot}/usr/bin
install -m 644 src/00-devlmode-fw.conf %{buildroot}/etc/connman/firewall.d/
install -m 644 src/devmode_connecting.ini %{buildroot}/etc/usb-moded/dyn-modes/
install -m 655 src/sudo_nemo %{buildroot}/etc/sudoers.d/

cd %{buildroot}/lib/systemd/system/multi-user.target.wants/
ln -s ../sshd.service

%files
%defattr(-,root,root,-)
%dir /var/lib/jolla-developer-mode/preloaded/
%{_bindir}/devel-su
/lib/systemd/system/multi-user.target.wants/*
%config %{_sysconfdir}/connman/firewall.d/00-devlmode-fw.conf
%config %{_sysconfdir}/usb-moded/dyn-modes/devmode_connecting.ini
%{_sysconfdir}/sudoers.d/sudo_nemo
