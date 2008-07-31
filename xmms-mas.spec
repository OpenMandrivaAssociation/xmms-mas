%define name xmms-mas
%define version 1.2.7
%define release %mkrel 6
%define fname %name-%version-2

Summary: MAS output plugin for xmms 
Name: %{name}
Version: %{version}
Release: %{release}
Source0: %{fname}.tar.bz2
Patch: xmms-mas-1.2.7-2-includes.patch
License: GPL
Group: Sound
URL: http://www.mediaapplicationserver.net/indexframes.html
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: libmas-devel
BuildRequires: libxmms-devel
Requires: xmms
ExcludeArch: x86_64

%description
This is an output plugin for XMMS. If you use it, XMMS will send its
output (raw PCM data) to MAS.

You can run XMMS on you computer alongside other audio-enabled apps
that also talk to MAS!! Using this plugin also automatically adds
network transparency to XMMS!!!

%prep
%setup -q -n %fname
%patch -p1 -b .includes

%build
gcc -DVERSION=\"%version\" -c `xmms-config --cflags` mas_client.c
gcc -shared -o libmas-client.so mas_client.o `xmms-config --libs` -lpthread -lmas -lmasc -lmas_jrtp -Wl,-soname -Wl,libmas-client.so

%install
rm -rf $RPM_BUILD_ROOT
install -D -m 755 libmas-client.so %buildroot%_libdir/xmms/Output/libmas-client.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
%_libdir/xmms/Output/libmas-client.so

