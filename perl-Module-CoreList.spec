#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	CoreList
Summary:	Module::CoreList Perl module - what modules shipped with versions of Perl
Summary(pl):	Modu³ Perla Module::CoreList - jakie modu³y zawiera dana wersja Perla
Name:		perl-Module-CoreList
Version:	1.93
Release:	3
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	d643a6f0fa1b3935c32f638a60e21a19
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-Module-Build >= 0.20
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::CoreList Perl module gives you information about modules
included in a specified perl release. It currently only covers the
5.003_07, 5.004, 5.004_05, 5.005, 5.005_03, 5.6.0, 5.6.1, 5.6.2,
5.7.3, 5.8.0, 5.8.1, 5.8.2 and 5.9.0 releases of perl.

%description -l pl
Modu³ perla Module::CoreList podaje informacje o modu³ach Perla
wchodz±cych w sk³ad danej wersji perla. Obecnie zawiera on informacje
o wersjach perla: 5.003_07, 5.004, 5.004_05, 5.005, 5.005_03, 5.6.0,
5.6.1, 5.6.2, 5.7.3, 5.8.0, 5.8.1, 5.8.2 i 5.9.0.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Build.PL \
	installdirs=vendor \
	perl="%{__perl}" \
	destdir=$RPM_BUILD_ROOT
./Build

%{?with_tests:./Build test}

%install
rm -rf $RPM_BUILD_ROOT

./Build install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/corelist
%{perl_vendorlib}/Module/*.pm
%{_mandir}/man[13]/*
