Summary: A utility for adjusting kernel time variables.
Name: adjtimex
Version: 1.3
Release: 6
Exclusiveos: Linux
Copyright: distributable
Group: System Environment/Base
Source: ftp://sunsite.unc.edu/pub/Linux/system/admin/time/adjtimex-1.3.tar.gz
Patch: adjtimex-1.3-glibc.patch
Buildroot: /var/tmp/%{name}-root

%description
Adjtimex is a kernel clock management program, which the
superuser may use to correct any drift in the system's clock.  Users can
use adjtimex to view the time variables.

%prep
%setup -q
%patch -p1 -b .glibc

%build
CFLAGS="$RPM_OPT_FLAGS" ./configure 
make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/sbin
mkdir -p $RPM_BUILD_ROOT/usr/man/man8
install -s -m755 adjtimex $RPM_BUILD_ROOT/sbin/adjtimex
install -m644 adjtimex.man $RPM_BUILD_ROOT/usr/man/man8/adjtimex.8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README
/sbin/adjtimex
/usr/man/man8/adjtimex.8
