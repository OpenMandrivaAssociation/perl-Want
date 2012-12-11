%define module Want

Name:		perl-%{module}
Version:	0.18
Release:	7
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




%changelog
* Wed Jan 25 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 0.18-7
+ Revision: 768358
- svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue Jul 20 2010 Jérôme Quelin <jquelin@mandriva.org> 0.18-6mdv2011.0
+ Revision: 555214
- rebuild

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.18-5mdv2010.0
+ Revision: 430654
- rebuild

* Thu Jul 31 2008 Thierry Vignaud <tv@mandriva.org> 0.18-4mdv2009.0
+ Revision: 258782
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.18-3mdv2009.0
+ Revision: 246696
- rebuild

* Fri Feb 29 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.1
+ Revision: 176707
- new version

* Mon Jan 14 2008 Pixel <pixel@mandriva.com> 0.14-2mdv2008.1
+ Revision: 151358
- rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun May 06 2007 Olivier Thauvin <nanardon@mandriva.org> 0.14-1mdv2008.0
+ Revision: 23601
- 0.14


* Wed Mar 29 2006 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 0.10-1mdk
- 0.10

* Thu Jul 14 2005 Andreas Hasenack <andreas@mandriva.com> 0.09-1mdk
- initial Mandriva package

