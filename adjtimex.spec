Summary:	A utility for adjusting kernel time variables.
Name:		adjtimex
Version:	1.3
Release:	7
Exclusiveos:	Linux
Copyright:	distributable
Group:		System Environment/Base
Source:		ftp://sunsite.unc.edu/pub/Linux/system/admin/time/adjtimex-1.3.tar.gz
Patch:		adjtimex-1.3-glibc.patch
Buildroot:	/tmp/%{name}-%{version}-root

%description
Adjtimex is a kernel clock management program, which the
superuser may use to correct any drift in the system's clock.  Users can
use adjtimex to view the time variables.

%prep
%setup -q
%patch -p1

%build
%configure 
make

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{/sbin,%{_mandir}/man8}

install -s adjtimex $RPM_BUILD_ROOT/sbin/adjtimex
install adjtimex.man $RPM_BUILD_ROOT%{_mandir}/man8/adjtimex.8

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man8/adjtimex.8 README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.gz
%attr(755,root,root) /sbin/adjtimex
%{_mandir}/man8/adjtimex.8.gz
