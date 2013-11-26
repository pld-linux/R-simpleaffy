%define		packname	simpleaffy

Summary:	Very simple high level analysis of Affymetrix data
Name:		R-%{packname}
Version:	2.38.0
Release:	1
License:	GPL v2+
Group:		Applications/Engineering
Source0:	http://www.bioconductor.org/packages/release/bioc/src/contrib/%{packname}_%{version}.tar.gz
# Source0-md5:	68fbe75b4e04265c0fe43610afdeff04
URL:		http://www.bioconductor.org/packages/release/bioc/html/simpleaffy.html
BuildRequires:	R-Biobase
BuildRequires:	R
BuildRequires:	R-BiocGenerics
BuildRequires:	R-affy
BuildRequires:	R-genefilter
BuildRequires:	R-gcrma
BuildRequires:	texlive-latex
Requires:	R-Biobase
Requires:	R
Requires:	R-BiocGenerics
Requires:	R-affy
Requires:	R-genefilter
Requires:	R-gcrma
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Provides high level functions for reading Affy .CEL files, phenotypic
data, and then computing simple things with it, such as t-tests, fold
changes and the like. Makes heavy use of the affy library. Also has
some basic scatter plot functions and mechanisms for generating high
resolution journal figures.

%prep
%setup -q -c -n %{packname}

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_libdir}/R/library

%{_bindir}/R CMD INSTALL -l $RPM_BUILD_ROOT%{_libdir}/R/library %{packname}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_libdir}/R/library/%{packname}/DESCRIPTION
%doc %{_libdir}/R/library/%{packname}/doc
%doc %{_libdir}/R/library/%{packname}/html
%dir %{_libdir}/R/library/%{packname}
%{_libdir}/R/library/%{packname}/Meta
%{_libdir}/R/library/%{packname}/NAMESPACE
%{_libdir}/R/library/%{packname}/INDEX
%{_libdir}/R/library/%{packname}/R
%{_libdir}/R/library/%{packname}/help
%{_libdir}/R/library/%{packname}/data
%{_libdir}/R/library/%{packname}/extdata
%dir %{_libdir}/R/library/%{packname}/libs
%attr(755,root,root) %{_libdir}/R/library/%{packname}/libs/%{packname}.so
