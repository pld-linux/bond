#
# Conditional build:
#%bcond_with	tests		# build with tests
#%bcond_without	tests		# build without tests
#
Summary:	building object network databases
Summary(pl):	Sieciowe obiektowe bazy danych
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
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	postgresql-devel
BuildRequires:	libgda-devel
Requires:	libxml2 >= 2.6.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bond is a rapid application development (RAD) tool for linux that
allows you to create network database programs quickly and easily.

%description -l pl
Bond jest narzêdziem RAD dla linuksa które pozwola tworzyæ sieciowe
bazy danych szybko i ³atwo.

%package -n bonddb
Summary:	building object network databases -- database
Summary(pl):	Sieciowe obiektowe bazy danych -- bazadanych
Group:		Development

%description -n bonddb
DB part of Bond.

%description -n bonddb -l pl
Czê¶æ bazodanowa Bonda

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
%configure --enable-mysql=yes --enable-gda=yes --with-gnu-ld --with-pic
%{__make}

cd ..

cd bond
%{__gettextize}
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}
cd ..

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS CREDITS ChangeLog NEWS README THANKS TODO

# if _sysconfdir != /etc:
#%%dir %{_sysconfdir}
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
