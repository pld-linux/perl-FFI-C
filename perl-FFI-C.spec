#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

%define		pdir	FFI
%define		pnam	C
Summary:	FFI::C - C data types for FFI
Name:		perl-FFI-C
Version:	0.15
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	2861103eb2a0db16b1c996983c7acacc
URL:		http://search.cpan.org/dist/FFI-C/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl(Test2)
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This distribution provides tools for building classes to interface
for common C data types. Arrays, struct, union and nested types based
on those are supported.

Core FFI::Platypus also provides FFI::Platypus::Record for
manipulating and passing structured data. Typically you want to use
FFI::C instead, the main exception is when you need to pass structured
data by value instead of by reference.

To work with C APIs that work with C file pointers you can use
FFI::C::File and FFI::C::PosixFile. For C APIs that expose the POSIX
stat structure use FFI::C::Stat.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}
%{__cp} -a examples/* $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/%{pdir}/*.pm
%{perl_vendorlib}/%{pdir}/%{pnam}
%{_mandir}/man3/*
%{_examplesdir}/%{name}-%{version}
