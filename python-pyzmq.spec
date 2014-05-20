%define module	pyzmq

Summary:	Python bindings for zeromq

Name:		python-%{module}
Version:	13.1.0
Release:	1
Source0:	http://pypi.python.org/packages/source/p/%{module}/%{module}-%{version}.tar.gz
Source100:	%{name}.rpmlintrc
License:	LGPLv3+ and ASL 2.0 and BSD
Group:		Development/Python
Url:		http://github.com/zeromq/pyzmq
BuildRequires:	pkgconfig(libzmq)
BuildRequires:	python-nose
BuildRequires:	python-setuptools
BuildRequires:	pkgconfig(python)
BuildRequires:	pkgconfig(python3)
BuildRequires:	python3-distribute
BuildRequires:	python3-nose
BuildRequires:  pythonegg(cython)
BuildRequires:  python3egg(cython)

%description
This package contains Python bindings for zeromq, a lightweight and
fast messaging implementation.

%package -n python3-%{module}
Summary:        Software library for fast, message-based applications

Group:          Development/Python

%description -n python3-%{module}
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the python 3 bindings.

%prep
%setup -q -c

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

mv %{module}-%{version} python2
cp -r python2 python3

pushd python2
python setup.py cython
popd

pushd python3
find . -name '*.py' | xargs sed -i '1s|^#!python|#!%{__python3}|'
popd

%build
pushd python2
CFLAGS="%{optflags}" python setup.py build
popd

pushd python3
CFLAGS="%{optflags}" python3 setup.py build
popd

%install
pushd python3
python3 setup.py install --skip-build --root %{buildroot}
popd

pushd python2
python setup.py install --skip-build --root %{buildroot}
popd

%check
rm python2/zmq/__*
rm python3/zmq/__*

pushd python2
PYTHONPATH=%{buildroot}%{py_platsitedir} \
 python setup.py test
popd

pushd python3
PYTHONPATH=%{buildroot}%{py3_platsitedir} \
 %{__python3} setup.py test
popd

rm -rf %{buildroot}%{py_platsitedir}/zmq/tests
rm -rf %{buildroot}%{py3_platsitedir}/zmq/tests

%files
%doc python2/README.md python2/COPYING.* python2/examples/
%{py_platsitedir}/%{module}-*.egg-info
%{py_platsitedir}/zmq

%files -n python3-%{module}
%doc python3/README.md python3/COPYING.* python3/examples/
%{py3_platsitedir}/%{module}-*.egg-info
%{py3_platsitedir}/zmq


