%global pkgname cliapp

Name:           python-%{pkgname}
Version:        1.20160109
Release:        1%{?dist}
Summary:        Python framework for Unix command line programs

License:        GPLv2+
URL:            http://liw.fi/%{pkgname}/
Source0:        http://code.liw.fi/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.xz

BuildArch:      noarch
BuildRequires:  python-coverage-test-runner
BuildRequires:  python-sphinx
BuildRequires:  PyYAML
BuildRequires:  python-pep8

%description
cliapp is a Python framework for Unix-like command line programs. It
contains the typical stuff such programs need to do, such as parsing
the command line for options, and iterating over input files.


%package        doc
Summary:        Documentation for %{pkgname}
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the documentation for %{pkgname}, a Python
framework for Unix command line programs.


%prep
%setup -q -n %{name}-%{version}


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
# ./cliapp/runcmd.py also missing tests
# (fixed in current Git but introduces other changes)
echo ./cliapp/runcmd.py >> without-tests
make check


%files
%doc COPYING NEWS README
%{_mandir}/man5/cliapp.5*
%{python_sitelib}/%{pkgname}
%{python_sitelib}/%{pkgname}-%{version}-py?.?.egg-info

%files doc
%doc doc/_build/html/*


%changelog
* Mon Jan 11 2016 Stephen Dunne <sdunne@nexcess.net> - 1.20160109
- Update to 1.20160109

* Tue Dec  2 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.20140719-1
- Update to 1.20140719

* Fri Sep 27 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130808-1
- Update to 1.20130808

* Fri Jun 14 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130613-1
- Update to 1.20130613

* Tue Apr 30 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130424-1
- Update to 1.20130424

* Fri Mar 15 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130313-1
- Update to 1.20130313

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 1.20121216-1
- Update to 1.20121216

* Tue Jul  3 2012 Michel Salim <salimma@fedoraproject.org> - 1.20120630-1
- Update to 1.20120630

* Tue Jun  5 2012 Michel Salim <salimma@fedoraproject.org> - 0.29-2
- Remove unneeded %%{python_sitelib} declaration
- Make file listing more specific
- Remove build directory before running coverage test

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.29-1
- Initial package
