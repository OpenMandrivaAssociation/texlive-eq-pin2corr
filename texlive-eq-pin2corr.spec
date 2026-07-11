%global tl_name eq-pin2corr
%global tl_revision 59477

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Add PIN security to the Correct button of a quiz created by exerquiz
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/eq-pin2corr
License:	lppl1.2
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eq-pin2corr.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eq-pin2corr.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/eq-pin2corr.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package is an add-on to the quiz environment of the exerquiz
package (part of the acrotex bundle). It adds PIN security to a quiz
created by the quiz environment. To correct a quiz, the document
consumer must press the "Correct" button of the quiz and successfully
enter the correct PIN number. The PIN security is designed for the
instructor to mark and record the student's effort on that quiz. The
package works for the usual workflows.

