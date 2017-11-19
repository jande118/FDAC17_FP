%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% This will be my template for research proposals
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
\NeedsTexFormat{LaTeX2e}
\ProvidesClass{proposal}[2017/10/15 Jacob Miller's Proposal Class]


\LoadClass[11pt]{article}

\RequirePackage{fancyhdr}
%\RequirePackage[top=1in,bottom=1in,left=1in,right=1in]{geometry}
\RequirePackage{graphicx}
\graphicspath{ {images/} }
\RequirePackage{empheq}
\RequirePackage{advdate}
\RequirePackage{ifthen}
\RequirePackage{amsthm}
\RequirePackage{amssymb}
\RequirePackage{mathtools}
\RequirePackage{mdframed}
\RequirePackage{color,soul,amsmath,eucal,amscd,mathpazo}


% Useful commands
\newcommand{\yesterday}{{\AdvanceDate[-1]\today}}
\renewcommand\typesetChapterTitle[1]{#1}
\newcommand{\edit}[1][!!!!!]{\textcolor{red}{\hl{#1}}}
% convenient absolute value
\DeclarePairedDelimiter\abs{\lvert}{\rvert}
\makeatletter
\let\oldabs\abs
\def\abs{\@ifstar{\oldabs}{\oldabs*}} % star prevents auto resize
\makeatother
% convenient space shorthands
\newcommand{\Rone}{\mathbb{R}}
\newcommand{\Rtwo}{\mathbb{R}^{2}}
\newcommand{\Rthree}{\mathbb{R}^{3}}
\newcommand{\Natnums}{\mathbb{N}}
\newcommand{\Integers}{\mathbb{Z}}
% big O notation
\newcommand{\Obig}{\mathcal{O}}



% Title Defaults 
\author{Jacob K. Miller}
\def\@title{Research Proposal}

% Set counters for sections
\setcounter{section}{0}
\setcounter{secnumdepth}{2}

% Set up formatting for theorems, proofs, and lemmas
\newtheorem{theorem}{Theorem}[section]
\newtheorem{corollary}{Corollary}[theorem]
\newtheorem{lemma}{Lemma}
\newtheorem{proposition}{Proposition}

\pagestyle{fancy}
\fancyhf{}
\renewcommand{\headrulewidth}{0pt}
\lhead{}
\chead{}
\rhead{}
\lfoot{}
\cfoot{\thepage}
\rfoot{}

\endinput
