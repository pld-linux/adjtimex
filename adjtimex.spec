Summary:	A utility for adjusting kernel time variables
Summary(cs):	Program pro nastavování èasovıch promìnnıch jádra
Summary(da):	Et værktøj til at justere kernetidsvariabler
Summary(de):	Ein Dienstprogramm für die Einstellung der Kernel-Zeitvariablen
Summary(es):	Utilidad para modificar las variables de tiempo del kernel
Summary(fr):	Utilitaire pour le réglage de l'horloge du noyau
Summary(id):	Utility untuk menyamakan variabel time kernel
Summary(is):	Tól til ağ stilla tímabreytur í kjarna
Summary(it):	Utility per modificare le variabili temporali del kernel
Summary(ja):	¥«¡¼¥Í¥ë¤Î»ş´ÖÊÑ¿ô¤òÄ´À°¤¹¤ë¤¿¤á¤Î¥æ¡¼¥Æ¥£¥ê¥Æ¥£
Summary(no):	Et verktøy for å justere kjernens tidsvariabler
Summary(pl):	Narzêdzie do regulacji zmiennych czasu kernela
Summary(pt):	Um utilitário para ajustar as variáveis de tempo do núcleo
Summary(ru):	õÔÉÌÉÔÁ ÄÌÑ ×ÎÅÓÅÎÉÑ ĞÏĞÒÁ×ÏË × ĞÅÒÅÍÅÎÎÙÅ ×ÒÅÍÅÎÉ ÑÄÒÁ
Summary(sk):	Pomôcka pre úpravu premennıch hodín jadra
Summary(sl):	Pripomoèek za prikrojitev èasovnih spremenljivk jedra
Summary(sv):	Ett verktyg för att justera kärnans tidsvariabler
Summary(uk):	õÔÉÌ¦ÔÁ ÄÌÑ ×ÎÅÓÅÎÎÑ ĞÏĞÒÁ×ÏË × ÚÍ¦ÎÎ¦ ŞÁÓÕ ÑÄÒÁ
Summary(zh_CN):	ÓÃÓÚµ÷ÕûÄÚºËÊ±¼ä±äÁ¿µÄÊµÓÃ³ÌĞò¡£
Name:		adjtimex
Version:	1.13
Release:	2
License:	GPL
Group:		Base
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/admin/time/%{name}-%{version}.tar.gz
Patch0:		%{name}-getopt.patch
Patch1:		%{name}-ia64.patch
Patch2:		%{name}-fixman.patch
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_sbindir		/sbin

%description
Adjtimex provides raw access to kernel time variables. On standalone
or intermittently connected machines, root can use adjtimex to correct
for systematic drift. If your machine is connected to the Internet or
is equipped with a precision oscillator or radio clock, you should
instead manage the system clock with the xntpd program. Users can use
adjtimex to view kernel time variables.

%description -l cs
Adjtimex poskytuje syrovı pøístup k èasovım promìnnım jádra. Na
poèítaèi, kterı není zasí»ovanı nebo se pøipojuje k Internetu pouze
obèas, mù¾e root pou¾ívat adjtimex pro korekci trvalého driftu hodin
(tj. pokud se systémové hodiny za bìhu operaèního systému zpomalují
nebo zrychlují proti pøesnému èasu). Jestli¾e je vá¹ poèítaè pøipojen
do Internetu nebo je vybaven pøesnım oscilátorem nebo rádiem øízenımi
hodinami, mìli byste místo adjtimexu nastavovat systémové hodiny
programem xntpd. U¾ivatelé mohou pou¾ívat program adjtimex pro ètení
èasovıch promìnnıch jádra.

%description -l da
Adjtimex giver direkte adgang til kernens tidvariabler. På fritstående
eller midlertidige tilkoblede maskiner, kan root bruge adjtimex til at
korrigere systemets tidsafvigelse. Hvis din maskine er tilkoblet
Internet eller er udstyret med en precisionsoscillator eller
radioklokke, bør du hellere bruge xntpd programmet til at styre
klokken. Brugere kan bruge adjtimex til at vise kernens tidsvariabler.

