%define upstream_name    Want
%define upstream_version 0.29

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    1

Summary:    A generalisation of wantarray

License:    GPL+ or Artistic
Group:      Development/Perl
Url:        https://metacpan.org/dist/Want
Source0:    https://cpan.metacpan.org/authors/id/R/RO/ROBIN/Want-%{upstream_version}.tar.gz

BuildRequires:	make
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl-devel
BuildRequires: perl-JSON-PP

%description
This module generalises the mechanism of the wantarray function, allowing a
function to determine in some detail how its return value is going to be
immediately used.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor DESTDIR=%{buildroot}
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.json META.yml MYMETA.yml README TODO
%{perl_vendorarch}/Want.pm
%{perl_vendorarch}/auto/Want
%{_mandir}/*/*


