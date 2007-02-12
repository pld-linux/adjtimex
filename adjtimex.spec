Summary:	A utility for adjusting kernel time variables
Summary(cs.UTF-8):	Program pro nastavování časových proměnných jádra
Summary(da.UTF-8):	Et værktøj til at justere kernetidsvariabler
Summary(de.UTF-8):	Ein Dienstprogramm für die Einstellung der Kernel-Zeitvariablen
Summary(es.UTF-8):	Utilidad para modificar las variables de tiempo del kernel
Summary(fr.UTF-8):	Utilitaire pour le réglage de l'horloge du noyau
Summary(id.UTF-8):	Utility untuk menyamakan variabel time kernel
Summary(is.UTF-8):	Tól til að stilla tímabreytur í kjarna
Summary(it.UTF-8):	Utility per modificare le variabili temporali del kernel
Summary(ja.UTF-8):	カーネルの時間変数を調整するためのユーティリティ
Summary(nb.UTF-8):	Et verktøy for å justere kjernens tidsvariabler
Summary(pl.UTF-8):	Narzędzie do regulacji zmiennych czasu kernela
Summary(pt.UTF-8):	Um utilitário para ajustar as variáveis de tempo do núcleo
Summary(ru.UTF-8):	Утилита для внесения поправок в переменные времени ядра
Summary(sk.UTF-8):	Pomôcka pre úpravu premenných hodín jadra
Summary(sl.UTF-8):	Pripomoček za prikrojitev časovnih spremenljivk jedra
Summary(sv.UTF-8):	Ett verktyg för att justera kärnans tidsvariabler
Summary(uk.UTF-8):	Утиліта для внесення поправок в змінні часу ядра
Summary(zh_CN.UTF-8):	用于调整内核时间变量的实用程序。
Name:		adjtimex
Version:	1.21
Release:	1
License:	GPL v2+
Group:		Base
Source0:	ftp://sunsite.unc.edu/pub/Linux/system/admin/time/%{name}-%{version}.tar.gz
# Source0-md5:	9888b54f418d7cc120fd3a4222f01c9c
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

%description -l cs.UTF-8
Adjtimex poskytuje syrový přístup k časovým proměnným jádra. Na
počítači, který není zasíťovaný nebo se připojuje k Internetu pouze
občas, může root používat adjtimex pro korekci trvalého driftu hodin
(tj. pokud se systémové hodiny za běhu operačního systému zpomalují
nebo zrychlují proti přesnému času). Jestliže je váš počítač připojen
do Internetu nebo je vybaven přesným oscilátorem nebo rádiem řízenými
hodinami, měli byste místo adjtimexu nastavovat systémové hodiny
programem xntpd. Uživatelé mohou používat program adjtimex pro čtení
časových proměnných jádra.

%description -l da.UTF-8
Adjtimex giver direkte adgang til kernens tidvariabler. På fritstående
eller midlertidige tilkoblede maskiner, kan root bruge adjtimex til at
korrigere systemets tidsafvigelse. Hvis din maskine er tilkoblet
Internet eller er udstyret med en precisionsoscillator eller
radioklokke, bør du hellere bruge xntpd programmet til at styre
klokken. Brugere kan bruge adjtimex til at vise kernens tidsvariabler.

%description -l de.UTF-8
Adjtimex ermöglicht den direkten Zugriff auf die Zeitvariablen des
Kernels. Bei nicht vernetzten oder nur zeitweise mit dem Netz
verbundenen Computern kann Root mit Hilfe von adjtimex die
systematische Zeitabweichung korrigieren. Wenn Ihr Rechner mit dem
Internet verbunden oder mit einem Präzisionsoszillator oder einer
Funkuhr ausgerüstet ist, sollten Sie die Systemuhr stattdessen mit dem
Programm xntpd einstellen. Die Benutzer können mit adjtimex die
Zeitvariablen des Kernels anzeigen.

%description -l es.UTF-8
Adjtimex proporciona un acceso de bajo nivel a las variables de tiempo
del kernel. En máquinas independientes o en máquinas conectadas a
intervalos, el usuario raíz puede utilizar adjtimex para corregir el
margen de error del reloj. Si el ordenador está conectado a Internet o
está dotado de un oscilador de precisión o un reloj radio, debería
poder usar el programa xntpd para corregir la hora. Los usuarios
pueden usar adjtimex para ver las variables de tiempo del kernel.

%description -l fr.UTF-8
Adjtimex offre un accès direct à l'horloge du noyau. Sur les
ordinateurs autonomes ou connectés de façon intermittente, un
utilisateur connecté en tant que root peut utiliser adjtimex pour
corriger la dérive systématique. Si votre ordinateur est connecté à
Internet ou équipé d'un oscillateur de précision ou d'une horloge
radio, gérez plutôt l'horloge système avec le programme xntpd. Les
utilisateurs peuvent utiliser adjtimex pour voir les variables de
temps du noyau.

%description -l id.UTF-8
Adjtimex menyediakan raw access terhadap variable time pada kernel.
Pada computer yang standalone atau tidak selalu tersambung pada
jaringan, root dapat menggunakan adjtimex untuk melakukan koreksi bagi
systematic drift. Bila mesin anda tersambung dengan Internet atau
dilengkapi dengan precision oscillator atau radio clock, sebaiknya
anda melakukan hal ini menggunakan program xntpd. Pengguna menggunakan
adjtimex untuk melihat variable time pada kernel.

