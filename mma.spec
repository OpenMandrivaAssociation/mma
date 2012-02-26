%define name	mma
%define version 12.02
%define release %mkrel 1

Name: 	 	%{name}
Summary: 	Musical MIDI Accompaniment
Version: 	%{version}
Release: 	%{release}

Source0:	http://mypage.uniserve.ca/~bvdp/mma/%{name}-bin-%{version}.tar.gz
URL:		http://www.kootenay.com/~bvdpoel/music.html
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
