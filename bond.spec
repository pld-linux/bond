#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_without	tests		# build without tests
#
Summary:	-
Summary(pl):	-
Name:		bond
Version:	2.0.9
Release:	0.1
License:	GPL v2
#Vendor:		-
Group:		-
#Icon:		-
Source0:	http://bond.treshna.com/%{name}-%{version}.tar.gz
# Source0-md5:	08b033a93d8b1a123a1be5fe112ac521
#Source1:	-
#Source1-md5:	-
#Patch0:		%{name}-what.patch
URL:		http://bond.treshna.com/
BuildRequires:	libxml2-devel >= 2.6.0
BuildRequires:	postgresql-devel 
#PreReq:		-
#Requires(pre,post):	-
#Requires(preun):	-
#Requires(postun):	-
Requires:	libxml2 >= 2.6.0
#Provides:	-
#Obsoletes:	-
#Conflicts:	-
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Bond is a rapid application development (RAD) tool for linux that allows you to create network database programs quickly and easily. With this new version comes major updates in Bond XML format, and a move away from the use of C code completely! This means you can create powerful database programs quickly, only requiring knowledge of XML and SQL.

%description -l pl

#%package subpackage
#Summary:	-
#Summary(pl):	-
#Group:		-

#%description subpackage

#%description subpackage -l pl

%prep
%setup -q -n %{name}
#%patch0 -p1

%build
# if ac/am/* rebuilding is necessary, do it in this order and add
# appropriate BuildRequires

for pack in bonddb bond; do

cd $pack
#%{__gettextize}
#%{__libtoolize}
#%{__aclocal}
#%{__autoconf}
#%{__autoheader}
#%{__automake}
%configure
%{__make}

cd ..
done

%install
rm -rf $RPM_BUILD_ROOT
# create directories if necessary
#install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%pre

%post

%preun

%postun

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

#%files subpackage
#%defattr(644,root,root,755)
#%doc extras/*.gz
#%{_datadir}/%{name}-ext
