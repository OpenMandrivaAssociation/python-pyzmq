%define module	pyzmq
%define name	python-%{module}
%define version 2.2.0
%define	rel		2
%if %mdkversion < 201100
%define release %mkrel %rel
%else
%define	release	%rel
%endif

Summary:	Python bindings for zeromq
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Patch0:		doc-version-2.2.0.patch
Patch1:		fix-version-test-2.2.0.patch
License:	LGPLv3+
Group:		Development/Python
Url:		http://github.com/zeromq/pyzmq/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	libzeromq >= %{version}
BuildRequires:	zeromq-devel >= %{version}
BuildRequires:	python-cython
#BuildRequires:	python-nose
BuildRequires:	python-devel
BuildRequires:	python-sphinx, python-matplotlib

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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
PYTHONPATH=`dir -d ../build/lib*` make html
popd

# Temporarily disable tests:
#%check
#pushd %{buildroot}%{py_platsitedir}
#nosetests
#popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc COPYING* README.rst examples/ docs/build/html/
