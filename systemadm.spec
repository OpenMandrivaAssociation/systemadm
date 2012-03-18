Summary:	System and Service Manager UI for systemd
Name:		systemadm
Version:	0
Release:	1
License:	GPLv2+
Group:		System/Configuration/Boot and Init
URL:		http://www.freedesktop.org/wiki/Software/systemd
Source0:	http://www.freedesktop.org/software/systemd/systemd-ui-%{version}.tar.xz
Patch0:		systemd-ui-0-linkage_fix.diff
BuildRequires:	autoconf automake m4 libtool
BuildRequires:	pkgconfig(dbus-1)
BuildRequires:	pkgconfig(gee-1.0)
BuildRequires:	pkgconfig(gio-unix-2.0)
BuildRequires:	pkgconfig(glib-2.0)
BuildRequires:	pkgconfig(gtk+-2.0)
BuildRequires:	pkgconfig(libnotify)
BuildRequires:	vala >= 0.11
BuildRequires:	xsltproc

%description
systemadm is a graphical frontend for the systemd system and service manager
and allows introspection and control of systemd

%prep

%setup -q -n systemd-ui-%{version}
%patch0 -p0

%build
autoreconf -fi

%configure2_5x
%make

%install

%makeinstall_std

install -d %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/systemadm.desktop <<EOF
[Desktop Entry]
Name=Graphical front-end for systemd
Comment=Modify systemd configuration
Exec=systemadm
Terminal=false
Type=Application
Icon=development_tools_section
Categories=GTK;Settings;System;X-MandrivaLinux-CrossDesktop;
EOF

%files
%{_bindir}/systemadm
%{_bindir}/systemd-gnome-ask-password-agent
%{_mandir}/man1/systemadm.*
%{_datadir}/applications/systemadm.desktop

