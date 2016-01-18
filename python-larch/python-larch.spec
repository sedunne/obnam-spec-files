%global pkgname larch

Name:           python-%{pkgname}
Version:        1.20151025
Release:        1%{?dist}
Summary:        Python B-tree library

License:        GPLv3+
URL:            http://liw.fi/%{pkgname}/
Source0:        http://code.liw.fi/debian/pool/main/p/%{name}/%{name}_%{version}.orig.tar.xz

BuildArch:      noarch
# build-time only
BuildRequires:  cmdtest
BuildRequires:  python-coverage-test-runner
BuildRequires:  python-sphinx
# build- and run-time
BuildRequires:  python-cliapp
BuildRequires:  python-tracing
BuildRequires:  python-ttystatus
Requires:       python-cliapp
Requires:       python-tracing
Requires:       python-ttystatus

%description
This is an implementation of particular kind of B-tree, based on
research by Ohad Rodeh. See "B-trees, Shadowing, and Clones" (copied
here with permission of author) for details on the data
structure. This is the same data structure that btrfs uses. Note that
my implementation is independent from the btrfs one, and might differ
from what the paper describes.

The distinctive feature of this B-tree is that a node is never
modified (sort-of). Instead, all updates are done by
copy-on-write. Among other things, this makes it easy to clone a tree,
and modify only the clone, while other processes access the original
tree. This is utterly wonderful for my backup application, and that's
the reason I wrote larch in the first place.

I have tried to keep the implementation generic and flexible, so that
you may use it in a variety of situations. For example, the tree
itself does not decide where its nodes are stored: you provide a class
that does that for it. I have two implementations of the NodeStore
class, one for in-memory and one for on-disk storage.

The tree attempts to guarantee this: all modifications you make will
be safely stored in the node store when the larch.Forest.commit method
is called. After that, unless you actually modify the committed tree
yourself, it will be safe from further modifications. (You need to
take care to create a new tree for further modifications, though.)


%package        doc
Summary:        Documentation for %{pkgname}
Requires:       %{name} = %{version}-%{release}

%description    doc
This package contains the documentation for %{pkgname}, a Python
framework for Unix command line programs.


%prep
%setup -n %{name}-%{version}


%build
%{__python} setup.py build
# Build documentation
make


%install
%{__python} setup.py install -O1 --skip-build --root %{buildroot}
# manpage not installed automatically yet
mkdir -p %{buildroot}%{_mandir}/man1
cp -p fsck-larch.1 %{buildroot}%{_mandir}/man1/


%check
# CoverageTestRunner trips up on build directory;
# since we've already done the install phase, remove it first
rm -rf build
make check


%files
%doc COPYING NEWS README
%{_mandir}/man1/fsck-larch.1*
%{_bindir}/fsck-larch
%{python_sitelib}/*

%files doc
%doc doc/_build/html/*


%changelog
* Mon Jan 11 2016 Stephen Dunne <sdunne@nexcess.net> - 1.20151025-1
- Update to 1.20151025

* Thu Nov 27 2014 Michel Alexandre Salim <salimma@fedoraproject.org> - 1.20131130-1
- Update to 1.20131130

* Fri Sep 27 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130808-1
- Update to 1.20130808

* Sun Mar 17 2013 Michel Salim <salimma@fedoraproject.org> - 1.20130316-1
- Update to 1.20130316

* Mon Feb 25 2013 Michel Salim <salimma@fedoraproject.org> - 1.20121216-1
- Update to 1.20121216

* Mon Oct  8 2012 Michel Salim <salimma@fedoraproject.org> - 1.20121006-1
- Update to 1.20121006

* Sun Sep 16 2012 Michel Salim <salimma@fedoraproject.org> - 1.20120527-3
- Switch source URL to Debian servers

* Tue Jun 19 2012 Michel Salim <salimma@fedoraproject.org> - 1.20120527-2
- Remove redundant %%{python_sitelib} declaration
- Fix %%check when using latest version of CoverageTestRunner

* Sun Jun  3 2012 Michel Salim <salimma@fedoraproject.org> - 1.20120527-1
- Initial package
