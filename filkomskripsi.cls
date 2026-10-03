% filkomskripsi.cls -- unofficial FILKOM UB thesis class
% Copyright 2026 Pande Kadek Nathan Prabhaswara Sudiara Putra
% Distributed under the LPPL 1.3c or later.
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{filkomskripsi}[2026/10/03 v0.1.0 Unofficial FILKOM thesis class]

\RequirePackage{kvoptions}
\SetupKeyvalOptions{family=filkomclass,prefix=filkomclass@}
\DeclareBoolOption[true]{preview}
\DeclareComplementaryOption{official}{preview}
\DeclareStringOption[auto]{font}
\ProcessKeyvalOptions*
\LoadClass[a4paper,12pt,oneside]{report}

\RequirePackage[english,indonesian]{babel}
\RequirePackage{fontspec}
\RequirePackage{etoolbox}
\RequirePackage{csquotes}
\DeclareQuoteAlias[american]{english}{indonesian}
\RequirePackage[left=4cm,right=3cm,top=3cm,bottom=3cm]{geometry}
\RequirePackage{setspace}
\RequirePackage{indentfirst}
\RequirePackage{graphicx}
\RequirePackage{fancyhdr}
\RequirePackage{titlesec}
\RequirePackage[titles]{tocloft}
\RequirePackage{caption}
\RequirePackage{booktabs}
\RequirePackage{longtable}
\RequirePackage{array}
\RequirePackage{enumitem}
\RequirePackage[fleqn]{amsmath}
\RequirePackage{xurl}
\RequirePackage{hyperref}
\urlstyle{same}
\RequirePackage{xkeyval}

\newcommand{\filkom@judul}{}
\newcommand{\filkom@judulinggris}{}
\newcommand{\filkom@gelar}{Sarjana Komputer}
\newcommand{\filkom@fontdir}{}
\newcommand{\filkom@nama}{}
\newcommand{\filkom@nim}{}
\newcommand{\filkom@prodi}{}
\newcommand{\filkom@departemen}{}
\newcommand{\filkom@fakultas}{Fakultas Ilmu Komputer}
\newcommand{\filkom@universitas}{Universitas Brawijaya}
\newcommand{\filkom@kota}{Malang}
\newcommand{\filkom@tahun}{\the\year}
\newcommand{\filkom@pembimbingsatu}{}
\newcommand{\filkom@pembimbingdua}{}
\newcommand{\filkom@logo}{assets/logo-ub.png}

