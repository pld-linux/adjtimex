Summary:	A utility for adjusting kernel time variables.
Summary(pl):	Narz�dzie do regulacji zmiennych czasu kernela.
Name:		adjtimex
Version:	1.12
Release:	1
License:	Distributable
Group:		Base
Group(de):	Gr�nds�tzlich
Group(pl):	Podstawowe
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/admin/time/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
Adjtimex is a kernel clock management program, which the superuser may
use to correct any drift in the system's clock. Users can use adjtimex
to view the time variables.

%description -l fr
Adjtimex est un programme de gestion de l'horloge du kernel, que le
superutilisateur peut utiliser pour corriger l'horloge syst�me. Les
utilisateurs peuvent utiliser adjtimex pour afficher les variables
temporelles.

%description -l pl
Program zarz�dzaj�cy zegarem j�dra. Root mo�e u�y� go do korekcji
zegara systemowego, natomiast u�ytkownik mo�e skorzysta� tylko z
podgl�du zmiennych czasu.

%prep
%setup -q

%build
autoconf
%configure 
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install adjtimex $RPM_BUILD_ROOT%{_sbindir}
install adjtimex.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
