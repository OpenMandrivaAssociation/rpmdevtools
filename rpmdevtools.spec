%global _emacs_sitestartdir %{_datadir}/emacs/site-lisp/site-start.d
%global spectool_version 1.0.10

Name:		rpmdevtools
Version:	8.4
Release:	9
Summary:	RPM Development Tools

# rpmdev-setuptree is GPLv2, everything else GPLv2+
License:	GPLv2+ and GPLv2
URL:		https://fedorahosted.org/rpmdevtools/
Source0:	https://fedorahosted.org/released/rpmdevtools/%{name}-%{version}.tar.xz

BuildArch:	noarch
# help2man, pod2man, *python for creating man pages
BuildRequires:	help2man
BuildRequires:	python >= 2.4
BuildRequires:	python-rpm
# emacs-common >= 1:22.3-3 for macros.emacs
BuildRequires:	emacs-common
%if 0%{?fedora}
# xemacs-common >= 21.5.29-8 for macros.xemacs
BuildRequires: 	xemacs-common >= 21.5.29-8
%endif
Provides:	spectool = %{spectool_version}
Requires:	curl
Requires:	diffutils
Requires:	fakeroot
Requires:	file
Requires:	findutils
Requires:	gawk
Requires:	grep
Requires:	python >= 2.4
Requires:	rpm-build >= 4.4.2.3
Requires:	python-rpm
Requires:	sed
Requires:	emacs-common
%if 0%{?fedora}
Requires:	xemacs-filesystem
%endif

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
sed -i 's|/usr/bin/python|%__python2|' rpmdev*

%build
%configure --libdir=%{_prefix}/lib
make %{?_smp_mflags}


%install
%makeinstall_std

%if 0%{?fedora}
for dir in %{_emacs_sitestartdir} %{_xemacs_sitestartdir} ; do
%else
for dir in %{_emacs_sitestartdir} ; do
%endif
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
%if 0%{?fedora}
%{_xemacs_sitestartdir}/rpmdev-init.el
%ghost %{_xemacs_sitestartdir}/rpmdev-init.elc
%endif
%{_mandir}/man1/*.1*
%{_mandir}/man8/*.8*
