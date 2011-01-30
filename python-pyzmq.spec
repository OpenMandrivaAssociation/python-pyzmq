%define module	pyzmq
%define name	python-%{module}
%define version 2.0.10.1
%define release %mkrel 1

Summary:	Python bindings for zeromq
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	%{module}-%{version}.tar.gz
License:	LGPLv3+
Group:		Development/Python
Url:		http://github.com/zeromq/pyzmq
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
Requires:	libzeromq 
BuildRequires:	zeromq-devel
BuildRequires:	python-nose
BuildRequires:	python-devel

%description
This package contains Python bindings for zeromq, a lightweight and
fast messaging implementation.

%prep
%setup -q -n %{module}-%{version}
%__python setup.py build

%install
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot} --record=FILE_LIST

%check
pushd %{buildroot}%{py_platsitedir}
nosetests
popd

%clean
%__rm -rf %{buildroot}

%files -f FILE_LIST
%defattr(-,root,root)
%doc COPYING* README.rst
