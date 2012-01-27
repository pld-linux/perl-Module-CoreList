#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Module
%define		pnam	CoreList
Summary:	Module::CoreList Perl module - what modules shipped with versions of Perl
Summary(pl.UTF-8):	Moduł Perla Module::CoreList - jakie moduły zawiera dana wersja Perla
Name:		perl-Module-CoreList
# NOTE: update version list in %description when upgrading
Version:	2.60
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/BINGOS/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	0bb3fcb0ff4500c9932032f68af5c6f8
URL:		http://search.cpan.org/dist/Module-CoreList/
%if %{with tests}
BuildRequires:	perl-Test-Simple
%endif
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::CoreList Perl module gives you information about modules
included in a specified perl release. It currently only covers the
5.000, 5.001, 5.002, 5.003_07, 5.004, 5.004_05, 5.005, 5.005_03,
5.005_04, 5.6.0, 5.6.1, 5.6.2, 5.7.3, 5.8.0, 5.8.1, 5.8.2, 5.8.3,
5.8.4, 5.8.5, 5.8.6, 5.8.7, 5.8.8, 5.8.9, 5.9.0, 5.9.1, 5.9.2, 5.9.3,
5.9.4, 5.9.5, 5.10.0, 5.11.0, 5.11.1, 5.11.2, 5.11.3, 5.11.4, 5.11.5,
5.12.0, 5.12.1, 5.12.2, 5.12.3, 5.13.0, 5.13.1, 5.13.2, 5.13.3,
5.13.4, 5.13.5, 5.13.6, 5.13.7, 5.13.8. 5.13.9 and 5.13.10 releases of
perl.

%description -l pl.UTF-8
Moduł Perla Module::CoreList podaje informacje o modułach Perla
wchodzących w skład danej wersji Perla. Obecnie zawiera on informacje
o wersjach Perla: 5.000, 5.001, 5.002, 5.003_07, 5.004, 5.004_05, 
5.005, 5.005_03, 5.005_04, 5.6.0, 5.6.1, 5.6.2, 5.7.3, 5.8.0, 5.8.1, 
5.8.2, 5.8.3, 5.8.4, 5.8.5, 5.8.6, 5.8.7, 5.8.8, 5.8.9, 5.9.0, 5.9.1,
5.9.2, 5.9.3, 5.9.4, 5.9.5, 5.10.0, 5.11.0, 5.11.1, 5.11.2, 5.11.3,
5.11.4, 5.11.5, 5.12.0, 5.12.1, 5.12.2, 5.12.3, 5.13.0, 5.13.1,
5.13.2, 5.13.3, 5.13.4, 5.13.5, 5.13.6, 5.13.7, 5.13.8. 5.13.9 oraz
5.13.10.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}
%{?with_tests: %{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes
%attr(755,root,root) %{_bindir}/corelist
%{perl_vendorlib}/Module/CoreList.pm
%{_mandir}/man1/corelist.1*
%{_mandir}/man3/Module::CoreList.3*
