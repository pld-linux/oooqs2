Summary:	OpenOffice.org 2 Quickstarter
Summary(pl):	Szybszy start OpenOffice.org 2
Name:		oooqs2
Version:	1.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://download.berlios.de/segfaultskde/%{name}-%{version}.tar.gz
# Source0-md5:	e7bac61aced37e3801335d4370b39aaf
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

%description -l pl
Szybszy start OpenOffice.org 2 jest ma³± aplikacj±, która uruchamia siê w
KDE System Tray. Mo¿na go u¿ywaæ do przy¶pieszania startu modu³ów 
OpenOffice.org 2 bez wchodzenia w menu.

%prep
%setup -q
%patch0 -p1

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

%find_lang oooqs --all-name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f oooqs.lang
%defattr(644,root,root,755)
#%doc AUTHORS ChangeLog README TODO
%attr(755,root,root) %{_bindir}/*
%{_iconsdir}/[!l]*/*/*/*
%{_desktopdir}/kde/*.desktop
%{_datadir}/autostart/*.desktop
%{_docdir}/kde/HTML/*/%{name}
