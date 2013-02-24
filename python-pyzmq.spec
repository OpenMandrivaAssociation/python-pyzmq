%define __noautoprov	'.*\.so\(\)'

%define module	pyzmq

Summary:	Python bindings for zeromq
Name:		python-%{module}
Version:	13.0.0
Release:	1
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Patch0:		doc-version-2.2.0.patch
Patch1:		fix-version-test-2.2.0.patch
License:	LGPLv3+
Group:		Development/Python
Url:		http://github.com/zeromq/pyzmq/
Requires:	libzeromq >= %{version}
BuildRequires:	zeromq-devel >= %{version}
BuildRequires:	python-cython
BuildRequires:	python-devel
BuildRequires:	python-nose
BuildRequires:	python-sphinx
BuildRequires:	python-matplotlib

# required for make check
BuildRequires:	python-tornado

BuildRequires:	pkgconfig(lapack)

%description
This package contains Python bindings for zeromq, a lightweight and
fast messaging implementation.

%prep
%setup -q -n %{module}-%{version}
%patch0 -p0
%patch1 -p0

%build
%__python setup.py build

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
PYTHONPATH=`dir -d ../build/lib*` make html
popd
rm docs//build/html/.buildinfo

# Temporarily disable tests:
%check
pushd %{buildroot}%{py_platsitedir}
nosetests
popd

%files -f FILE_LIST
%doc COPYING* README.rst examples/ docs/build/html/

%changelog
* Wed Feb 13 2013 pcpa <paulo.cesar.pereira.de.andrade@gmail.com> - 2.2.0-4
- Rebuild with updated dependencies.
- Do not provide internal shared objects.

* Sat Jul 07 2012 Lev Givon <lev@mandriva.org> 2.2.0-2
+ Revision: 808409
- Add patch for pyzmq issue #213 (broken version test).

* Tue May 08 2012 Lev Givon <lev@mandriva.org> 2.2.0-1
+ Revision: 797611
- Update to 2.2.0.

* Mon Dec 19 2011 Lev Givon <lev@mandriva.org> 2.1.11-1
+ Revision: 743817
- Update to 2.1.11.

* Tue Aug 30 2011 Lev Givon <lev@mandriva.org> 2.1.9-1
+ Revision: 697498
- Update to 2.1.9.

* Sun May 15 2011 Lev Givon <lev@mandriva.org> 2.1.7-1
+ Revision: 674734
- Update to 2.1.7.

* Thu Apr 21 2011 Lev Givon <lev@mandriva.org> 2.1.4-1
+ Revision: 656498
- Update to 2.1.4.

* Thu Mar 03 2011 Lev Givon <lev@mandriva.org> 2.1.1-1
+ Revision: 641531
- Update to 2.1.1.

* Mon Feb 07 2011 Lev Givon <lev@mandriva.org> 2.1.1-0.git1ad1d0baa0c0
+ Revision: 636740
- Update to 2.1.1 git revision 1ad1d0baa0c0.
- Update to 2.0.10.1.

* Sun Jan 30 2011 Lev Givon <lev@mandriva.org> 2.0.10_1-1
+ Revision: 634029
- Update to 2.0.10-1.

* Tue Nov 16 2010 Lev Givon <lev@mandriva.org> 2.0.10-2mdv2011.0
+ Revision: 598119
- Bump release to force rebuild.
- Update to 2.0.10.

* Tue Nov 02 2010 Lev Givon <lev@mandriva.org> 2.0.8-1mdv2011.0
+ Revision: 592558
- import python-pyzmq


