%undefine _debugsource_packages
%define module pyzmq

Summary:	Python bindings for zeromq
Name:		python-%{module}
Version:	27.1.0
Release:	1
License:	LGPLv3+ and ASL 2.0 and BSD
Group:		Development/Python
URL:		https://github.com/zeromq/pyzmq
Source0:	https://github.com/zeromq/pyzmq/archive/v%{version}/%{name}-%{version}.tar.gz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	pkgconfig(libzmq)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(scikit-build-core)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package contains Python bindings for zeromq, a lightweight and
fast messaging implementation.

%package devel
Summary:        Development files for %{name}
Requires:       %{name} = %{version}
Requires:       python-devel
Requires:       zeromq-devel

%description devel
Development libraries and headers needed to build software using %{name}.

%prep
%autosetup -n %{module}-%{version} -p1
# increase/loosen cmake upper version requirements
sed -i 's/cmake_minimum_required(VERSION 3.14...4.1)/cmake_minimum_required(VERSION 3.14...4.5)/g' CMakeLists.txt

%build
export CFLAGS="%{optflags}"
export LDFLAGS="%{ldflags} -lpython%{py_ver}"
%py_build

%install
%py_install

%files
%doc README.md examples/
%license LICENSE.md
%{py_platsitedir}/%{module}-*.*-info
%{py_platsitedir}/zmq
%exclude %{python_sitearch}/zmq/backend/cffi/*.c
%exclude %{python_sitearch}/zmq/utils/*.h
%exclude %{python_sitearch}/zmq/backend/cffi/_cdefs.h

%files devel
%{python_sitearch}/zmq/utils/*.h
%{python_sitearch}/zmq/backend/cffi/*.c
%{python_sitearch}/zmq/backend/cffi/_cdefs.h
