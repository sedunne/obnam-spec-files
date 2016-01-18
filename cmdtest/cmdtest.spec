Name:           cmdtest
Version:        0.12
Release:        1%{?dist}
Summary:        Black-box testing for Unix command line tools

License:        GPLv3+
URL:            http://liw.fi/%{name}/
Source0:        http://code.liw.fi/debian/pool/main/c/%{name}/%{name}_%{version}.orig.tar.gz

BuildArch:      noarch
BuildRequires:  python-coverage-test-runner
BuildRequires:  python-cliapp
# EL6's markdown does not have the needed extensions attribute
%if ! 0%{?el6}
BuildRequires:  python-markdown
%endif
BuildRequires:  python-ttystatus
Requires:       python-cliapp
Requires:       python-ttystatus

%description
cmdtest black box tests Unix command line tools. Roughly, it is given
a command line and input files, and the expected output, and it
verifies that the command line produces the expected output. If not,
it reports a problem, and shows the differences.


%prep
%setup -q


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%check
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
%{__python} setup.py check


%files
%doc COPYING NEWS README README.yarn
%{_bindir}/cmdtest
%{_bindir}/yarn
%{_mandir}/man1/cmdtest.1*
%if ! 0%{?el6}
%{_mandir}/man1/yarn.1*
%endif
%{python_sitelib}/*


%changelog
* Mon Apr 14 2014 Michel Salim <salimma@fedoraproject.org> - 0.12-1
- Update to 0.12

* Fri Sep 27 2013 Michel Salim <salimma@fedoraproject.org> - 0.9-1
- Update to 0.9

* Thu Jul  4 2013 Michel Salim <salimma@fedoraproject.org> - 0.8.3-1
- Update to 0.8.3

* Sun Mar 17 2013 Michel Salim <salimma@fedoraproject.org> - 0.6-1
- Update to 0.6

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 0.5-1
- Update to 0.5

* Sun Sep 16 2012 Michel Salim <salimma@fedoraproject.org> - 0.3-3
- Switch source URL to Debian servers

* Mon Jun 25 2012 Michel Salim <salimma@fedoraproject.org> - 0.3-2
- Remove deprecated %%{python_sitelib} declaration
- Delete build directory before doing coverage tests; the coverage
  exclusion list does not include the built version of the excluded
  modules

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.3-1
- Initial package
