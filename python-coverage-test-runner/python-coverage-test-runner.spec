%global pkgname CoverageTestRunner
%global prjname coverage-test-runner

Name:           python-%{prjname}
Version:        1.10
Release:        1%{?dist}.1
Summary:        Python module for enforcing code coverage completeness

License:        GPLv3+
URL:            http://liw.fi/%{prjname}/
Source0:        http://code.liw.fi/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.gz

BuildArch:      noarch
BuildRequires:  python-coverage
Requires:       python-coverage

%description
CoverageTestRunner is a Python module for running unit tests and
failing them if the unit test module does not exercise all statements
in the module it tests.

For example, unit tests in module foo_tests.py are supposed to test
everything in the foo.py module, and if they don't, it's a bug in the
test coverage. It does not matter if other tests happen to test the
missing parts. The unit tests for the module should test everything in
that module.


%prep
%setup -q -n %{pkgname}-%{version}


%build
%{__python} setup.py build


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%check
make check


%files
%doc COPYING NEWS README
%{python_sitelib}/%{pkgname}.py*
%{python_sitelib}/%{pkgname}-%{version}-py?.?.egg-info


%changelog
* Fri Sep 27 2013 Michel Salim <salimma@fedoraproject.org> - 1.10-1.1
- Rebuild to push as Bodhi update

* Sat Apr 20 2013 Michel Salim <salimma@fedoraproject.org> - 1.10-1
- Update to 1.10

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 1.9-1
- Update to 1.9

* Mon Jun  4 2012 Michel Salim <salimma@fedoraproject.org> - 1.8-1
- Update to 1.8
- Drop unneeded conditional declaration of %%{python_sitelib}

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 1.0-1
- Initial package
