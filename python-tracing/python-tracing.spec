%global pkgname tracing

Name:           python-%{pkgname}
Version:        0.8
Release:        1%{?dist}
Summary:        Python debug logging helper

License:        GPLv3+
URL:            http://liw.fi/%{pkgname}/
Source0:        http://code.liw.fi/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.gz

BuildArch:      noarch
BuildRequires:  python-sphinx

%description
The Python library tracing helps with logging debug messages. It
provides a couple of functions for logging debug messages, and allows
the user to enable or disable logging for particular code modules.

It is sometimes practical to add a lot of debugging log messages to a
program, but having them enabled all the time results in very large
log files. Also, logging that much takes quite a bit of time.

This module provides a way to turn such debugging or tracing messages
on and off, based on the filename they occur in. The logging can that
be left in the code, and only enabled when it is needed.


%package        doc
Summary:        Documentation for %{pkgname}
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the documentation for %{pkgname}, a Python debug
logging helper.


%prep
%setup -q


%build
%{__python} setup.py build
# Build documentation
make -C doc html


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}

 
%files
%doc COPYING NEWS README
%{python_sitelib}/*

%files doc
%doc doc/_build/html/* example.py


%changelog
* Fri Sep 27 2013 Michel Salim <salimma@fedoraproject.org> - 0.8-1
- Update to 0.8

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 0.7-2
- Include license text

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 0.7-1
- Update to 0.7

* Tue Jun  5 2012 Michel Salim <salimma@fedoraproject.org> - 0.6-2
- Remove unneeded %%{python_sitelib} declaration
- Include example program in -doc

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.6-1
- Initial package
