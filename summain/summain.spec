Name:           summain
Version:        0.18
Release:        1%{?dist}
Summary:        File manifest generator

License:        GPLv3+
URL:            http://liw.fi/%{name}/
Source0:        http://code.liw.fi/debian/pool/main/s/%{name}/%{name}_%{version}.orig.tar.gz

# build-time
BuildRequires:  python-coverage-test-runner
BuildRequires:  libattr-devel
BuildRequires:  python-devel
# build- and run-time
BuildRequires:  python-cliapp
Requires:       python-cliapp

# we don't want to provide private python extension libs
# http://fedoraproject.org/wiki/Packaging:AutoProvidesAndRequiresFiltering#Arch-specific_extensions_to_scripting_languages
%{?filter_setup:
%filter_provides_in %{python_sitearch}/_summain.so 
%filter_setup
}

%description
Summain generates file manifests, which contain metadata about the
files, and a checksum of their content for regular files. The manifest
can be generated for a directory tree at different points in time and
compared (with diff) to see if something has changed.


%prep
%setup -q


%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build
# Generate manpages
make summain.1


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# fix permission
chmod 755 %{buildroot}%{python_sitearch}/_summain.so


%check
%if 0%{?fedora}
# check not part of EL6's python
# TODO: replace this with proper test suite once available
%{__python} setup.py check
%endif


%files
%doc COPYING NEWS README
%{_mandir}/man1/summain.1*
%{_bindir}/summain
%{python_sitearch}/*


%changelog
* Sun Mar 17 2013 Michel Salim <salimma@fedoraproject.org> - 0.18-1
- Update to 0.18

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 0.17-1
- Update to 0.17

* Fri Oct 19 2012 Michel Salim <salimma@fedoraproject.org> - 0.14-2
- When building for EL6, skip unavailable package checks

* Wed Jul  4 2012 Michel Salim <salimma@fedoraproject.org> - 0.14-1
- Update to 0.14

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 0.13-1
- Initial package