%description -l de
Adjtimex ermöglicht den direkten Zugriff auf die Zeitvariablen des
Kernels. Bei nicht vernetzten oder nur zeitweise mit dem Netz
verbundenen Computern kann Root mit Hilfe von adjtimex die
systematische Zeitabweichung korrigieren. Wenn Ihr Rechner mit dem
Internet verbunden oder mit einem Präzisionsoszillator oder einer
Funkuhr ausgerüstet ist, sollten Sie die Systemuhr stattdessen mit dem
Programm xntpd einstellen. Die Benutzer können mit adjtimex die
Zeitvariablen des Kernels anzeigen.

%description -l es
Adjtimex proporciona un acceso de bajo nivel a las variables de tiempo
del kernel. En máquinas independientes o en máquinas conectadas a
intervalos, el usuario raíz puede utilizar adjtimex para corregir el
margen de error del reloj. Si el ordenador está conectado a Internet o
está dotado de un oscilador de precisión o un reloj radio, debería
poder usar el programa xntpd para corregir la hora. Los usuarios
pueden usar adjtimex para ver las variables de tiempo del kernel.

%description -l fr
Adjtimex offre un accès direct à l'horloge du noyau. Sur les
ordinateurs autonomes ou connectés de façon intermittente, un
utilisateur connecté en tant que root peut utiliser adjtimex pour
corriger la dérive systématique. Si votre ordinateur est connecté à
Internet ou équipé d'un oscillateur de précision ou d'une horloge
radio, gérez plutôt l'horloge système avec le programme xntpd. Les
utilisateurs peuvent utiliser adjtimex pour voir les variables de
temps du noyau.

%description -l id
Adjtimex menyediakan raw access terhadap variable time pada kernel.
Pada computer yang standalone atau tidak selalu tersambung pada
jaringan, root dapat menggunakan adjtimex untuk melakukan koreksi bagi
systematic drift. Bila mesin anda tersambung dengan Internet atau
dilengkapi dengan precision oscillator atau radio clock, sebaiknya
anda melakukan hal ini menggunakan program xntpd. Pengguna menggunakan
adjtimex untuk melihat variable time pada kernel.

%description -l is
Adjtimex gefur hráan ağgang ağ tímabreytum kjarna. A netlausum eğa
viğ-og-viğ tengdum vélum getur rót notağ adjtimex til şess ağ
leiğrétta rek á klukku. Ef vélin şín er tengd viğ internetiğ eğa er
meğ nákvæmt tímamælingartæki ættir şú frekar ağ breyta kerfisklukkunni
meğ xntpd forritinu. Notendur geta notağ adjtimex til şess ağ sjá
tímabreytur kjarna.

%description -l it
Adjtimex fornisce un accesso di basso livello alle variabili temporali
del kernel. Su elaboratori indipendenti o connessi in
modointermittente, il root può utilizzare adjtimex per correggere la
deriva sistematica dell'orologio. Se l'elaboratore è connesso a
Internet o dotato di oscillatore di precisione o orologio radio si
consiglia di utilizzare il programma xntpd per gestire l'orologio di
sistema. Gli utenti possono utilizzare adjtimex per visualizzare le
variabili temporali del kernel.

%description -l ja
adjtimex ¤Ï¡¢¥«¡¼¥Í¥ë¤Î»ş´ÖÊÑ¿ô¤Ø¤ÎÄ¾ÀÜ¥¢¥¯¥»¥¹¤òÄó¶¡¤·¤Ş¤¹¡£
¥¹¥¿¥ó¥É¥¢¥í¡¼¥ó¤Ş¤¿¤ÏÁê¸ßÀÜÂ³¤µ¤ì¤¿¥Ş¥·¥ó¾å¤Ç¡¢root ¥æ¡¼¥¶¡¼¤Ï
adjtimex
¤ò»ÈÍÑ¤·¤Æ¥·¥¹¥Æ¥à¤Î»ş´Ö¸íº¹¤ò½¤Àµ¤Ç¤­¤Ş¤¹¡£¤´»ÈÍÑ¤Î¥Ş¥·¥ó¤¬¥¤¥ó¥¿¡¼¥Í¥Ã¥È
¤ËÀÜÂ³¤µ¤ì¤Æ¤¤¤ë¾ì¹ç¡¢¤Ş¤¿¤ÏÀºÅÙÈ¯¿¶´ï¤ä¥é¥¸¥ª
¥¯¥í¥Ã¥¯¤¬ÁõÈ÷¤µ¤ì¤Æ¤¤¤ë¾ì¹ç¡¢Âå¤ï¤ê¤Ë xntpd ¥×¥í¥°¥é¥à¤ò
»ÈÍÑ¤·¤Æ¥·¥¹¥Æ¥à¥¯¥í¥Ã¥¯¤ò´ÉÍı¤¹¤ëÉ¬Í×¤¬¤¢¤ê¤Ş¤¹¡£¥æ¡¼¥¶¡¼¤Ï¡¢
adjtimex ¤ò»ÈÍÑ¤·¤Æ¡¢¥«¡¼¥Í¥ë¤Î»ş´ÖÊÑ¿ô¤ò»²¾È¤Ç¤­¤Ş¤¹¡£