%description -l is.UTF-8
Adjtimex gefur hráan aðgang að tímabreytum kjarna. A netlausum eða
við-og-við tengdum vélum getur rót notað adjtimex til þess að
leiðrétta rek á klukku. Ef vélin þín er tengd við internetið eða er
með nákvæmt tímamælingartæki ættir þú frekar að breyta kerfisklukkunni
með xntpd forritinu. Notendur geta notað adjtimex til þess að sjá
tímabreytur kjarna.

%description -l it.UTF-8
Adjtimex fornisce un accesso di basso livello alle variabili temporali
del kernel. Su elaboratori indipendenti o connessi in
modointermittente, il root può utilizzare adjtimex per correggere la
deriva sistematica dell'orologio. Se l'elaboratore è connesso a
Internet o dotato di oscillatore di precisione o orologio radio si
consiglia di utilizzare il programma xntpd per gestire l'orologio di
sistema. Gli utenti possono utilizzare adjtimex per visualizzare le
variabili temporali del kernel.

%description -l ja.UTF-8
adjtimex は、カーネルの時間変数への直接アクセスを提供します。
スタンドアローンまたは相互接続されたマシン上で、root ユーザーは
adjtimex
を使用してシステムの時間誤差を修正できます。ご使用のマシンがインターネット
に接続されている場合、または精度発振器やラジオ
クロックが装備されている場合、代わりに xntpd プログラムを
使用してシステムクロックを管理する必要があります。ユーザーは、
adjtimex を使用して、カーネルの時間変数を参照できます。

%description -l nb.UTF-8
Adjtimex gir direkte tilgang til kjernens tidvariabler. På
frittstående eller midlertidige tilkoblede maskiner, kan root bruke
adjtimex til å korrigere systemets tidsavvik. Hvis din maskin er
tilkoblet Internett eller er utstyrt med en presisjonsoscillator eller
radioklokke, bør du heller bruke xntpd programmet til å styre klokken.
Brukere kan bruke adjtimex til å vise kjernens tidsvariabler.

%description -l pl.UTF-8
Adjtimex umożliwia niskopoziomowy dostęp do zmiennych czasu
systemowego. W systemach wolnostojących lub podłączonych do Internetu
w sposób nieciągły, program ten może zostać wykorzystany przez roota
do korekcji dryfu zegara systemowego. Jeśli maszyna jest podłączona do
Internetu lub wyposażona w precyzyjny generator częstotliwości lub
zegar radiowy, lepiej do korekcji czasu systemowego używać zamiast
niego programu xntpd. Zwykli użytkownicy mogą za pomocą adjtimex
podglądać zmienne czasu.

%description -l pt.UTF-8
O adjtimex fornece o acesso em bruto às variáveis temporais do núcleo.
Em sistemas autónomos ou em máquinas ligadas intermitentemente, o
'root' pode usar o 'adjtimex' para corrigir desvios sistemáticos. Se a
máquina do utilizador está ligada à Internet ou está equipada com um
oscilador de precisão ou um relógio-rádio, então deve-se ajustar o
relógio do sistema com o programa xntpd. Os utilizadores podem usar o
adjtimex para verificar as variáveis temporais do núcleo.

%description -l ru.UTF-8
Adjtimex обеспечивает прямой доступ к переменным времени системы. На
компьютерах, не подключенных или периодически подключаемых к сети,
администратор может использовать adjtimex для корректировки
систематических отклонений во времени. Если ваша машина имеет доступ к
Internet или оборудована точным гетеродином или радиочасами, то вам
лучше управлять системными часами с помоью программы xntpd. Вы можете
использовать adjtimex для просмотра переменных времени системы.

%description -l sk.UTF-8
Adjtimex poskytuje nízkoúrovňový prístup k časovým premenným jadra. Na
samostatných alebo len prechodne pripojených počítačoch môže
superpoužívateľ korigovať systematický posun hodín systému. Pokiaľ je
váľ počítač pripojený k Internetu alebo je vybavený presným
oscilátorom alebo rádiovými hodinami, mali by ste spravovať systémové
hodiny programom xntpd. Obyčajní používatelia môžu adjtimex-om
prezerať nastavenie príslušných premenných jadra.

%description -l sv.UTF-8
Adjtimex erbjuder rå tillgång till kärnans tidsvariabler. På
fristående eller intermittent uppkopplade maskiner, kan root använda
adjtimex för att korrigera för systematisk drift. Om din maskin är
uppkopplad till Internet eller utrustad med en precisionsoscillator
eller radioklocka skall du istället styra systemklockan med
xntpd-programmet. Användare kan använda adjtimex för att se kärnans
tidsvariabler.

%description -l uk.UTF-8
Adjtimex дозволяє маніпулювати з командного рядка змінними ядра, які
відповідають за корекцію ходу системного годинника. Завдяки цьому є
можливість корегувати системний годинник без використання ntpd, котрий
вимагає наявності постійного зв'язку з еталонним годинником.

Підтримується порівняння вашого системного годинника з еталонним
джерелом часу, включаючи RTC вашого комп'ютера.

%description -l zh_CN.UTF-8
Adjtimex
提供了对原始内核时间变量的存取功能。在独立或间歇式连接的计算机上，
根可以使用 adjtimex 校正系统偏差。如果您的计算机已连接至 Internet，
或者配备了精密振荡器或无线电时钟，则应该使用 xntpd 程序管理系统时钟。
用户可以使用 adjtimex 查看内核时间变量。

%prep
%setup -q

%build
%{__autoconf}
%configure
%{__make} \
	CC="%{__cc}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{_mandir}/man8}

install adjtimex $RPM_BUILD_ROOT%{_sbindir}
install adjtimex.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYRIGHT ChangeLog README
%lang(ru) %doc README.ru
%attr(755,root,root) %{_sbindir}/*
%{_mandir}/man8/*
