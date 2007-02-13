Summary:	OpenOffice.org 2 Quickstarter
Summary(pl.UTF-8):	Szybszy start OpenOffice.org 2
Name:		oooqs2
Version:	1.0.1
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/segfaultskde/%{name}-%{version}.tar.gz
# Source0-md5:	6b5cf0d2a6497ff5210242d55e467e6f
Patch0:		%{name}-desktop.patch
URL:		http://segfaultskde.berlios.de/oooqs/
BuildRequires:	automake
BuildRequires:	kdebase-devel >= 3.0.5a
BuildRequires:	qt-devel >= 3.0.5
BuildRequires:	rpmbuild(macros) >= 1.129
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
OpenOffice.org2 Quickstarter is a small application that runs in the
KDE SystemTray. It is used to quickly start the different
OpenOffice.org 2 modules without having to go through the K-Menu.

%description -l pl.UTF-8
Szybszy start OpenOffice.org 2 jest małą aplikacją, która uruchamia
się w KDE System Tray. Można go używać do przyśpieszania startu
modułów OpenOffice.org 2 bez wchodzenia w menu.

%prep
%setup -q
%patch0 -p0

%build
export CXXFLAGS="%{rpmcflags} -fno-exceptions -fno-rtti"

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir=%{_kdedocdir} \
	shelldesktopdir=%{_desktopdir}/kde

%find_lang oooqs --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f oooqs.lang
%defattr(644,root,root,755)
%doc AUTHORS
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/[!l]*/*/*/*
%{_desktopdir}/kde/*.desktop
%{_datadir}/autostart/*.desktop
