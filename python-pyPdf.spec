%define		module	pyPdf

Summary:	A Pure-Python library built as a PDF toolkit
Summary(pl.UTF-8):	Biblioteka toolkitu PDF napisana w czystym Pythonie
Name:		python-%{module}
Version:	1.12
Release:	3
License:	BSD
Group:		Development/Languages/Python
Source0:	http://pybrary.net/pyPdf/pyPdf-%{version}.tar.gz
# Source0-md5:	7be5f7f4659f64fd194e9eb9a38ad425
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

%description -l pl.UTF-8
pyPdf to napisana w czystym Pythonie biblioteka stworzona jako toolkit
PDF. Potrafi:
- wyciągać informacje z dokumentów (tytuł, autora...),
- dzielić dokumenty na strony,
- łączyć dokumenty z pojedynczych stron,
- przycinać strony,
- łączyć wiele stron w jedną,
- szyfrować i odszyfrowywać pliki PDF.

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
