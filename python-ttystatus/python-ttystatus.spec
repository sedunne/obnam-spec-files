%global pkgname ttystatus

Name:           python-%{pkgname}
Version:        0.30
Release:        1%{?dist}
Summary:        Progress and status updates on terminals for Python

License:        GPLv3+
URL:            http://liw.fi/%{pkgname}/
Source0:        http://code.liw.fi/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.xz

BuildArch:      noarch
BuildRequires:  python-coverage-test-runner
BuildRequires:  python-sphinx
BuildRequires:  python-pep8

%description
ttystatus is a Python library for showing progress reporting and
status updates on terminals, for (Unix) command line programs. Output
is automatically adapted to the width of the terminal: truncated if it
does not fit, and re-sized if the terminal size changes.

Output is provided via widgets. Each widgets formats some data into a
suitable form for output. It gets the data either via its initializer,
or from key/value pairs maintained by the master object. The values
are set by the user. Every time a value is updated, widgets get
updated (although the terminal is only updated every so often to give
user time to actually read the output).


%package        doc
Summary:        Documentation for %{pkgname}
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the documentation for %{pkgname}, a Python
library providing progress and status updates on terminals.


%prep
%setup -n %{name}-%{version}


%build
%{__python} setup.py build
# Build documentation
make


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%check
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
make check


%files
%doc COPYING NEWS README
%{python_sitelib}/*

%files doc
%doc doc/_build/html/*


%changelog
* Fri Jan 8 2016 Stephen Dunne <sdunne@nexcess.net> - 0.30-1
- Update to 0.30

* Thu Jul 4 2013 Michel Salim <salimma@fedoraproject.org> - 0.23-1
- Update to 0.23

* Fri Mar 15 2013 Michel Salim <salimma@fedoraproject.org> - 0.22-1
- Update to 0.22

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 0.21-1
- Update to 0.21

* Thu Oct 18 2012 Michel Salim <salimma@fedoraproject.org> - 0.19-1
- Update to 0.19

* Thu Jun  7 2012 Michel Salim <salimma@fedoraproject.org> - 0.18-2
- Remove deprecated %%{python_sitelib} declaration
- Delete build directory before doing coverage tests; the coverage
  exclusion list does not include the built version of the excluded
  modules

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.18-1
- Initial package
