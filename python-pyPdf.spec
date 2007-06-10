%define		module	pyPdf

Summary:	A Pure-Python library built as a PDF toolkit
Name:		python-%{module}
Version:	1.9
Release:	1
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pybrary.net/pyPdf/pyPdf-%{version}.tar.gz
# Source0-md5:	2caddd42b685246621ecd19ce62f99ac
URL:		http://pybrary.net/pyPdf/
BuildRequires:	python-devel
BuildRequires:	rpm-pythonprov
%pyrequires_eq	python
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Pure-Python library built as a PDF toolkit. It is capable of:
* extracting document information (title, author, ...),
* splitting documents page by page,
* merging documents page by page,
* cropping pages,
* merging multiple pages into a single page,
* encrypting and decrypting PDF files.

%prep
%setup -q -n %{module}-%{version}

%build
python ./setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python ./setup.py install \
	--optimize 2 \
	--root=$RPM_BUILD_ROOT

%py_ocomp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_comp $RPM_BUILD_ROOT%{py_sitescriptdir}
%py_postclean

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG
%dir %{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{module}/*.py[co]
%{py_sitescriptdir}/*.egg-info