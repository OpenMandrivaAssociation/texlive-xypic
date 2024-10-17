Name:		texlive-xypic
Epoch:		1
Version:	61719
Release:	2
Summary:	Flexible diagramming macros
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/generic/diagrams/xypic
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xypic.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/xypic.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
A package for typesetting a variety of graphs and diagrams with
TeX. Xy-pic works with most formats (including LaTeX, AMS-
LaTeX, AMS-TeX, and plain TeX). The distribution includes
Michael Barr's diag package, which was previously distributed
stand-alone.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/dvips/xypic/xy389dict.pro
%{_texmfdistdir}/fonts/afm/public/xypic/xyatip10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xybsql10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xybtip10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xycirc10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xycmat10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xycmat11.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xycmat12.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xycmbt10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xycmbt11.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xycmbt12.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xydash10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xyeuat10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xyeuat11.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xyeuat12.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xyeubt10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xyeubt11.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xyeubt12.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xyluat10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xyluat11.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xyluat12.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xylubt10.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xylubt11.afm
%{_texmfdistdir}/fonts/afm/public/xypic/xylubt12.afm
%{_texmfdistdir}/fonts/enc/dvips/xypic/xycirc.enc
%{_texmfdistdir}/fonts/enc/dvips/xypic/xyd.enc
%{_texmfdistdir}/fonts/enc/dvips/xypic/xyd2.enc
%{_texmfdistdir}/fonts/map/dvips/xypic/xypic.map
%{_texmfdistdir}/fonts/source/public/xypic/xyatip.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyatip10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyatri.mf
%{_texmfdistdir}/fonts/source/public/xypic/xybsql10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xybtip.mf
%{_texmfdistdir}/fonts/source/public/xypic/xybtip10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xybtri.mf
%{_texmfdistdir}/fonts/source/public/xypic/xycirc10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xycm.mf
%{_texmfdistdir}/fonts/source/public/xypic/xycmat10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xycmat11.mf
%{_texmfdistdir}/fonts/source/public/xypic/xycmat12.mf
%{_texmfdistdir}/fonts/source/public/xypic/xycmbt10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xycmbt11.mf
%{_texmfdistdir}/fonts/source/public/xypic/xycmbt12.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyd.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyd2.mf
%{_texmfdistdir}/fonts/source/public/xypic/xydash10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyeuat10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyeuat11.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyeuat12.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyeubt10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyeubt11.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyeubt12.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyeuler.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyline10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xylu.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyluat10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyluat11.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyluat12.mf
%{_texmfdistdir}/fonts/source/public/xypic/xylubt10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xylubt11.mf
%{_texmfdistdir}/fonts/source/public/xypic/xylubt12.mf
%{_texmfdistdir}/fonts/source/public/xypic/xymisc10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xyqc10.mf
%{_texmfdistdir}/fonts/source/public/xypic/xytech.mf
%{_texmfdistdir}/fonts/tfm/public/xypic/xyatip10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xybsql10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xybtip10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xycirc10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xycmat10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xycmat11.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xycmat12.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xycmbt10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xycmbt11.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xycmbt12.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xydash10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyeuat10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyeuat11.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyeuat12.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyeubt10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyeubt11.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyeubt12.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyline10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyluat10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyluat11.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyluat12.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xylubt10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xylubt11.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xylubt12.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xymisc10.tfm
%{_texmfdistdir}/fonts/tfm/public/xypic/xyqc10.tfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyatip10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyatip10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xybsql10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xybsql10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xybtip10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xybtip10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xycirc10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xycirc10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xycmat10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xycmat10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xycmat11.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xycmat11.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xycmat12.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xycmat12.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xycmbt10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xycmbt10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xycmbt11.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xycmbt11.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xycmbt12.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xycmbt12.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xydash10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xydash10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyeuat10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyeuat10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyeuat11.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyeuat11.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyeuat12.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyeuat12.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyeubt10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyeubt10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyeubt11.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyeubt11.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyeubt12.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyeubt12.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyluat10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyluat10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyluat11.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyluat11.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xyluat12.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xyluat12.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xylubt10.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xylubt10.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xylubt11.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xylubt11.pfm
%{_texmfdistdir}/fonts/type1/public/xypic/xylubt12.pfb
%{_texmfdistdir}/fonts/type1/public/xypic/xylubt12.pfm
%{_texmfdistdir}/tex/generic/xypic/movie.cls
%{_texmfdistdir}/tex/generic/xypic/xy.sty
%{_texmfdistdir}/tex/generic/xypic/xy.tex
%{_texmfdistdir}/tex/generic/xypic/xy16textures.tex
%{_texmfdistdir}/tex/generic/xypic/xy17oztex.tex
%{_texmfdistdir}/tex/generic/xypic/xy2cell.tex
%{_texmfdistdir}/tex/generic/xypic/xyall.tex
%{_texmfdistdir}/tex/generic/xypic/xyarc.tex
%{_texmfdistdir}/tex/generic/xypic/xyarrow.tex
%{_texmfdistdir}/tex/generic/xypic/xybarr.tex
%{_texmfdistdir}/tex/generic/xypic/xycmactex.tex
%{_texmfdistdir}/tex/generic/xypic/xycmtip.tex
%{_texmfdistdir}/tex/generic/xypic/xycolor.tex
%{_texmfdistdir}/tex/generic/xypic/xycrayon.tex
%{_texmfdistdir}/tex/generic/xypic/xycurve.tex
%{_texmfdistdir}/tex/generic/xypic/xydummy.tex
%{_texmfdistdir}/tex/generic/xypic/xydvidrv.tex
%{_texmfdistdir}/tex/generic/xypic/xydvips.tex
%{_texmfdistdir}/tex/generic/xypic/xydvitops.tex
%{_texmfdistdir}/tex/generic/xypic/xyemtex.tex
%{_texmfdistdir}/tex/generic/xypic/xyframe.tex
%{_texmfdistdir}/tex/generic/xypic/xygraph.tex
%{_texmfdistdir}/tex/generic/xypic/xyidioms.tex
%{_texmfdistdir}/tex/generic/xypic/xyimport.tex
%{_texmfdistdir}/tex/generic/xypic/xyknot.tex
%{_texmfdistdir}/tex/generic/xypic/xyline.tex
%{_texmfdistdir}/tex/generic/xypic/xymacpat.xyp
%{_texmfdistdir}/tex/generic/xypic/xymatrix.tex
%{_texmfdistdir}/tex/generic/xypic/xymovie.tex
%{_texmfdistdir}/tex/generic/xypic/xynecula.tex
%{_texmfdistdir}/tex/generic/xypic/xyoztex.tex
%{_texmfdistdir}/tex/generic/xypic/xypdf-co.tex
%{_texmfdistdir}/tex/generic/xypic/xypdf-cu.tex
%{_texmfdistdir}/tex/generic/xypic/xypdf-fr.tex
%{_texmfdistdir}/tex/generic/xypic/xypdf-li.tex
%{_texmfdistdir}/tex/generic/xypic/xypdf-ro.tex
%{_texmfdistdir}/tex/generic/xypic/xypdf.tex
%{_texmfdistdir}/tex/generic/xypic/xypic.sty
%{_texmfdistdir}/tex/generic/xypic/xypic.tex
%{_texmfdistdir}/tex/generic/xypic/xypicture.tex
%{_texmfdistdir}/tex/generic/xypic/xypoly.tex
%{_texmfdistdir}/tex/generic/xypic/xyps-c.tex
%{_texmfdistdir}/tex/generic/xypic/xyps-col.tex
%{_texmfdistdir}/tex/generic/xypic/xyps-f.tex
%{_texmfdistdir}/tex/generic/xypic/xyps-l.tex
%{_texmfdistdir}/tex/generic/xypic/xyps-pro.tex
%{_texmfdistdir}/tex/generic/xypic/xyps-ps.tex
%{_texmfdistdir}/tex/generic/xypic/xyps-r.tex
%{_texmfdistdir}/tex/generic/xypic/xyps-s.tex
%{_texmfdistdir}/tex/generic/xypic/xyps-t.tex
%{_texmfdistdir}/tex/generic/xypic/xyps.tex
%{_texmfdistdir}/tex/generic/xypic/xypsdict.tex
%{_texmfdistdir}/tex/generic/xypic/xypspatt.tex
%{_texmfdistdir}/tex/generic/xypic/xyrecat.tex
%{_texmfdistdir}/tex/generic/xypic/xyrotate.tex
%{_texmfdistdir}/tex/generic/xypic/xysmart.tex
%{_texmfdistdir}/tex/generic/xypic/xytextures.tex
%{_texmfdistdir}/tex/generic/xypic/xytile.tex
%{_texmfdistdir}/tex/generic/xypic/xytips.tex
%{_texmfdistdir}/tex/generic/xypic/xytp-f.tex
%{_texmfdistdir}/tex/generic/xypic/xytpic.tex
%{_texmfdistdir}/tex/generic/xypic/xyv2.tex
%{_texmfdistdir}/tex/generic/xypic/xyweb.tex
%{_texmfdistdir}/tex/generic/xypic/xyxdvi.tex
%doc %{_texmfdistdir}/doc/generic/xypic/CATALOG
%doc %{_texmfdistdir}/doc/generic/xypic/COPYING
%doc %{_texmfdistdir}/doc/generic/xypic/FONTCOPYING
%doc %{_texmfdistdir}/doc/generic/xypic/INSTALL
%doc %{_texmfdistdir}/doc/generic/xypic/MANIFEST
%doc %{_texmfdistdir}/doc/generic/xypic/README
%doc %{_texmfdistdir}/doc/generic/xypic/TRAILER
%doc %{_texmfdistdir}/doc/generic/xypic/VERSIONS
%doc %{_texmfdistdir}/doc/generic/xypic/Xy-logo.png
%doc %{_texmfdistdir}/doc/generic/xypic/Xy-pic.html
%doc %{_texmfdistdir}/doc/generic/xypic/barrdoc.pdf
%doc %{_texmfdistdir}/doc/generic/xypic/support/dvitogif89a
%doc %{_texmfdistdir}/doc/generic/xypic/support/install-tds
%doc %{_texmfdistdir}/doc/generic/xypic/support/pnmrawtopcropwhite.c
%doc %{_texmfdistdir}/doc/generic/xypic/xy389src.tar.gz
%doc %{_texmfdistdir}/doc/generic/xypic/xyguide.pdf
%doc %{_texmfdistdir}/doc/generic/xypic/xypdf.pdf
%doc %{_texmfdistdir}/doc/generic/xypic/xyrefer.pdf
%doc %{_texmfdistdir}/doc/generic/xypic/xysource.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar dvips fonts tex doc %{buildroot}%{_texmfdistdir}
