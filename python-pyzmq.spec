%undefine _debugsource_packages
%define module pyzmq

Summary:	Python bindings for zeromq
Name:		python-%{module}
Version:	27.1.0
Release:	1
License:	LGPLv3+ and ASL 2.0 and BSD
Group:		Development/Python
Url:		https://zguide.zeromq.org/py:all
Source0:	https://github.com/zeromq/pyzmq/archive/v%{version}.tar.gz?/%{module}-%{version}.tar.gz
BuildRequires:	pkgconfig(libzmq)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(cffi)
BuildRequires:	python%{pyver}dist(nose)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(scikit-build-core)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:	python%{pyver}dist(wheel)

%description
This package contains Python bindings for zeromq, a lightweight and
fast messaging implementation.

%prep
%autosetup -n %{module}-%{version} -p1
# Fix non-executable script rpmlint warning:
# find examples zmq -name "*.py" -exec sed -i "s|#\!\/usr\/bin\/env python||" {} \;
# find . -name ".gitignore" -exec rm {} \;
# chmod -x examples/pubsub/topics_pub.py examples/pubsub/topics_sub.py

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
