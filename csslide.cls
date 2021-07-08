%
% Document class for slides used for the Institute of Photogrammetry in
% Bonn
%


\def\filedate{28/09/2003} 
\def\fileversion{0.6}
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{csslide}[\filedate\space v\fileversion\space]
\typeout{\space\space CS seminar class v\fileversion\space \filedate\space
for slides}


\RequirePackage{fancyhdr}
% if you want a different font, specify it here!
\RequirePackage{times}
%\RequirePackage{palatino}
\RequirePackage{epsfig}
\RequirePackage{graphicx}
\RequirePackage{ifthen}
\RequirePackage{fancybox}
\AtEndOfClass{
  }

% ------------------------------ Option Declaration

\DeclareOption*{\PassOptionsToClass{\CurrentOption}{seminar}}

\def\CSheadersep{0.5in}
\def\CSfootersep{0.25in}

% ------------------------------ Ausfuhrung von Optionen

\ProcessOptions

% ------------------------------ Laden von Paketen

\LoadClass[slidesec]{seminar}

% ------------------------------ Hauptteil

\definecolor{grey}{rgb}{0.5,0.5,0.5}

% for patches to seminar class
%\input{seminar.bug}
%\input{seminar.bg2}

% To adjust the frame length to the header and footer ones
%\autoslidemarginstrue

% The following definitions can be redefined in your document
\def\CSSlidesTitle{}
% if this is empty, \CSSlidesTitle will be used for the heading
\def\CSSlidesHeadingTitle{}
\def\CSSlidesCourse{}
% the following image should be (roughly) square
\def\CSSlidesOrganizationI{Mathematics and Computer Science}
\def\CSSlidesOrganizationII{Mount Allison University}

\def\CSSlidesAuthor{\today}
\def\CSSlidesFooterLeft{\CSSlidesAuthor}
%\def\CSSlidesFooterLeft{\CSSlidesCourse} 
\def\CSSlidesFooterMiddle{}
\def\CSSlidesFooterRight{Page \thepage}

% To center horizontally the headers and footers (see seminar.bug)
\renewcommand{\headwidth}{\textwidth}
\renewcommand{\headheight}{\textheight}


\addtolength{\slideheight}{1.5cm}
\addtolength{\slidewidth}{1.5cm} 


% for the user to manually adjust width and height
\newcommand{\CSAddToSlideWidth}[1]{%
  \addtolength{\slidewidth}{#1}
}


% new paragraphs should start on the very left side
\parindent0pt
\parskip0.2em

% adjust additional  distance to header and footer
\renewcommand{\slidetopmargin}{\CSheadersep}
\renewcommand{\slidebottommargin}{\CSfootersep}

% Fancy Headings
\fancyhf{}

\newlength{\mytitlewidthI}
\newlength{\mytitlewidthII}
\newcommand{\CSfancyheadersets}{%
  \fancyhead[L]{\sf
  \ifthenelse{\equal{\CSSlidesCourse}{}}% then
    {}{\small \textcolor{grey}{\CSSlidesCourse}}
    \vspace{0mm}
    \hspace{0.7mm}
    }
  \fancyhead[R]{\sf   %
    \ifthenelse{\equal{\CSSlidesHeadingTitle}{}}% then
    { \small \textcolor{grey}{\CSSlidesTitle}}{ % else
      \small \textcolor{grey}{\CSSlidesHeadingTitle}}
    \vspace{0mm}
    \hspace{0.7mm}}}

\newcommand{\CSfancyfootersets}{%
  \fancyfoot[L]{\scriptsize \hspace*{1.2mm} \sf
  		\textcolor{grey}{\CSSlidesFooterLeft}}
  \fancyfoot[C]{\scriptsize \sf \textcolor{grey}{\CSSlidesFooterMiddle}}
  \fancyfoot[R]{\scriptsize \sf
  		\textcolor{grey}{\CSSlidesFooterRight} \hspace{1.2mm}}}
  
\fancypagestyle{plain}{
  \fancyhf{}
  \CSfancyheadersets
  \renewcommand{\headrulewidth}{0.2mm}
  \renewcommand{\footrulewidth}{0.2mm}
  }  

% settings for fancy style
\renewcommand{\headrulewidth}{0.2mm}
\renewcommand{\footrulewidth}{0.2mm}
\CSfancyheadersets
\CSfancyfootersets

\def\printlandscape{\special{landscape}}    % Works with dvips.

\slideframe{none}
\pagestyle{fancy}
%\slideframe{plain}
%\pagestyle{plain}


% settings for title page
\title{\Large \CSSlidesTitle}
\author{\CSSlidesCourse}
\date{\CSSlidesAuthor}

% command for automatically generating Titlepage inside a slide
\newcommand{\makeCSSlidesTitle}{
  \pagestyle{plain}
  \maketitle
  \addtocounter{slide}{-1}
}

% renew commands for slideheading and slidesubheading
\newlength{\myheadingwidth} % you could also use \linewidth, meybe better...
\renewcommand{\makeslideheading}[1]%
{\setlength{\fboxrule}{.15mm}%
 \settowidth{\myheadingwidth}{\Large \textbf{#1}} %
 \addtolength{\myheadingwidth}{3em}%
 \begin{center}%
     \centering \shadowbox{\parbox[t][4ex]{\myheadingwidth}%
       {\vspace{0.5ex}\centerline{\Large \textbf{#1} }}} 
  \end{center}%
}

\renewcommand{\makeslidesubheading}[1]{%
  \setlength{\fboxrule}{.4mm}%
  \settowidth{\myheadingwidth}{\large #1} %
  \addtolength{\myheadingwidth}{3em} %
  \begin{center}%
      \fbox{\parbox[t][3.6ex]{\myheadingwidth}%
        {\vspace{0.7ex}\centerline{\large #1 }}} %
  \end{center}%
}

% and now a heading kind of thing 
\newcommand{\CSbox}[1]{%
  \setlength{\fboxrule}{.2mm}%
  \settowidth{\myheadingwidth}{#1} %
  \addtolength{\myheadingwidth}{2em} %
  \begin{center}%
      \fbox{\parbox[t][2.5ex]{\myheadingwidth}%
        {\vspace{0.4ex}\centerline{ #1 }}} %
  \end{center}
}

