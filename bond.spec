Summary:	Building object network databases
Summary(pl.UTF-8):   Sieciowe obiektowe bazy danych
Name:		bond
Version:	2.0.9
Release:	0.1
License:	GPL v2
Group:		Development
Source0:	http://bond.treshna.com/%{name}-%{version}.tar.gz
# Source0-md5:	08b033a93d8b1a123a1be5fe112ac521
URL:		http://bond.treshna.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	libgda-devel
BuildRequires:	libtool
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	postgresql-devel
Requires:	libxml2 >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bond is a rapid application development (RAD) tool for Linux that
allows you to create network database programs quickly and easily.

%description -l pl.UTF-8
Bond jest narzędziem RAD dla Linuksa pozwalającym szybko i łatwo
tworzyć sieciowe bazy danych.

%package -n bonddb
Summary:	Building object network databases - database
Summary(pl.UTF-8):   Sieciowe obiektowe bazy danych - baza danych
Group:		Development

%description -n bonddb
DB part of Bond.

%description -n bonddb -l pl.UTF-8
Część bazodanowa Bonda.

%prep
%setup -q -n %{name}

%build
cd bonddb
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure \
	--enable-mysql=yes \
	--enable-gda=yes \
	--with-gnu-ld \
	--with-pic
%{__make}

cd ../bond
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}

# initscript and its config
%attr(754,root,root) /etc/rc.d/init.d/%{name}
%config(noreplace) %verify(not md5 mtime size) /etc/sysconfig/%{name}

%files -n bonddb
%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
