%define name	mma
%define version 0.20
%define release 1mdk

Name: 	 	%{name}
Summary: 	Musical MIDI Accompaniment
Version: 	%{version}
Release: 	%{release}

Source:		http://mypage.uniserve.ca/~bvdp/mma/%{name}-bin-%{version}.tar.bz2
URL:		http://www.kootenay.com/~bvdpoel/music.html
License:	GPL
Group:		Sound
BuildRoot:	%{_tmppath}/%{name}-buildroot
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
%setup -q -n %name-bin-%version

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p %buildroot/%_bindir
mkdir -p %buildroot/%_datadir/%name
cp %name %buildroot/%_bindir
cp -r lib %buildroot/%_datadir/%name
cp -r includes %buildroot/%_datadir/%name
cp -r modules %buildroot/%_datadir/%name

%post
mma -G

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc ANNOUNCE CHANGES CONTRIB FAKEBOOKS FAQ README SLASHCHORDS SYNTHS TODO egs
%{_bindir}/%name
%{_datadir}/%name

