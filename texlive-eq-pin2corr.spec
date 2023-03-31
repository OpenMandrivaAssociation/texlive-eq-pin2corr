Name:		texlive-eq-pin2corr
Version:	59477
Release:	2
Summary:	Add PIN security to the "Correct" button of a quiz created by exerquiz
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/eq-pin2corr
License:	lppl1.2
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eq-pin2corr.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eq-pin2corr.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/eq-pin2corr.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package is an add-on to the quiz environment of the
exerquiz package (part of the acrotex bundle). It adds PIN
security to a quiz created by the quiz environment. To correct
a quiz, the document consumer must press the "Correct" button
of the quiz and successfully enter the correct PIN number. The
PIN security is designed for the instructor to mark and record
the student's effort on that quiz. The package works for the
usual workflows.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/eq-pin2corr
%{_texmfdistdir}/tex/latex/eq-pin2corr
%doc %{_texmfdistdir}/doc/latex/eq-pin2corr

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
