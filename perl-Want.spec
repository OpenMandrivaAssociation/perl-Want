%define real_name Want

Summary:	Want module for perl 
Name:		perl-%{real_name}
Version:	0.10
Release:	%mkrel 1
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{real_name}
Source0:	%{real_name}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
This module generalises the mechanism of the wantarray function, allowing a
function to determine in some detail how its return value is going to be
immediately used.

%prep
%setup -q -n %{real_name}-%{version} 

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
%{perl_vendorlib}/*/Want.pm
%{perl_vendorlib}/*/auto/Want
%{_mandir}/*/*


