# lock-dependent tests fail in mock
# enable them on local builds by using --with locktests
%bcond_with locktests
# crash tests seem to stall
# use --with crashtests to try
%bcond_with crashtests

Name:           obnam
Version:        1.18.2
Release:        1%{?dist}
Summary:        An easy, secure backup program

License:        GPLv3+
URL:            http://obnam.org/
Source0:        http://code.liw.fi/debian/pool/main/o/%{name}/%{name}_%{version}.orig.tar.xz
# Portability fix for a unit test that uses Python 2.7 features
Patch0:         obnam-1.8-py26.patch

# build-time
BuildRequires:  cmdtest
BuildRequires:  genbackupdata
BuildRequires:  libattr-devel
BuildRequires:  python-coverage-test-runner
BuildRequires:  python2-devel
# some yarn tests fail due to not expecting SELinux xattrs
# BuildRequires:  python-markdown
BuildRequires:  summain
# build- and run-time dependencies
BuildRequires:  attr
BuildRequires:  gnupg
BuildRequires:  python-cliapp
BuildRequires:  python-larch
BuildRequires:  python-paramiko
BuildRequires:  python-tracing
BuildRequires:  python-ttystatus
BuildRequires:  PyYAML

Requires:       attr
Requires:       gnupg
Requires:       python-cliapp
Requires:       python-larch
Requires:       python-paramiko
Requires:       python-tracing
Requires:       python-ttystatus
Requires:       PyYAML
# requires EPEL repo
Requires:       fuse-python

# we don't want to provide private python extension libs
# http://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Arch-specific_extensions_to_scripting_languages
%{?filter_setup:
%filter_provides_in %{python_sitearch}/obnamlib/_obnam.so 
%filter_setup
}

%description
Obnam is an easy, secure backup program. Backups can be stored on
local hard disks, or online via the SSH SFTP protocol. The backup
server, if used, does not require any special software, on top of SSH.

Some features that may interest you:

 * Snapshot backups. Every generation looks like a complete snapshot,
   so you don't need to care about full versus incremental backups, or
   rotate real or virtual tapes.

 * Data de-duplication, across files, and backup generations. If the
   backup repository already contains a particular chunk of data, it
   will be re-used, even if it was in another file in an older backup
   generation. This way, you don't need to worry about moving around
   large files, or modifying them.

 * Encrypted backups, using GnuPG.

Obnam can do push or pull backups, depending on what you need. You can
run Obnam on the client, and push backups to the server, or on the
server, and pull from the client over SFTP. However, access to live
data over SFTP is currently somewhat limited and fragile, so it is not
recommended.


%prep
%setup -q
%if 0%{?el6}
%patch0 -p1 -b .py26
%endif


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# fix permission
chmod 755 %{buildroot}%{python_sitearch}/obnamlib/_obnam.so


%check
./check \
       --unit-tests \
%if %{with locktests}
       --lock-tests \
%endif
%if %{with crashtests}
       --crash-tests
%endif


%files
%doc COPYING NEWS README
%{_mandir}/man1/obnam*.1*
%{_bindir}/obnam*
%{python_sitearch}/*


%changelog
* Thu Jan 7 2016 Stephen Dunne <sedunne@nexcess.net> - 1.18-1
- Update to 1.18

* Tue Oct  6 2015 Michel Salim <salimma@fedoraproject.org> - 1.17-1
- Update to 1.17

* Thu Sep 10 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.16-1
- Update to 1.16

* Fri Sep  4 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.15-1
- Update to 1.15

* Sun Aug  9 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.13-2
- Fix spec typo - PyYAML should be listed as Requires (bz# 1251619)

* Sun Aug  2 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.13-1
- Update to 1.13

* Sun Jul 19 2015 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.12-1
- Update to 1.12

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.8-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Tue Dec  2 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.8-1
- Update to 1.8

* Sun Aug 17 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.6.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Thu Jan 16 2014 Michel Salim <salimma@fedoraproject.org> - 1.6.1-1
- Update to 1.6.1

* Sat Sep 28 2013 Michel Salim <salimma@fedoraproject.org> - 1.5-1
- Update to 1.5

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.4-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Sun Mar 17 2013 Michel Salim <salimma@fedoraproject.org> - 1.4-1
- Update to 1.4

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 1.3-1
- Update to 1.3

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Tue Oct 16 2012 Michel Salim <salimma@fedoraproject.org> - 1.2-1
- Update to 1.2

* Sat Sep 15 2012 Michel Salim <salimma@fedoraproject.org> - 1.1-1
- Update to 1.1

* Tue Jun 19 2012 Michel Salim <salimma@fedoraproject.org> - 1.0-2
- Remove redundant %%{python_sitearch} declaration
- Use upstream's check script instead of manually setting up the environment

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 1.0-1
- Initial package
