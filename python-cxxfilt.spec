Name:		python-cxxfilt
Version:	0.3.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/c/cxxfilt/cxxfilt-%{version}.tar.gz
Summary:	Python interface to c++filt / abi::__cxa_demangle
URL:		https://pypi.org/project/cxxfilt/
License:	BSD
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildArch:	noarch

%description
Python interface to c++filt / abi::__cxa_demangle

%prep
%autosetup -p1 -n cxxfilt-%{version}

%build
%py_build

%install
%py_install

%files
%{py_sitedir}/cxxfilt
%{py_sitedir}/cxxfilt-*.*-info
