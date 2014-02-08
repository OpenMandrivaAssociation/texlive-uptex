# revision 26775
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-uptex
Version:	20120810
Release:	2
Summary:	TeXLive uptex package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-ptex
Requires:	texlive-hyph-utf8
Requires:	texlive-adobemapping
Requires:	texlive-ipaex
Requires:	texlive-japanese
Requires:	texlive-japanese-otf
Requires:	texlive-uptex.bin

%description
TeXLive uptex package.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_bindir}/convbkmk
%{_texmfdistdir}/fonts/cmap/uptex/UTF8-UTF16
%{_texmfdistdir}/fonts/map/dvipdfmx/uptex/uptex-noEmbed.map
%{_texmfdistdir}/fonts/tfm/uptex/jis/upgbm-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upgbm-hq.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upgbm-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uphygt-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uphygt-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uphysmjm-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uphysmjm-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjisg-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjisg-hq.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjisg-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjisr-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjisr-hq.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjisr-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjpngt-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjpngt-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjpnrm-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upjpnrm-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upkorgt-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upkorgt-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upkorrm-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upkorrm-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upmhm-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upmhm-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upmsl-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upmsl-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uprml-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uprml-hq.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uprml-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upschgt-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upschgt-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upschrm-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upschrm-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upstht-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upstht-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upstsl-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/upstsl-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uptchgt-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uptchgt-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uptchrm-h.tfm
%{_texmfdistdir}/fonts/tfm/uptex/jis/uptchrm-v.tfm
%{_texmfdistdir}/fonts/tfm/uptex/min/ugbm.tfm
%{_texmfdistdir}/fonts/tfm/uptex/min/ugbmv.tfm
%{_texmfdistdir}/fonts/tfm/uptex/min/ugoth10.tfm
%{_texmfdistdir}/fonts/tfm/uptex/min/umin10.tfm
%{_texmfdistdir}/fonts/tfm/uptex/min/urml.tfm
%{_texmfdistdir}/fonts/tfm/uptex/min/urmlv.tfm
%{_texmfdistdir}/fonts/tfm/uptex/min/utgoth10.tfm
%{_texmfdistdir}/fonts/tfm/uptex/min/utmin10.tfm
%{_texmfdistdir}/fonts/vf/uptex/jis/upjisg-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upjisg-hq.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upjisg-v.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upjisr-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upjisr-hq.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upjisr-v.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upjpngt-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upjpngt-v.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upjpnrm-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upjpnrm-v.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upkorgt-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upkorgt-v.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upkorrm-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upkorrm-v.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upschgt-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upschgt-v.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upschrm-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/upschrm-v.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/uptchgt-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/uptchgt-v.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/uptchrm-h.vf
%{_texmfdistdir}/fonts/vf/uptex/jis/uptchrm-v.vf
%{_texmfdistdir}/fonts/vf/uptex/min/ugoth10.vf
%{_texmfdistdir}/fonts/vf/uptex/min/umin10.vf
%{_texmfdistdir}/fonts/vf/uptex/min/utgoth10.vf
%{_texmfdistdir}/fonts/vf/uptex/min/utmin10.vf
%{_texmfdistdir}/scripts/uptex/convbkmk.rb
%{_texmfdistdir}/tex/uplatex/base/jt2gt.fd
%{_texmfdistdir}/tex/uplatex/base/jt2mc.fd
%{_texmfdistdir}/tex/uplatex/base/jy2gt.fd
%{_texmfdistdir}/tex/uplatex/base/jy2mc.fd
%{_texmfdistdir}/tex/uplatex/base/ujarticle.cls
%{_texmfdistdir}/tex/uplatex/base/ujbk10.clo
%{_texmfdistdir}/tex/uplatex/base/ujbk11.clo
%{_texmfdistdir}/tex/uplatex/base/ujbk12.clo
%{_texmfdistdir}/tex/uplatex/base/ujbook.cls
%{_texmfdistdir}/tex/uplatex/base/ujreport.cls
%{_texmfdistdir}/tex/uplatex/base/ujsize10.clo
%{_texmfdistdir}/tex/uplatex/base/ujsize11.clo
%{_texmfdistdir}/tex/uplatex/base/ujsize12.clo
%{_texmfdistdir}/tex/uplatex/base/uplatex.ltx
%{_texmfdistdir}/tex/uplatex/base/uplcore.ltx
%{_texmfdistdir}/tex/uplatex/base/upldefs.ltx
%{_texmfdistdir}/tex/uplatex/base/uplpatch.ltx
%{_texmfdistdir}/tex/uplatex/base/uptrace.sty
%{_texmfdistdir}/tex/uplatex/base/utarticle.cls
%{_texmfdistdir}/tex/uplatex/base/utbk10.clo
%{_texmfdistdir}/tex/uplatex/base/utbk11.clo
%{_texmfdistdir}/tex/uplatex/base/utbk12.clo
%{_texmfdistdir}/tex/uplatex/base/utbook.cls
%{_texmfdistdir}/tex/uplatex/base/utreport.cls
%{_texmfdistdir}/tex/uplatex/base/utsize10.clo
%{_texmfdistdir}/tex/uplatex/base/utsize11.clo
%{_texmfdistdir}/tex/uplatex/base/utsize12.clo
%{_texmfdistdir}/tex/uplatex/config/uplatex.ini
%{_texmfdistdir}/tex/uptex/base/euptex.src
%{_texmfdistdir}/tex/uptex/base/ukinsoku.tex
%{_texmfdistdir}/tex/uptex/base/uptex.tex
%{_texmfdistdir}/tex/uptex/config/euptex.ini
%{_texmfdistdir}/tex/uptex/config/uptex.ini
%_texmf_fmtutil_d/uptex
%doc %{_texmfdistdir}/doc/uplatex/base/README_uplatex.txt
%doc %{_texmfdistdir}/doc/uptex/base/00readme_uptex.txt
%doc %{_texmfdistdir}/doc/uptex/base/01uptex_doc_utf8.txt
%doc %{_texmfdistdir}/doc/uptex/base/02uptex_changelog_utf8.txt
%doc %{_texmfdistdir}/doc/uptex/base/README_uptex.txt
%doc %{_texmfdistdir}/doc/uptex/base/samples/00readme_uptex_samples.txt
%doc %{_texmfdistdir}/doc/uptex/base/samples/Makefile
%doc %{_texmfdistdir}/doc/uptex/base/samples/adobe-cid.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/adobe-cns-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/adobe-gb-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/adobe-jp-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/adobe-kr-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/aozora-ujarticle-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/aozora-ujbook-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/aozora-ujreport-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/aozora-utarticle-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/aozora-utbook-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/aozora-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/aozora-utreport-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-euc-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-euc.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-jis-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-jis.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-sjis-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-sjis.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-uptex-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-uptex.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-utf8-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/area-utf8.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/bkmk-jis.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/bkmk-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/box-euc.eps
%doc %{_texmfdistdir}/doc/uptex/base/samples/box-jis.eps
%doc %{_texmfdistdir}/doc/uptex/base/samples/box-sjis.eps
%doc %{_texmfdistdir}/doc/uptex/base/samples/box-utf8.eps
%doc %{_texmfdistdir}/doc/uptex/base/samples/check_enc.pl
%doc %{_texmfdistdir}/doc/uptex/base/samples/cjk_babel.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/console_io.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/greek-uplatex.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/iotext.txt
%doc %{_texmfdistdir}/doc/uptex/base/samples/jbib1-jis.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/jbib2-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/jbtest.bib
%doc %{_texmfdistdir}/doc/uptex/base/samples/jis_uni_variation.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-euc-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-euc.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-jis-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-jis.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-sjis-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-sjis.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-uptex-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-uptex.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-utf8-incl.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/jstr-utf8.mp
%doc %{_texmfdistdir}/doc/uptex/base/samples/kinsoku-chk-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/linebreak.bib
%doc %{_texmfdistdir}/doc/uptex/base/samples/min10x.tfm
%doc %{_texmfdistdir}/doc/uptex/base/samples/misc-check-h-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/misc-check-v-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/otfsmpl-uplatex.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/sangoku-uplatex.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/sangoku-uptex.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/set3-check-h-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/simple-euc.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/simple-jis.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/simple-sjis.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/simple-u-jis.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/simple-u-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/simple-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/testrun.bat
%doc %{_texmfdistdir}/doc/uptex/base/samples/texxet-jis.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/umin10x.tfm
%doc %{_texmfdistdir}/doc/uptex/base/samples/uotftest-utf8.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/uotftest.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/utfsmpl-uplatex.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/widow.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/yaku-jsc-jis.tex
%doc %{_texmfdistdir}/doc/uptex/base/samples/yaku-jsc-utf8.tex
#- source
%doc %{_texmfdistdir}/source/fonts/uptex/Makefile
%doc %{_texmfdistdir}/source/fonts/uptex/README_ASCII_Corp.txt
%doc %{_texmfdistdir}/source/fonts/uptex/README_uptex_font.txt
%doc %{_texmfdistdir}/source/fonts/uptex/makepl.perl
%doc %{_texmfdistdir}/source/fonts/uptex/upjisr-h-hk.pl
%doc %{_texmfdistdir}/source/fonts/uptex/upjisr-h.pl
%doc %{_texmfdistdir}/source/fonts/uptex/upjisr-v.pl
%doc %{_texmfdistdir}/source/fonts/uptex/uprml-h-hk.pl
%doc %{_texmfdistdir}/source/fonts/uptex/uprml-h.pl
%doc %{_texmfdistdir}/source/uplatex/base/ujclasses.dtx
%doc %{_texmfdistdir}/source/uplatex/base/ukinsoku.dtx
%doc %{_texmfdistdir}/source/uplatex/base/uplatex.dtx
%doc %{_texmfdistdir}/source/uplatex/base/uplcls.ins
%doc %{_texmfdistdir}/source/uplatex/base/uplfmt.ins
%doc %{_texmfdistdir}/source/uplatex/base/uplfonts.dtx
%doc %{_texmfdistdir}/source/uplatex/base/uplvers.dtx

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_bindir}
pushd %{buildroot}%{_bindir}
    ln -sf %{_texmfdistdir}/scripts/uptex/convbkmk.rb convbkmk
popd
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
mkdir -p %{buildroot}%{_texmf_fmtutil_d}
cat > %{buildroot}%{_texmf_fmtutil_d}/uptex <<EOF
#
# from uptex:
uptex uptex - uptex.ini
euptex euptex language.def *euptex.ini
uplatex euptex language.dat *uplatex.ini
EOF


%changelog
* Fri Aug 10 2012 Paulo Andrade <pcpa@mandriva.com.br> 20120810-1
+ Revision: 813790
- Import texlive-uptex
- Import texlive-uptex

