#
# Conditional build:
%bcond_without	static_libs	# static library

Summary:	GNOME Internet Radio Locator
Summary(pl.UTF-8):	GNOME Internet Radio Locator - program do wyszukiwania rozgłośni internetowych
Name:		girl
Version:	9.2.0
Release:	1
License:	LGPL v2.1+
Group:		Applications/System
Source0:	http://ftp.gnome.org/pub/GNOME/sources/girl/9.2/%{name}-%{version}.tar.xz
# Source0-md5:	d23c41f924332b02d8f6df55bf348d46
URL:		https://wiki.gnome.org/Apps/Girl
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	gnome-vfs2-devel >= 2.0
BuildRequires:	gtk+2-devel >= 2.0
BuildRequires:	gtk-doc >= 1.16
BuildRequires:	intltool >= 0.50.1
BuildRequires:	libgnome-devel >= 2.0
BuildRequires:	libgnomecanvas-devel >= 2.0
BuildRequires:	libgnomeui-devel >= 2.0
BuildRequires:	libxml2-devel >= 2.0
BuildRequires:	pkgconfig
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRequires:	yelp-tools
Suggests:	streamripper
Suggests:	totem
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Girl, the GNOME Internet Radio Locator program, allows users to easily
find live radio programs on radio broadcasters on the Internet.

%description -l pl.UTF-8
Girl (GNOME Internet Radio Locator) to program pozwalający
użytkownikom łatwo wyszukać programy internetowych rozgłości radiowych
nadających na żywo.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# it's exactly the same as C
%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/help/en_US

%find_lang %{name} --with-gnome

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog HACKING LETTER NEWS* README THANKS TODO YP-DIRS
%attr(755,root,root) %{_bindir}/girl
%{_datadir}/appdata/girl.appdata.xml
%{_datadir}/girl
%{_desktopdir}/girl.desktop
%{_iconsdir}/hicolor/*x*/apps/girl.png
%{_mandir}/man1/girl.1*
