Name:           genbackupdata
Version:        1.7
Release:        1%{?dist}
Summary:        A program to generate test data for testing backup software

# upstream asked to include license text
License:        GPLv2+
URL:            http://liw.fi/%{name}/
Source0:        http://code.liw.fi/debian/pool/main/g/%{name}/%{name}_%{version}.orig.tar.gz

BuildArch:      noarch
# build-time
BuildRequires:  cmdtest
BuildRequires:  python-coverage-test-runner
# build- and run-time
BuildRequires:  python-cliapp
BuildRequires:  python-ttystatus
Requires:       python-cliapp
Requires:       python-ttystatus

%description
genbackupdata creates or modifies directory trees in ways that
simulate real filesystems sufficiently well for performance testing of
backup software. For example, it can create files that are a mix of
small text files and big binary files, with the binary files
containing random binary junk which compresses badly. This can then be
backed up, and later the directory tree can be changed by creating new
files, modifying files, or deleting or renaming files. The backup can
then be run again.

The output is deterministic, such that for a given set of parameters
the same output always happens. Thus it is more efficient to
distribute genbackupdata and a set of parameters between people who
wish to benchmark backup software than distributing very large test
sets.


%prep
%setup -q


%build
%{__python} setup.py build
# build manpage
make genbackupdata.1


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}


%check
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
make check


%files
%doc NEWS README
%{_mandir}/man1/genbackupdata.1*
%{_bindir}/genbackupdata
%{python_sitelib}/*


%changelog
* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 1.7-1
- Update to 1.7

* Sun Jul  8 2012 Michel Salim <salimma@fedoraproject.org> - 1.6-2
- Remove deprecated %%{python_sitelib} declaration
- Switch source URL to use the Debian-hosted file
- Delete build directory before doing coverage tests; the coverage
  exclusion list does not include the built version of the excluded
  modules

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 1.6-1
- Initial package
