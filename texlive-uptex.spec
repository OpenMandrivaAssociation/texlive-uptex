Name:		texlive-uptex
Version:	1.20
Release:	3
Summary:	Unicode version of pTeX
Group:		Publishing
URL:		http://tug.org/texlive
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/uptex.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea
Requires(post):	texlive-tetex
Requires:	texlive-ptex
Requires:	texlive-hyph-utf8
Requires:	texlive-adobemapping
Requires:	texlive-convbkmk
Requires:	texlive-ipaex
Requires:	texlive-japanese
Requires:	texlive-japanese-otf
Requires:	texlive-uptex.bin

%description
upTeX is an extension of pTeX, using UTF-8 input and producing
UTF-8 output. It was originally designed to improve support for
Japanese, but is also useful for documents in Chinese and
Korean. It can process Chinese simplified, Chinese traditional,
Japanese, and Korean simultaneously, and can also process
original LaTeX with \inputenc{utf8} and Babel
(Latin/Cyrillic/Greek etc.) by switching its \kcatcode tables.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/upmendex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_datadir}
cp -fpar texmf-dist %{buildroot}%{_datadir}
