%define emacs_sitestart_d  %{_sysconfdir}/emacs/site-start.d
%define spectool_version   1.0.9

Name:           rpmdevtools
Version:        6.4
Release:        %mkrel 1
Summary:        RPM Development Tools

Group:          System/Configuration/Packaging 
# rpmdev-setuptree is GPLv2, everything else GPLv2+
License:        GPL
URL:            http://fedoraproject.org/
Source0:        %{name}-%{version}.tar.bz2
Source1:        http://people.redhat.com/nphilipp/spectool/spectool-%{spectool_version}.tar.bz2

BuildArch:      noarch
Provides:       spectool = %{spectool_version}
Obsoletes:      fedora-rpmdevtools < 5.0
# Minimal RPM build requirements
Requires:       bash
Requires:       bzip2
Requires:       coreutils
Requires:       cpio
Requires:       diffutils
Requires:       findutils
Requires:       gawk
Requires:       gcc
Requires:       gcc-c++
Requires:       grep
Requires:       gzip
Requires:       info
Requires:       make
Requires:       patch
Requires:       redhat-release
Requires:       rpm-mandriva-setup-build
Requires:       rpm-build >= 4.4.2.1
Requires:       sed
Requires:       tar
Requires:       unzip
Requires:       util-linux
Requires:       which
# Additionally required for tool operations
#Requires:      cpio
Requires:       fakeroot
Requires:       file
Requires:       perl
Requires:       python
Requires:       rpm-python
#Requires:      sed
Requires:       wget

%description
This package contains scripts and (X)Emacs support files to aid in
development of RPM packages.
rpmdev-setuptree    Create RPM build tree within user's home directory
rpmdev-diff         Diff contents of two archives
rpmdev-newspec      Creates new .spec from template
rpmdev-rmdevelrpms  Find (and optionally remove) "development" RPMs
rpmdev-checksig     Check package signatures using alternate RPM keyring
rpminfo             Print information about executables and libraries
rpmdev-md5          Display the md5sum of all files in an RPM
rpmdev-vercmp       RPM version comparison checker
spectool            Expand and download sources and patches in specfiles
rpmdev-wipetree     Erase all files within dirs created by rpmdev-setuptree
rpmdev-extract      Extract various archives, "tar xvf" style
...and many more.


%prep
%setup -q -a 1
%{__cp} -a spectool*/README README.spectool

%build
%{configure2_5x} --libdir=%{_prefix}/lib
%{make}

%install
%{__rm} -rf %{buildroot}

%{makeinstall_std}

%{__cp} -a spectool*/spectool %{buildroot}%{_bindir}

%{__mkdir_p} %{buildroot}%{emacs_sitestart_d}
%{__ln_s} %{buildroot}%{_datadir}/rpmdevtools/rpmdev-init.el %{buildroot}%{emacs_sitestart_d}/rpmdev-init.el
#/bin/touch %{buildroot}%{emacs_sitestart_d}/rpmdev-init.elc

%{__chmod} 755 %{buildroot}%{_datadir}/rpmdevtools/{trap.sh,template.init,tmpdir.sh}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc COPYING README*
%config(noreplace) %{_sysconfdir}/rpmdevtools/
%{_datadir}/rpmdevtools/
%attr(0755,root,root) %{_bindir}/rpm*
%attr(0755,root,root) %{_bindir}/spectool
%config(noreplace) %{emacs_sitestart_d}/rpmdev-init.el*
%{_mandir}/man[18]/rpm*.[18]*

