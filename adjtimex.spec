Summary:	A utility for adjusting kernel time variables
Summary(cs):	Program pro nastavov�n� �asov�ch prom�nn�ch j�dra
Summary(da):	Et v�rkt�j til at justere kernetidsvariabler
Summary(de):	Ein Dienstprogramm f�r die Einstellung der Kernel-Zeitvariablen
Summary(es):	Utilidad para modificar las variables de tiempo del kernel
Summary(fr):	Utilitaire pour le r�glage de l'horloge du noyau
Summary(id):	Utility untuk menyamakan variabel time kernel
Summary(is):	T�l til a� stilla t�mabreytur � kjarna
Summary(it):	Utility per modificare le variabili temporali del kernel
Summary(ja):	�����ͥ�λ����ѿ���Ĵ�����뤿��Υ桼�ƥ���ƥ�
Summary(no):	Et verkt�y for � justere kjernens tidsvariabler
Summary(pl):	Narz�dzie do regulacji zmiennych czasu kernela
Summary(pt):	Um utilit�rio para ajustar as vari�veis de tempo do n�cleo
Summary(ru):	������� ��� �������� �������� � ���������� ������� ����
Summary(sk):	Pom�cka pre �pravu premenn�ch hod�n jadra
Summary(sl):	Pripomo�ek za prikrojitev �asovnih spremenljivk jedra
Summary(sv):	Ett verktyg f�r att justera k�rnans tidsvariabler
Summary(uk):	���̦�� ��� �������� �������� � �ͦ�Φ ���� ����
Summary(zh_CN):	���ڵ����ں�ʱ�������ʵ�ó���
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
Adjtimex poskytuje syrov� p��stup k �asov�m prom�nn�m j�dra. Na
po��ta�i, kter� nen� zas�ovan� nebo se p�ipojuje k Internetu pouze
ob�as, m��e root pou��vat adjtimex pro korekci trval�ho driftu hodin
(tj. pokud se syst�mov� hodiny za b�hu opera�n�ho syst�mu zpomaluj�
nebo zrychluj� proti p�esn�mu �asu). Jestli�e je v� po��ta� p�ipojen
do Internetu nebo je vybaven p�esn�m oscil�torem nebo r�diem ��zen�mi
hodinami, m�li byste m�sto adjtimexu nastavovat syst�mov� hodiny
programem xntpd. U�ivatel� mohou pou��vat program adjtimex pro �ten�
�asov�ch prom�nn�ch j�dra.

%description -l da
Adjtimex giver direkte adgang til kernens tidvariabler. P� fritst�ende
eller midlertidige tilkoblede maskiner, kan root bruge adjtimex til at
korrigere systemets tidsafvigelse. Hvis din maskine er tilkoblet
Internet eller er udstyret med en precisionsoscillator eller
radioklokke, b�r du hellere bruge xntpd programmet til at styre
klokken. Brugere kan bruge adjtimex til at vise kernens tidsvariabler.

%description -l de
Adjtimex erm�glicht den direkten Zugriff auf die Zeitvariablen des
Kernels. Bei nicht vernetzten oder nur zeitweise mit dem Netz
verbundenen Computern kann Root mit Hilfe von adjtimex die
systematische Zeitabweichung korrigieren. Wenn Ihr Rechner mit dem
Internet verbunden oder mit einem Pr�zisionsoszillator oder einer
Funkuhr ausger�stet ist, sollten Sie die Systemuhr stattdessen mit dem
Programm xntpd einstellen. Die Benutzer k�nnen mit adjtimex die
Zeitvariablen des Kernels anzeigen.

%description -l es
Adjtimex proporciona un acceso de bajo nivel a las variables de tiempo
del kernel. En m�quinas independientes o en m�quinas conectadas a
intervalos, el usuario ra�z puede utilizar adjtimex para corregir el
margen de error del reloj. Si el ordenador est� conectado a Internet o
est� dotado de un oscilador de precisi�n o un reloj radio, deber�a
poder usar el programa xntpd para corregir la hora. Los usuarios
pueden usar adjtimex para ver las variables de tiempo del kernel.

%description -l fr
Adjtimex offre un acc�s direct � l'horloge du noyau. Sur les
ordinateurs autonomes ou connect�s de fa�on intermittente, un
utilisateur connect� en tant que root peut utiliser adjtimex pour
corriger la d�rive syst�matique. Si votre ordinateur est connect� �
Internet ou �quip� d'un oscillateur de pr�cision ou d'une horloge
radio, g�rez plut�t l'horloge syst�me avec le programme xntpd. Les
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
Adjtimex gefur hr�an a�gang a� t�mabreytum kjarna. A netlausum e�a
vi�-og-vi� tengdum v�lum getur r�t nota� adjtimex til �ess a�
lei�r�tta rek � klukku. Ef v�lin ��n er tengd vi� interneti� e�a er
me� n�kv�mt t�mam�lingart�ki �ttir �� frekar a� breyta kerfisklukkunni
me� xntpd forritinu. Notendur geta nota� adjtimex til �ess a� sj�
t�mabreytur kjarna.

%description -l it
Adjtimex fornisce un accesso di basso livello alle variabili temporali
del kernel. Su elaboratori indipendenti o connessi in
modointermittente, il root pu� utilizzare adjtimex per correggere la
deriva sistematica dell'orologio. Se l'elaboratore � connesso a
Internet o dotato di oscillatore di precisione o orologio radio si
consiglia di utilizzare il programma xntpd per gestire l'orologio di
sistema. Gli utenti possono utilizzare adjtimex per visualizzare le
variabili temporali del kernel.