\define@key{filkom}{judul-inggris}{\renewcommand{\filkom@judulinggris}{#1}}
\define@key{filkom}{gelar}{\renewcommand{\filkom@gelar}{#1}}
\define@key{filkom}{font-dir}{\renewcommand{\filkom@fontdir}{#1}}
\define@key{filkom}{judul}{\renewcommand{\filkom@judul}{#1}}
\define@key{filkom}{nama}{\renewcommand{\filkom@nama}{#1}}
\define@key{filkom}{nim}{\renewcommand{\filkom@nim}{#1}}
\define@key{filkom}{program-studi}{\renewcommand{\filkom@prodi}{#1}}
\define@key{filkom}{departemen}{\renewcommand{\filkom@departemen}{#1}}
\define@key{filkom}{fakultas}{\renewcommand{\filkom@fakultas}{#1}}
\define@key{filkom}{universitas}{\renewcommand{\filkom@universitas}{#1}}
\define@key{filkom}{kota}{\renewcommand{\filkom@kota}{#1}}
\define@key{filkom}{tahun}{\renewcommand{\filkom@tahun}{#1}}
\define@key{filkom}{logo}{\renewcommand{\filkom@logo}{#1}}
\define@key{filkom}{pembimbing-1}{\renewcommand{\filkom@pembimbingsatu}{#1}}
\define@key{filkom}{pembimbing-2}{\renewcommand{\filkom@pembimbingdua}{#1}}
\newcommand{\filkomsetup}[1]{\setkeys{filkom}{#1}}

\newcommand{\filkom@calibri}{%
  \ifx\filkom@fontdir\@empty
    \IfFontExistsTF{Calibri}{\setmainfont{Calibri}}{%
      \ClassError{filkomskripsi}{Calibri wajib tetapi tidak ditemukan}{Gunakan preview, pasang Calibri legal, atau isi font-dir dengan berkas font legal.}}%
  \else
    \setmainfont{calibri}[Path=\filkom@fontdir,Extension=.ttf,
      UprightFont=*,BoldFont=calibrib,ItalicFont=calibrii,BoldItalicFont=calibriz]%
  \fi}
\newcommand{\filkom@carlito}{%
  \IfFontExistsTF{Carlito}{\setmainfont{Carlito}}{%
    \setmainfont{Carlito-Regular.ttf}[BoldFont=Carlito-Bold.ttf,
      ItalicFont=Carlito-Italic.ttf,BoldItalicFont=Carlito-BoldItalic.ttf]}}
\newcommand{\filkom@setupfont}{%
  \ifdefstring{\filkomclass@font}{auto}{%
    \iffilkomclass@preview
      \ifx\filkom@fontdir\@empty
        \IfFontExistsTF{Calibri}{\filkom@calibri}{\filkom@carlito}%
      \else\filkom@calibri\fi
    \else\filkom@calibri\fi
  }{%
    \ifdefstring{\filkomclass@font}{carlito}{%
      \iffilkomclass@preview\filkom@carlito\else
        \ClassError{filkomskripsi}{Carlito tidak diizinkan dalam mode official}{Pilih font=calibri untuk keluaran official.}\fi
    }{%
      \ifdefstring{\filkomclass@font}{calibri}{\filkom@calibri}{%
        \ClassError{filkomskripsi}{Pilihan font tidak dikenal}{Pilih auto, carlito, atau calibri.}}}}
  \hypersetup{hidelinks,pdfauthor={\filkom@nama},pdftitle={\filkom@judul}}}
\AtEndPreamble{\filkom@setupfont}

\newcommand{\filkom@require}[2]{%
  \ifx#1\@empty
    \ClassError{filkomskripsi}{Metadata #2 belum diisi}{Isi kunci #2 pada metadata.tex.}%
  \fi
}
\AtBeginDocument{%
  \filkom@require{\filkom@judul}{judul}%
  \filkom@require{\filkom@judulinggris}{judul-inggris}%
  \filkom@require{\filkom@nama}{nama}%
  \filkom@require{\filkom@nim}{nim}%
  \filkom@require{\filkom@prodi}{program-studi}%
  \filkom@require{\filkom@departemen}{departemen}%
  \filkom@require{\filkom@pembimbingsatu}{pembimbing-1}%
  \filkom@require{\filkom@pembimbingdua}{pembimbing-2}%
}

\setstretch{1}
\setlength{\parindent}{0.6cm}
\setlength{\parskip}{6pt}
\AtBeginDocument{\setlength{\mathindent}{10\fontdimen2\font}}
\clubpenalty=10000
\widowpenalty=10000
\displaywidowpenalty=10000
\setlist{nosep}
\captionsetup{font={normalsize,bf},labelsep=space,justification=centering}
\hypersetup{hidelinks,pdfauthor={\filkom@nama},pdftitle={\filkom@judul}}

\titleformat{\chapter}[block]
  {\centering\bfseries\fontsize{16pt}{19pt}\selectfont}
  {BAB \thechapter}{0.75em}{\MakeUppercase}
\titlespacing*{\chapter}{0pt}{0pt}{18pt}
\titleformat{name=\chapter,numberless}[block]
  {\centering\bfseries\fontsize{16pt}{19pt}\selectfont}
  {}{0pt}{\MakeUppercase}
\titleformat{\section}{\bfseries\fontsize{14pt}{17pt}\selectfont}{\thesection}{0.75em}{}
\titleformat{\subsection}{\bfseries\fontsize{14pt}{17pt}\selectfont}{\thesubsection}{0.75em}{}
\titleformat{\subsubsection}{\bfseries\itshape\fontsize{12pt}{14pt}\selectfont}{\thesubsubsection}{0.75em}{}
\titlespacing*{\section}{0pt}{12pt}{6pt}
\titlespacing*{\subsection}{0pt}{9pt}{6pt}
\titlespacing*{\subsubsection}{0pt}{9pt}{6pt}
\setcounter{secnumdepth}{3}
\setcounter{tocdepth}{3}
\renewcommand{\cftchappresnum}{BAB\space}
\setlength{\cftchapnumwidth}{4.2em}

\pagestyle{fancy}
\fancyhf{}
\cfoot{\fontsize{10pt}{12pt}\selectfont\thepage}
\renewcommand{\headrulewidth}{0pt}
\renewcommand{\footrulewidth}{0pt}
\fancypagestyle{plain}{%
  \fancyhf{}%
  \cfoot{\fontsize{10pt}{12pt}\selectfont\thepage}%
  \renewcommand{\headrulewidth}{0pt}%
  \renewcommand{\footrulewidth}{0pt}}

\newcommand{\makeskripsicover}{%
  \hypersetup{pageanchor=false}%
  \begin{titlepage}
    \thispagestyle{empty}
    \setlength{\parskip}{0pt}
    \centering
    {\bfseries\fontsize{16pt}{19pt}\selectfont\MakeUppercase{\filkom@judul}\par}
    \vspace{0.8cm}
    {\fontsize{14pt}{17pt}\selectfont
    {\bfseries SKRIPSI\par}
    \vspace{0.45cm}
    {Diajukan untuk memenuhi sebagian persyaratan\par}
    {memperoleh gelar \filkom@gelar\par}
    \vspace{0.65cm}
    {Disusun oleh:\par}
    \vspace{0.25cm}
    {\filkom@nama\par}
    {NIM: \filkom@nim\par}
    \vfill
    \IfFileExists{\filkom@logo}{\includegraphics[width=5cm]{\filkom@logo}}{%
      \ClassError{filkomskripsi}{Logo tidak ditemukan: \filkom@logo}{Periksa kunci logo pada metadata.tex.}}
    \vfill
    {\MakeUppercase{PROGRAM STUDI \filkom@prodi}\par}
    {\MakeUppercase{\filkom@departemen}\par}
    {\MakeUppercase{\filkom@fakultas}\par}
    {\MakeUppercase{\filkom@universitas}\par}
    {\MakeUppercase{\filkom@kota}\par}
    {\filkom@tahun\par}
    }
  \end{titlepage}
  \hypersetup{pageanchor=true}%
}

\addto\captionsindonesian{%
  \renewcommand{\contentsname}{DAFTAR ISI}%
  \renewcommand{\listtablename}{DAFTAR TABEL}%
  \renewcommand{\listfigurename}{DAFTAR GAMBAR}%
}

\newcommand{\skripsifrontmatter}{\clearpage\pagenumbering{roman}\setcounter{page}{2}}
\newcommand{\skripsifrontchapter}[1]{\clearpage\phantomsection\chapter*{#1}\addcontentsline{toc}{chapter}{#1}}
\newcommand{\listofappendices}{\chapter*{DAFTAR LAMPIRAN}\@starttoc{loa}}
\newcommand{\l@skripsiappendix}[2]{\@dottedtocline{0}{0pt}{7em}{#1}{#2}}
\newcommand{\makeskripsilists}{%
  \clearpage\phantomsection\addcontentsline{toc}{chapter}{\contentsname}\tableofcontents\clearpage
  \phantomsection\addcontentsline{toc}{chapter}{\listtablename}\listoftables\clearpage
  \phantomsection\addcontentsline{toc}{chapter}{\listfigurename}\listoffigures\clearpage
  \phantomsection\addcontentsline{toc}{chapter}{DAFTAR LAMPIRAN}\listofappendices\clearpage
}
\newcommand{\skripsimainmatter}{\clearpage\pagenumbering{arabic}\setcounter{page}{1}}
\newcommand{\skripsiappendix}[1]{%
  \refstepcounter{chapter}%
  \chapter*{LAMPIRAN \thechapter\space \MakeUppercase{#1}}%
  \addcontentsline{toc}{chapter}{LAMPIRAN \thechapter\texorpdfstring{\quad}{ }#1}%
  \addcontentsline{loa}{skripsiappendix}{\protect\numberline{LAMPIRAN \thechapter}#1}}

\newcommand{\namamahasiswa}{\filkom@nama}
\newcommand{\nimmahasiswa}{\filkom@nim}
\newcommand{\judulskripsi}{\filkom@judul}
\newcommand{\judulskripsiinggris}{\filkom@judulinggris}
\newcommand{\pembimbingsatu}{\filkom@pembimbingsatu}
\newcommand{\pembimbingdua}{\filkom@pembimbingdua}
\endinput
