%define module Want

Name:		perl-%{module}
Version:	0.18
Release:	%mkrel 6
Summary:	A generalisation of wantarray
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	http://search.cpan.org/CPAN/authors/id/R/RO/ROBIN/%{module}-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
This module generalises the mechanism of the wantarray function, allowing a
function to determine in some detail how its return value is going to be
immediately used.

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README TODO
%{perl_vendorarch}/Want.pm
%{perl_vendorarch}/auto/Want
%{_mandir}/*/*


