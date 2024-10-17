%undefine _debugsource_packages
%define module pyzmq

Summary:	Python bindings for zeromq
Name:		python-%{module}
Version:	26.1.0
Release:	1
License:	LGPLv3+ and ASL 2.0 and BSD
Group:		Development/Python
Url:		https://zguide.zeromq.org/py:all
Source0:	https://github.com/zeromq/pyzmq/archive/v%{version}.tar.gz?/%{module}-%{version}.tar.gz
BuildRequires:	pkgconfig(libzmq)
BuildRequires:	pkgconfig(python)
BuildRequires:	python%{pyver}dist(nose)
BuildRequires:	python%{pyver}dist(cython)
BuildRequires:	python%{pyver}dist(scikit-build-core)

%description
This package contains Python bindings for zeromq, a lightweight and
fast messaging implementation.

#------------------------------------------------------------------

%files
%{py_platsitedir}/%{module}-*.*-info
%{py_platsitedir}/zmq

#------------------------------------------------------------------

%prep
%setup -q -c
%autopatch -p1

pushd %{module}-%{version}
# forcibly regenerate the Cython-generated .c files:
find zmq -name "*.c" -delete

# remove bundled libraries
rm -rf bundled
for lib in zmq/eventloop/*.py; do
	sed '/\/usr\/bin\/env/d' $lib > $lib.new &&
	touch -r $lib $lib.new &&
	mv $lib.new $lib
done

# remove excecutable bits
chmod -x examples/pubsub/topics_pub.py
chmod -x examples/pubsub/topics_sub.py
popd

%build
pushd %{module}-%{version}
%py_build
popd

%install
pushd %{module}-%{version}
%py_install
popd

%check
rm -f python3/zmq/__*
rm -rf %{buildroot}%{py_platsitedir}/zmq/tests
