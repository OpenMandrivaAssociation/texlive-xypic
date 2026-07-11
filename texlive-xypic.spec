%global tl_name xypic
%global tl_revision 79461

Name:		texlive-%{tl_name}
Epoch:		1
Version:	3.8.9
Release:	%{tl_revision}.1
Summary:	Flexible diagramming macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/diagrams/xypic
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xypic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/xypic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
A package for typesetting a variety of graphs and diagrams with TeX. Xy-
pic works with most formats (including LaTeX, AMS-LaTeX, AMS-TeX, and
plain TeX). The distribution includes Michael Barr's diag package, which
was previously distributed stand-alone.

