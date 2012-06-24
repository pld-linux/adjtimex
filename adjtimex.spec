Summary:	A utility for adjusting kernel time variables.
Summary(pl):	Narz�dzie do regulacji zmiennych czasu kernela.
Name:		adjtimex
Version:	1.12
Release:	1
Exclusiveos:	Linux
Copyright:	distributable
Group:		Base
Group(pl):	Podstawowe
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/admin/time/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Adjtimex is a kernel clock management program, which the superuser may
use to correct any drift in the system's clock. Users can use adjtimex
to view the time variables.

%description -l pl
Program zarz�dzaj�cy zegarem j�dra.
Root mo�e u�y� go do korekcji zegara systemowego, natomiast u�ytkownik
mo�e skorzysta� tylko z podgl�du zmiennych czasu.

%prep
%setup -q

%build
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT/sbin
install -d $RPM_BUILD_ROOT%{_mandir}/man8

install -s adjtimex	$RPM_BUILD_ROOT/sbin
install adjtimex.8	$RPM_BUILD_ROOT%{_mandir}/man8/%{name}.8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man*/* README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) /sbin/%{name}
%{_mandir}/man8/*.gz