%description -l ja
adjtimex �ϡ������ͥ�λ����ѿ��ؤ�ľ�ܥ����������󶡤��ޤ���
������ɥ�����ޤ��������³���줿�ޥ����ǡ�root �桼������
adjtimex
����Ѥ��ƥ����ƥ�λ��ָ������Ǥ��ޤ��������ѤΥޥ��󤬥��󥿡��ͥå�
����³����Ƥ����硢�ޤ�������ȯ�����饸��
����å�����������Ƥ����硢����� xntpd �ץ�����
���Ѥ��ƥ����ƥ९��å����������ɬ�פ�����ޤ����桼�����ϡ�
adjtimex ����Ѥ��ơ������ͥ�λ����ѿ��򻲾ȤǤ��ޤ���

%description -l no
Adjtimex gir direkte tilgang til kjernens tidvariabler. P�
frittst�ende eller midlertidige tilkoblede maskiner, kan root bruke
adjtimex til � korrigere systemets tidsavvik. Hvis din maskin er
tilkoblet Internett eller er utstyrt med en presisjonsoscillator eller
radioklokke, b�r du heller bruke xntpd programmet til � styre klokken.
Brukere kan bruke adjtimex til � vise kjernens tidsvariabler.

%description -l pl
Adjtimex umo�liwia niskopoziomowy dost�p do zmiennych czasu
systemowego. W systemach wolnostoj�cych lub pod��czonych do Internetu
w spos�b nieci�g�y, program ten mo�e zosta� wykorzystany przez roota
do korekcji dryfu zegara systemowego. Je�li maszyna jest pod��czona do
Internetu lub wyposa�ona w precyzyjny generator cz�stotliwo�ci lub
zegar radiowy, lepiej do korekcji czasu systemowego u�ywa� zamiast
niego programu xntpd. Zwykli u�ytkownicy mog� za pomoc� adjtimex
podgl�da� zmienne czasu.

%description -l pt
O adjtimex fornece o acesso em bruto �s vari�veis temporais do n�cleo.
Em sistemas aut�nomos ou em m�quinas ligadas intermitentemente, o
'root' pode usar o 'adjtimex' para corrigir desvios sistem�ticos. Se a
m�quina do utilizador est� ligada � Internet ou est� equipada com um
oscilador de precis�o ou um rel�gio-r�dio, ent�o deve-se ajustar o
rel�gio do sistema com o programa xntpd. Os utilizadores podem usar o
adjtimex para verificar as vari�veis temporais do n�cleo.

%description -l ru
Adjtimex ������������ ������ ������ � ���������� ������� �������. ��
�����������, �� ������������ ��� ������������ ������������ � ����,
������������� ����� ������������ adjtimex ��� �������������
��������������� ���������� �� �������. ���� ���� ������ ����� ������ �
Internet ��� ����������� ������ ����������� ��� �����������, �� ���
����� ��������� ���������� ������ � ������ ��������� xntpd. �� ������
������������ adjtimex ��� ��������� ���������� ������� �������.

%description -l sk
Adjtimex poskytuje n�zko�rov�ov� pr�stup k �asov�m premenn�m jadra. Na
samostatn�ch alebo len prechodne pripojen�ch po��ta�och m��e
superpou��vate� korigova� systematick� posun hod�n syst�mu. Pokia� je
v� po��ta� pripojen� k Internetu alebo je vybaven� presn�m
oscil�torom alebo r�diov�mi hodinami, mali by ste spravova� syst�mov�
hodiny programom xntpd. Oby�ajn� pou��vatelia m��u adjtimex-om
prezera� nastavenie pr�slu�n�ch premenn�ch jadra.

%description -l sv
Adjtimex erbjuder r� tillg�ng till k�rnans tidsvariabler. P�
frist�ende eller intermittent uppkopplade maskiner, kan root anv�nda
adjtimex f�r att korrigera f�r systematisk drift. Om din maskin �r
uppkopplad till Internet eller utrustad med en precisionsoscillator
eller radioklocka skall du ist�llet styra systemklockan med
xntpd-programmet. Anv�ndare kan anv�nda adjtimex f�r att se k�rnans
tidsvariabler.

%description -l uk
Adjtimex ������Ѥ ��Φ�������� � ���������� ����� �ͦ����� ����, �˦
צ���צ����� �� �����æ� ���� ���������� ���������. ������� ����� �
�����צ��� ���������� ��������� �������� ��� ������������ ntpd, ������
������� �������Ԧ ���Ԧ����� ��'���� � ��������� ����������.

������դ���� ��Ҧ������ ������ ���������� ��������� � ���������
�������� ����, ��������� RTC ������ ����'�����.

%description -l zh_CN
Adjtimex
�ṩ�˶�ԭʼ�ں�ʱ������Ĵ�ȡ���ܡ��ڶ������Ъʽ���ӵļ�����ϣ�
������ʹ�� adjtimex У��ϵͳƫ�������ļ������������ Internet��
�����䱸�˾������������ߵ�ʱ�ӣ���Ӧ��ʹ�� xntpd �������ϵͳʱ�ӡ�
�û�����ʹ�� adjtimex �鿴�ں�ʱ�������

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
