#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	CoreList
Summary:	Module::CoreList Perl module - what modules shipped with versions of perl
Summary(pl):	Modu³ Perla Module::CoreList - jakie modu³y zawiera dana wersja perla
Name:		perl-Module-CoreList
Version:	1.8
Release:	2
License:	GPL or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl-devel >= 5.6
%if %{?_without_tests:0}%{!?_without_tests:1}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::CoreList Perl module gives you information about modules
included in a specified perl release. It currently only covers the
5.003_07, 5.004, 5.004_05, 5.005, 5.005_03, 5.6.0, 5.6.1, 5.7.3 and
5.8.0 releases of perl.

%description -l pl
Modu³ perla Module::CoreList podaje informacje o modu³ach Perla
wchodz±cych w sk³ad danej wersji perla. Obecnie zawiera on informacje
o wersjach perla: 5.003_07, 5.004, 5.004_05, 5.005, 5.005_03, 5.6.0,
5.6.1, 5.7.3 i 5.8.0.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor 
%{__make}
%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%{perl_vendorlib}/Module/*.pm
%{_mandir}/man[13]/*
