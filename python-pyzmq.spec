%define module	pyzmq
%define name	python-%{module}
%define version 2.1.1
%define release %mkrel 0.git1ad1d0baa0c0

Summary:	Python bindings for zeromq
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	LGPLv3+
Group:		Development/Python
Url:		http://github.com/zeromq/pyzmq
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	libzeromq >= 2.1.0
BuildRequires:	zeromq-devel >= 2.1.0
BuildRequires:	python-cython
BuildRequires:	python-nose
BuildRequires:	python-devel
BuildRequires:	python-sphinx, python-matplotlib

%description
This package contains Python bindings for zeromq, a lightweight and
fast messaging implementation.

%prep
%setup -q -n %{module}-%{version}
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST
pushd docs
PYTHONPATH=`dir -d ../build/lib*` make html
popd

%check
pushd %{buildroot}%{py_platsitedir}
nosetests
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc COPYING* README.rst examples/ docs/build/html/