%description -l no
Adjtimex gir direkte tilgang til kjernens tidvariabler. På
frittstående eller midlertidige tilkoblede maskiner, kan root bruke
adjtimex til å korrigere systemets tidsavvik. Hvis din maskin er
tilkoblet Internett eller er utstyrt med en presisjonsoscillator eller
radioklokke, bør du heller bruke xntpd programmet til å styre klokken.
Brukere kan bruke adjtimex til å vise kjernens tidsvariabler.

%description -l pl
Adjtimex umo¿liwia niskopoziomowy dostêp do zmiennych czasu
systemowego. W systemach wolnostoj±cych lub pod³±czonych do Internetu
w sposób nieci±g³y, program ten mo¿e zostaæ wykorzystany przez roota
do korekcji dryfu zegara systemowego. Je¶li maszyna jest pod³±czona do
Internetu lub wyposa¿ona w precyzyjny generator czêstotliwo¶ci lub
zegar radiowy, lepiej do korekcji czasu systemowego u¿ywaæ zamiast
niego programu xntpd. Zwykli u¿ytkownicy mog± za pomoc± adjtimex
podgl±daæ zmienne czasu.

%description -l pt
O adjtimex fornece o acesso em bruto às variáveis temporais do núcleo.
Em sistemas autónomos ou em máquinas ligadas intermitentemente, o
'root' pode usar o 'adjtimex' para corrigir desvios sistemáticos. Se a
máquina do utilizador está ligada à Internet ou está equipada com um
oscilador de precisão ou um relógio-rádio, então deve-se ajustar o
relógio do sistema com o programa xntpd. Os utilizadores podem usar o
adjtimex para verificar as variáveis temporais do núcleo.

%description -l ru
Adjtimex ÏÂÅÓĞÅŞÉ×ÁÅÔ ĞÒÑÍÏÊ ÄÏÓÔÕĞ Ë ĞÅÒÅÍÅÎÎÙÍ ×ÒÅÍÅÎÉ ÓÉÓÔÅÍÙ. îÁ
ËÏÍĞØÀÔÅÒÁÈ, ÎÅ ĞÏÄËÌÀŞÅÎÎÙÈ ÉÌÉ ĞÅÒÉÏÄÉŞÅÓËÉ ĞÏÄËÌÀŞÁÅÍÙÈ Ë ÓÅÔÉ,
ÁÄÍÉÎÉÓÔÒÁÔÏÒ ÍÏÖÅÔ ÉÓĞÏÌØÚÏ×ÁÔØ adjtimex ÄÌÑ ËÏÒÒÅËÔÉÒÏ×ËÉ
ÓÉÓÔÅÍÁÔÉŞÅÓËÉÈ ÏÔËÌÏÎÅÎÉÊ ×Ï ×ÒÅÍÅÎÉ. åÓÌÉ ×ÁÛÁ ÍÁÛÉÎÁ ÉÍÅÅÔ ÄÏÓÔÕĞ Ë
Internet ÉÌÉ ÏÂÏÒÕÄÏ×ÁÎÁ ÔÏŞÎÙÍ ÇÅÔÅÒÏÄÉÎÏÍ ÉÌÉ ÒÁÄÉÏŞÁÓÁÍÉ, ÔÏ ×ÁÍ
ÌÕŞÛÅ ÕĞÒÁ×ÌÑÔØ ÓÉÓÔÅÍÎÙÍÉ ŞÁÓÁÍÉ Ó ĞÏÍÏØÀ ĞÒÏÇÒÁÍÍÙ xntpd. ÷Ù ÍÏÖÅÔÅ
ÉÓĞÏÌØÚÏ×ÁÔØ adjtimex ÄÌÑ ĞÒÏÓÍÏÔÒÁ ĞÅÒÅÍÅÎÎÙÈ ×ÒÅÍÅÎÉ ÓÉÓÔÅÍÙ.

