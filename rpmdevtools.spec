%global _emacs_sitestartdir %{_datadir}/emacs/site-lisp/site-start.d
%global spectool_version 1.0.10

%global __reqires_exclude_from %{_bindir}/spectool
%global __requires_exclude /usr/bin/perl

Summary:	RPM Development Tools
Name:		rpmdevtools
Version:	8.10
Release:	5
# rpmdev-setuptree is GPLv2, everything else GPLv2+
License:	GPLv2+ and GPLv2
URL:		https://fedorahosted.org/rpmdevtools/
Source0:	https://fedorahosted.org/released/rpmdevtools/%{name}-%{version}.tar.xz
BuildArch:	noarch
# help2man, pod2man, *python for creating man pages
BuildRequires:	help2man
BuildRequires:	python >= 3
BuildRequires:	python-rpm
# emacs-common >= 1:22.3-3 for macros.emacs
BuildRequires:	emacs-common
Provides:	spectool = %{spectool_version}
Requires:	curl
Requires:	diffutils
Requires:	fakeroot
Requires:	file
Requires:	findutils
Requires:	gawk
Requires:	grep
Requires:	python >= 3
Requires:	python-rpm
Requires:	sed
Suggests:	emacs-common
Suggests:	rpm-build >= 4.4.2.3

%description
This package contains scripts and (X)Emacs support files to aid in
development of RPM packages.
rpmdev-setuptree    Create RPM build tree within user's home directory
rpmdev-diff         Diff contents of two archives
rpmdev-newspec      Creates new .spec from template
rpmdev-rmdevelrpms  Find (and optionally remove) "development" RPMs
rpmdev-checksig     Check package signatures using alternate RPM keyring
rpminfo             Print information about executables and libraries
rpmdev-md5/sha*     Display checksums of all files in an archive file
rpmdev-vercmp       RPM version comparison checker
spectool            Expand and download sources and patches in specfiles
rpmdev-wipetree     Erase all files within dirs created by rpmdev-setuptree
rpmdev-extract      Extract various archives, "tar xvf" style
rpmdev-bumpspec     Bump revision in specfile
...and many more.


%prep
%setup -q

%build
%configure --libdir=%{_prefix}/lib
%make_build

%install
%make_install

for dir in %{_emacs_sitestartdir} ; do
  install -dm 755 $RPM_BUILD_ROOT$dir
  ln -s %{_datadir}/rpmdevtools/rpmdev-init.el $RPM_BUILD_ROOT$dir
  touch $RPM_BUILD_ROOT$dir/rpmdev-init.elc
done

%files
%doc COPYING NEWS
%config(noreplace) %{_sysconfdir}/rpmdevtools/
%{_sysconfdir}/bash_completion.d/
%{_datadir}/rpmdevtools/
%{_bindir}/*
%{_emacs_sitestartdir}/rpmdev-init.el
%ghost %{_emacs_sitestartdir}/rpmdev-init.elc
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*
