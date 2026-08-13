%global tl_name uptex
%global tl_revision 77830

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Unicode version of pTeX
Group:		Publishing
URL:		https://www.ctan.org/pkg/uptex
License:	other-free
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Requires:	texlive(cm)
Requires:	texlive(etex)
Requires:	texlive(hyphen-base)
Requires:	texlive(knuth-lib)
Requires:	texlive(plain)
Requires:	texlive(ptex-base)
Requires:	texlive(uptex-base)
Requires:	texlive(uptex-fonts)
Requires:	texlive(uptex.bin)
Requires:	texlive-tlpkg
Provides:	texlive(%{tl_name}) = %{version}

%description
upTeX is an extension of pTeX, using UTF-8 input and producing UTF-8
output. It was originally designed to improve support for Japanese, but
is also useful for documents in Chinese and Korean. It can process
Chinese simplified, Chinese traditional, Japanese, and Korean
simultaneously, and can also process original LaTeX with \inputenc{utf8}
and Babel (Latin/Cyrillic/Greek etc.) by switching its \kcatcode tables.


%install -a
mkdir -p %{buildroot}%{_texmf_updmap_d}
cat > %{buildroot}%{_texmf_updmap_d}/%{tl_name} <<'TL_DROPIN_EOF'
# from uptex:
KanjiMap uptex-@jaEmbed@@jaVariant@.map
KanjiMap uptex-ko-@koEmbed@.map
KanjiMap uptex-sc-@scEmbed@.map
KanjiMap uptex-tc-@tcEmbed@.map
TL_DROPIN_EOF