%description -l sk
Adjtimex poskytuje nízkoúrovòovı prístup k èasovım premennım jadra. Na
samostatnıch alebo len prechodne pripojenıch poèítaèoch mô¾e
superpou¾ívateµ korigova» systematickı posun hodín systému. Pokiaµ je
váµ poèítaè pripojenı k Internetu alebo je vybavenı presnım
oscilátorom alebo rádiovımi hodinami, mali by ste spravova» systémové
hodiny programom xntpd. Obyèajní pou¾ívatelia mô¾u adjtimex-om
prezera» nastavenie príslu¹nıch premennıch jadra.

%description -l sv
Adjtimex erbjuder rå tillgång till kärnans tidsvariabler. På
fristående eller intermittent uppkopplade maskiner, kan root använda
adjtimex för att korrigera för systematisk drift. Om din maskin är
uppkopplad till Internet eller utrustad med en precisionsoscillator
eller radioklocka skall du istället styra systemklockan med
xntpd-programmet. Användare kan använda adjtimex för att se kärnans
tidsvariabler.

%description -l uk
Adjtimex ÄÏÚ×ÏÌÑ¤ ÍÁÎ¦ĞÕÌÀ×ÁÔÉ Ú ËÏÍÁÎÄÎÏÇÏ ÒÑÄËÁ ÚÍ¦ÎÎÉÍÉ ÑÄÒÁ, ÑË¦
×¦ÄĞÏ×¦ÄÁÀÔØ ÚÁ ËÏÒÅËÃ¦À ÈÏÄÕ ÓÉÓÔÅÍÎÏÇÏ ÇÏÄÉÎÎÉËÁ. úÁ×ÄÑËÉ ÃØÏÍÕ ¤
ÍÏÖÌÉ×¦ÓÔØ ËÏÒÅÇÕ×ÁÔÉ ÓÉÓÔÅÍÎÉÊ ÇÏÄÉÎÎÉË ÂÅÚ ×ÉËÏÒÉÓÔÁÎÎÑ ntpd, ËÏÔÒÉÊ
×ÉÍÁÇÁ¤ ÎÁÑ×ÎÏÓÔ¦ ĞÏÓÔ¦ÊÎÏÇÏ Ú×'ÑÚËÕ Ú ÅÔÁÌÏÎÎÉÍ ÇÏÄÉÎÎÉËÏÍ.

ğ¦ÄÔÒÉÍÕ¤ÔØÓÑ ĞÏÒ¦×ÎÑÎÎÑ ×ÁÛÏÇÏ ÓÉÓÔÅÍÎÏÇÏ ÇÏÄÉÎÎÉËÁ Ú ÅÔÁÌÏÎÎÉÍ
ÄÖÅÒÅÌÏÍ ŞÁÓÕ, ×ËÌÀŞÁÀŞÉ RTC ×ÁÛÏÇÏ ËÏÍĞ'ÀÔÅÒÁ.

%description -l zh_CN
Adjtimex
Ìá¹©ÁË¶ÔÔ­Ê¼ÄÚºËÊ±¼ä±äÁ¿µÄ´æÈ¡¹¦ÄÜ¡£ÔÚ¶ÀÁ¢»ò¼äĞªÊ½Á¬½ÓµÄ¼ÆËã»úÉÏ£¬
¸ù¿ÉÒÔÊ¹ÓÃ adjtimex Ğ£ÕıÏµÍ³Æ«²î¡£Èç¹ûÄúµÄ¼ÆËã»úÒÑÁ¬½ÓÖÁ Internet£¬
»òÕßÅä±¸ÁË¾«ÃÜÕñµ´Æ÷»òÎŞÏßµçÊ±ÖÓ£¬ÔòÓ¦¸ÃÊ¹ÓÃ xntpd ³ÌĞò¹ÜÀíÏµÍ³Ê±ÖÓ¡£
ÓÃ»§¿ÉÒÔÊ¹ÓÃ adjtimex ²é¿´ÄÚºËÊ±¼ä±äÁ¿¡£

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__autoconf}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install adjtimex $RPM_BUILD_ROOT%{_sbindir}
install adjtimex.8 $RPM_BUILD_ROOT%{_mandir}/man8

gzip -9nf README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
