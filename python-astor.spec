#
# Conditional build:
%bcond_with	tests	# unit tests (using local python installation, failing on python 3.9)
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

Summary:	Read/rewrite/write Python ASTs
Summary(pl.UTF-8):	Odczyt/przepisywanie/zapis pythonowych AST
Name:		python-astor
Version:	0.8.1
Release:	1
License:	BSD
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/astor/
Source0:	https://files.pythonhosted.org/packages/source/a/astor/astor-%{version}.tar.gz
# Source0-md5:	83ab4ee6598f0381d94ed6949a6d6da2
URL:		https://pypi.org/project/astor/
%if %{with python2}
BuildRequires:	python-modules >= 1:2.7
BuildRequires:	python-setuptools
%if %{with tests}
BuildRequires:	python-astunparse
BuildRequires:	python-nose
%endif
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.4
BuildRequires:	python3-setuptools
%if %{with tests}
BuildRequires:	python3-astunparse
BuildRequires:	python3-nose
%endif
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.7
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
astor is designed to allow easy manipulation of Python source via the
AST.

%description -l pl.UTF-8
astor powstał, aby umożliwić łatwe operowanie na kodzie źródłowym w
Pythonie poprzez AST.

%package -n python3-astor
Summary:	Read/rewrite/write Python ASTs
Summary(pl.UTF-8):	Odczyt/przepisywanie/zapis pythonowych AST
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.4

%description -n python3-astor
astor is designed to allow easy manipulation of Python source via the
AST.

%description -n python3-astor -l pl.UTF-8
astor powstał, aby umożliwić łatwe operowanie na kodzie źródłowym w
Pythonie poprzez AST.

%prep
%setup -q -n astor-%{version}

%build
%if %{with python2}
%py_build

%if %{with tests}
nosetests-%{py_ver} tests
%endif
%endif

%if %{with python3}
%py3_build

%if %{with tests}
nosetests-%{py3_ver} tests
%endif
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%{py_sitescriptdir}/astor
%{py_sitescriptdir}/astor-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-astor
%defattr(644,root,root,755)
%doc AUTHORS LICENSE README.rst
%{py3_sitescriptdir}/astor
%{py3_sitescriptdir}/astor-%{version}-py*.egg-info
%endif
