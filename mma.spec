%define name	mma
%define version 12.02
%define release 2

Name: 	 	%{name}
Summary: 	Musical MIDI Accompaniment
Version: 	%{version}
Release: 	%{release}

Source0:	http://mypage.uniserve.ca/~bvdp/mma/%{name}-bin-%{version}.tar.gz
URL:		https://www.kootenay.com/~bvdpoel/music.html
License:	GPLv2+
Group:		Sound
Requires:	python
BuildArch:	noarch

%description
"Musical MIDI Accompaniment" is an accompaniment generator -- it creates midi
tracks for a soloist to perform over from a user supplied file containing
chords and MMA directives.

MMA is very versatile and generates excellent tracks. It comes with an
extensive user-extendable library with a variety of patterns for various
popular rhythms, an extensive user manual, and several demo songs.
MMA is a command line driven program. It creates MIDI files which need a
sequencer or MIDI file play program.

%prep
%setup -q -n %{name}-bin-%{version}

%install
install -d -m 755 %{buildroot}%{_bindir}
install -d -m 755 %{buildroot}%{_datadir}/%{name}
install -d -m 755 %{buildroot}%{py_sitedir}
install -d -m 755 %{buildroot}%{_docdir}
install -d -m 755 %{buildroot}%{_mandir}/man1
install -d -m 755 %{buildroot}%{_mandir}/man8
install -D mma.py %{buildroot}%{_bindir}/mma
cp -a lib %{buildroot}%{_datadir}/%{name}/lib
cp -a includes %{buildroot}%{_datadir}/%{name}/includes
cp -a MMA %{buildroot}%{py_sitedir}/MMA
cp -a docs/html %{buildroot}%{_docdir}/%{name}
for file in util/*.py
do
	prog=`echo "$file" | sed 's|^util/||' | sed 's|.py$||'`
	install -D -m 755 "$file" "%{buildroot}%{_bindir}/$prog"
done
install -m 644 docs/man/*.1 %{buildroot}%{_mandir}/man1/
install -m 644 docs/man/*.8 %{buildroot}%{_mandir}/man8/

%post
mma -G

%files
%doc text/* egs util/README.*
%{_bindir}/*
%{py_sitedir}/MMA
%{_datadir}/%{name}
%{_mandir}/man?/*


%changelog
* Sun Feb 26 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 12.02-1mdv2011.0
+ Revision: 780904
- new version 12.02

* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.20-5mdv2011.0
+ Revision: 620374
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.20-4mdv2010.0
+ Revision: 430079
- rebuild

* Tue Jul 29 2008 Thierry Vignaud <tv@mandriva.org> 0.20-3mdv2009.0
+ Revision: 252621
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Mon Dec 17 2007 Thierry Vignaud <tv@mandriva.org> 0.20-1mdv2008.1
+ Revision: 130075
- kill re-definition of %%buildroot on Pixel's request
- use %%mkrel
- import mma


* Thu Mar 09 2006 Austin Acton <austin@mandriva.org> 0.20-1mdk
- New release 0.20

* Thu Dec 29 2005 Austin Acton <austin@mandriva.org> 0.19-1mdk
- New release 0.19

* Fri Nov 04 2005 Austin Acton <austin@mandriva.org> 0.18-1mdk
- New release 0.18

* Thu Oct 06 2005 Austin Acton <austin@mandriva.org> 0.16-1mdk
- New release 0.16

* Thu Aug 25 2005 Austin Acton <austin@mandriva.org> 0.15-1mdk
- New release 0.15

* Tue Jun 21 2005 Austin Acton <austin@mandriva.org> 0.14-1mdk
- 0.14
- post script

* Tue Feb 17 2004 Austin Acton <austin@mandrake.org> 0.6-2mdk
- install all files!

* Mon Feb 16 2004 Austin Acton <austin@mandrake.org> 0.6-1mdk
- 0.6

* Tue Apr 29 2003 Austin Acton <aacton@yorku.ca> 0.1-1mdk
- initial package
