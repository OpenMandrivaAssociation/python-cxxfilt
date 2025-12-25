Name:		python-cxxfilt
Version:	0.3.0
Release:	3
Source0:	https://files.pythonhosted.org/packages/source/c/cxxfilt/cxxfilt-%{version}.tar.gz
Summary:	Python interface to c++filt / abi::__cxa_demangle
URL:		https://pypi.org/project/cxxfilt/
License:	BSD
Group:		Development/Python
BuildSystem:	python
BuildRequires:	python%{pyver}dist(setuptools)
BuildArch:	noarch

%description
Python interface to c++filt / abi::__cxa_demangle

%files
%{py_sitedir}/cxxfilt
%{py_sitedir}/cxxfilt-*.*-info
