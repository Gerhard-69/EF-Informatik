"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[445],{3905:(e,n,t)=>{t.d(n,{Zo:()=>u,kt:()=>c});var r=t(7294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function s(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function a(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?s(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):s(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function d(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},s=Object.keys(e);for(r=0;r<s.length;r++)t=s[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var s=Object.getOwnPropertySymbols(e);for(r=0;r<s.length;r++)t=s[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var l=r.createContext({}),o=function(e){var n=r.useContext(l),t=n;return e&&(t="function"==typeof e?e(n):a(a({},n),e)),t},u=function(e){var n=o(e.components);return r.createElement(l.Provider,{value:n},e.children)},m={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},k=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,s=e.originalType,l=e.parentName,u=d(e,["components","mdxType","originalType","parentName"]),k=o(t),c=i,h=k["".concat(l,".").concat(c)]||k[c]||m[c]||s;return t?r.createElement(h,a(a({ref:n},u),{},{components:t})):r.createElement(h,a({ref:n},u))}));function c(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var s=t.length,a=new Array(s);a[0]=k;var d={};for(var l in n)hasOwnProperty.call(n,l)&&(d[l]=n[l]);d.originalType=e,d.mdxType="string"==typeof e?e:i,a[1]=d;for(var o=2;o<s;o++)a[o]=t[o];return r.createElement.apply(null,a)}return r.createElement.apply(null,t)}k.displayName="MDXCreateElement"},422:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>l,contentTitle:()=>a,default:()=>m,frontMatter:()=>s,metadata:()=>d,toc:()=>o});var r=t(7462),i=(t(7294),t(3905));const s={},a="3. Vom Lan zum Internet",d={unversionedId:"Netzwerke/webserver/Netzwerke 3-8",id:"Netzwerke/webserver/Netzwerke 3-8",title:"3. Vom Lan zum Internet",description:"Host",source:"@site/docs/Netzwerke/webserver/Netzwerke 3-8.md",sourceDirName:"Netzwerke/webserver",slug:"/Netzwerke/webserver/Netzwerke 3-8",permalink:"/EF-Informatik/docs/Netzwerke/webserver/Netzwerke 3-8",draft:!1,editUrl:"https://github.com/Gerhard-69/EF-Informatik/tree/main/docs/Netzwerke/webserver/Netzwerke 3-8.md",tags:[],version:"current",frontMatter:{},sidebar:"tutorialSidebar",previous:{title:"Knobelw\xfcrfel",permalink:"/EF-Informatik/docs/IOT_Day/knobelwuerfel"},next:{title:"Cheatsheet API's",permalink:"/EF-Informatik/docs/Netzwerke/webserver/apis"}},l={},o=[{value:"Host",id:"host",level:2},{value:"IP-Adressen",id:"ip-adressen",level:2},{value:"Network",id:"network",level:2},{value:"Repeaters",id:"repeaters",level:2},{value:"Hub",id:"hub",level:2},{value:"Bridge",id:"bridge",level:2},{value:"Switch",id:"switch",level:2},{value:"Router",id:"router",level:2},{value:"Bonus",id:"bonus",level:2},{value:"Netzwerkteil und Hostteil",id:"netzwerkteil-und-hostteil",level:2},{value:"Netzmaske",id:"netzmaske",level:2},{value:"Suffixnotation f\xfcr Netzmaske",id:"suffixnotation-f\xfcr-netzmaske",level:2},{value:"Broadcastadresse",id:"broadcastadresse",level:2},{value:"Spezielle IP-Adressen",id:"spezielle-ip-adressen",level:2},{value:"Mac-Adressen",id:"mac-adressen",level:2},{value:"Gateway",id:"gateway",level:2},{value:"ARP",id:"arp",level:2},{value:"MAC-Tabelle",id:"mac-tabelle",level:2},{value:"Ethernet-Frame",id:"ethernet-frame",level:2},{value:"Routing-Tabelle",id:"routing-tabelle",level:2}],u={toc:o};function m(e){let{components:n,...s}=e;return(0,i.kt)("wrapper",(0,r.Z)({},u,s,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"3-vom-lan-zum-internet"},"3. Vom Lan zum Internet"),(0,i.kt)("h2",{id:"host"},"Host"),(0,i.kt)("p",null,"Host sind alle Ger\xe4te die Daten senden oder erhalten. Host ist in Client und Server aufgeteilt der Client schickt eine Anfrage an den Server. Ein Server kann aber auch als Client fungieren wenn er z.B ein Server Update macht. Dabei ist ein Server auch einfach nur ein Computer. "),(0,i.kt)("h2",{id:"ip-adressen"},"IP-Adressen"),(0,i.kt)("p",null,"Die IP-Adresse ist die Identit\xe4t f\xfcr jeden Host. Jede IP Adresse besteht aus 32 bits also aus 32 Nullen oder Einsen. Diese werden wiederum in Vier Teile geteilt also 8 bit gleich eine Zahl und Vier Zahlen gleich eine IP Adresse. Die gr\xf6sste zahl ist 255 also 2^8-1 und die kleinste 0. Man kann mithilfe der IP-Adressen die Host zuordnen bzw. identifizieren. "),(0,i.kt)("h2",{id:"network"},"Network"),(0,i.kt)("p",null,"Ein Network entsteht wenn mindestens zwei Hosts miteinander Verbunden sind. Das Network transpotiert die Daten von Host zu Host. Es k\xf6nnen in einem Network andere Netzwerke bestehen die dann Subnets genannt werden. Jedes Network ist mit dem Internet (Interconnected Networks) verbunden."),(0,i.kt)("h2",{id:"repeaters"},"Repeaters"),(0,i.kt)("p",null,"Ein Signal zwischen zwei Host kommt nicht an wenn diese zuweit auseinander sind, um dass zu verhindern gibt es Repeater die dazu da sind um das Signal zu erneuern."),(0,i.kt)("h2",{id:"hub"},"Hub"),(0,i.kt)("p",null,"Ein Hub ist ein multi-port Repeater. Er erm\xf6glicht es ein Signal, dass in den Hub reingeht wie ein Repeater zu erneuern gleichzeitig zu vermehrfachen und an alle anderen Hosts die mit dem Hub verbunden sind zu schicken."),(0,i.kt)("h2",{id:"bridge"},"Bridge"),(0,i.kt)("p",null,"Eine Bridge verbindet zwei Hosts. Sie lernen welche Hosts auf welcher Seite sind und k\xf6nnen ein Signal auch nicht weiterleiten wenn sie wissen, dass das Signal nicht durch soll.   "),(0,i.kt)("h2",{id:"switch"},"Switch"),(0,i.kt)("p",null,"Ein Switch ist eine Kombination von einem Hub und einem Bridge.WDie die Bridge lernen sie welcher Host auf welchem Port ist und k\xf6nnen so das Signal nur an den gew\xfcnschten Host weiterleiten, so ist man das Problem der Hubs los. Hosts in einem Network teilen die gleiche IP Adresse z.B 192.168.1.x ist bestimmt in dem Fall dann den Host."),(0,i.kt)("h2",{id:"router"},"Router"),(0,i.kt)("p",null,"Ein Router erm\xf6glicht Kommunikation zwischen Netzwerken. Er ist mit dem Internet Verbunden. Er kann Daten \xfcberpr\xfcfen, filtern und umleiten. Router lernen mit welchen Netzwerken sie verbunden sind. Sie haben in jedem Network in dem sie sind eine IP-Adresse die in dem Network als Gateway dient. Das Internet besteht aus ganz vielen Routern wenn eine Datei von New York nach Tokio m\xf6chte dann muss sie durch Router im Internet."),(0,i.kt)("h2",{id:"bonus"},"Bonus"),(0,i.kt)("p",null,"Routing is the process of moving data between networks",(0,i.kt)("br",{parentName:"p"}),"\n","a Router is routing "),(0,i.kt)("p",null,"Switching is the process of moving data within networks",(0,i.kt)("br",{parentName:"p"}),"\n","a Switch is switching"),(0,i.kt)("p",null,"There are many other Network Devices and all of them perform switching and/or routing."),(0,i.kt)("h1",{id:"4-ip-adressen"},"4. IP-Adressen"),(0,i.kt)("h2",{id:"netzwerkteil-und-hostteil"},"Netzwerkteil und Hostteil"),(0,i.kt)("p",null,"IP-Adressen bestehen aus zwei Teilen.",(0,i.kt)("br",{parentName:"p"}),"\n","Vorderer Teil ist der Netzwerkteil und der hintere Teil ist der Hostteil."),(0,i.kt)("h2",{id:"netzmaske"},"Netzmaske"),(0,i.kt)("p",null,"Merksatz: Links von dieser Stelle hat es in der Netzmaske ausschliesslich 1, rechts davon hat es nur 0"),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"Netzmaske:  255.255.254.0\nIP-Adresse: 13.162.25.4\n\nBin\xe4r:\nNetzmaske:    1111 1111.1111 1111.1111 1110.0000 0000\nIP-Adresse:   0000 1101.1010 0010.0001 1001.0000 0100\n#             vvvv vvvv vvvv vvvv vvvv vvv\nNetzwerkteil: 0000 1101.1010 0010.0001 100\n#                                         v vvvv vvvv\nHostteil:                                 1.0000 0100\n")),(0,i.kt)("p",null,"Erg\xe4nzt man den Netzwerkteil mit lauter 0 zu einer vollen 32 Bit langen IP-Adresse, so erh\xe4lt man die Netzwerkadresse."),(0,i.kt)("pre",null,(0,i.kt)("code",{parentName:"pre"},"Netzwerkteil:                  0000'1101.1010'0010.0001'100\nerg\xe4nzte Nullen:                                           0.0000.0000\nresultierende Netzwerkadresse: 0000'1101.1010'0010.0001'1000.0000.0000 = 13.162.24.0\n")),(0,i.kt)("h2",{id:"suffixnotation-f\xfcr-netzmaske"},"Suffixnotation f\xfcr Netzmaske"),(0,i.kt)("p",null,"Um die Netzmaske zu erkennen muss man wissen wieviele einser sie hat. Die Anzahl der einsen kann man als Suffix bei einer IP-Adresse anh\xe4ngen."),(0,i.kt)("h2",{id:"broadcastadresse"},"Broadcastadresse"),(0,i.kt)("p",null,"Broadcastadressen werden ben\xf6tigt um ein IP-Paket an alle Ger\xe4te in einem Netzwerk zu schicken. Sie darf nicht als Adresse f\xfcr ein Ger\xe4t verwendet werden."),(0,i.kt)("h2",{id:"spezielle-ip-adressen"},"Spezielle IP-Adressen"),(0,i.kt)("p",null,(0,i.kt)("strong",{parentName:"p"},"127.0.0.1")," diese Adresse wird ben\xf6tigt wenn ein Ger\xe4t sich ein IP-Paket an sich selber senden will.",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("strong",{parentName:"p"},"0.0.0.0"),' diese Adresse steht nach Ger\xe4t f\xfcr etwas anderes. "Ich habe noch keine IP-Adresse", "eine beliebige IP-Adresse" oder "aktuelles Netzwerk".'),(0,i.kt)("h1",{id:"5-8"},"5-8"),(0,i.kt)("h2",{id:"mac-adressen"},"Mac-Adressen"),(0,i.kt)("p",null,"Um Einsen und Nullen von einem Ger\xe4t zu einem anderen zu Transpotieren werden MAC-Adressen ben\xf6tigt. Sie bestehen aus 48 bits die in 12 hex stellen dargestellt werden. 94-65-9C-3B-8A-E5 w\xe4re z.B eine. Jeder NIC hat eine eigene MAC-Adresse."),(0,i.kt)("h2",{id:"gateway"},"Gateway"),(0,i.kt)("p",null,"ein Gateway ist die IP-Adresse von dem Router mit dem ein Ger\xe4t verbunden ist."),(0,i.kt)("h2",{id:"arp"},"ARP"),(0,i.kt)("p",null,"ARP steht f\xfcr Address Resolution Protocol und wird von hosts verwendet um die MAC Adresse von einem anderen host herrauszufinden. Das funktioniert in dem der host einen ARP request an alle hosts im Netzwerk sendet in der nach der IP-Adresse gefragt wird und die MAC-Adresse angefordet. Damit der host die MAC-Adresse zur\xfcckschicken kann sind im request die IP und MAC-Adresse angeh\xe4ngt. Wenn der host mit einem Router verbunden ist dann kann er den Router als Ziel angeben."),(0,i.kt)("h2",{id:"mac-tabelle"},"MAC-Tabelle"),(0,i.kt)("p",null,"Ein Switch erstellt eine MAC-Tabelle in der er sieht bei welchem Ausgang welche MAC-Adresse ist. Er lernt das in dem er nach einer erhaltenen Datei sich die Source MAC-Adresse merkt, mit der Zeit weiss er welche MAC-Adresse mit welchem Ausgang verbunden ist.\nBis er das weiss schickt er die Datei an alle host von denen er die MAC-Adresse nicht weiss."),(0,i.kt)("h2",{id:"ethernet-frame"},"Ethernet-Frame"),(0,i.kt)("p",null,(0,i.kt)("img",{src:t(8833).Z,width:"1332",height:"556"}),"\nSo sieht ein Ethernet-Frame aus der den Austausch von in einem Lan verbundenen Ger\xe4ten darstellt. Die Bereiche haben folgende bedeutungen:",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("strong",{parentName:"p"},"Pr\xe4ambel und Start Frame Delimitter (SFD)"),(0,i.kt)("br",{parentName:"p"}),"\n","Enth\xe4lt keine Information, sondern nur abwechselnde auf 0 und 1 gesetzte Bits. Dadurch k\xf6nnen sich die Empf\xe4nger auf die \xdcbertragungsgeschwindigkeit des Senders einstellen.",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("strong",{parentName:"p"},"Ziel-MAC-Adresse"),(0,i.kt)("br",{parentName:"p"}),"\n","Die lokale Adresse des Ger\xe4tes, an welches der Frame gerichtet ist.",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("strong",{parentName:"p"},"Quell-MAC-Adresse"),(0,i.kt)("br",{parentName:"p"}),"\n","Die lokale Adresse des Ger\xe4tes, von welchem der Frame gesendet worden ist.",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("strong",{parentName:"p"},"Ether-Type"),(0,i.kt)("br",{parentName:"p"}),"\n","Gibt an welches Protokoll in den Nutzdaten verwendet wird (also zum Beispiel IP).",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("strong",{parentName:"p"},"Nutzdaten"),(0,i.kt)("br",{parentName:"p"}),"\n","Die eigentliche Nachricht. Im Falle des TCP/IP-Protokollstapels ein IP-Paket.",(0,i.kt)("br",{parentName:"p"}),"\n",(0,i.kt)("strong",{parentName:"p"},"Frame Pr\xfcfsumme (Frame Check Sequence, FCS)"),(0,i.kt)("br",{parentName:"p"}),"\n","Wird vom Sender berechnet und erlaubt dem Empf\xe4nger zu \xfcberpr\xfcfen, ob der Frame korrekt \xfcbertragen und empfangen worden ist."),(0,i.kt)("h2",{id:"routing-tabelle"},"Routing-Tabelle"),(0,i.kt)("p",null,"Sie beschreibt eine Route wie ein Paket weitergeleitet werden kann und muss deswegen folgende Information enthalten. Das Routenziel, wenn das Ziel nicht im Netzwerk ist dann die IP-Adresse des Gateways und die Identifikation des Netzwerkadapters. Durch eine Metrik wird die beste Route entschieden. Die Route kann mehrere Ziele haben. Eine Host-Adresse, eine Netzwerk-Adresse oder die Standartroute. Um die Host- und Netzwerk-Adresse unterscheiden zu k\xf6nnen wird die Netzmaske ben\xf6tigt."))}m.isMDXComponent=!0},8833:(e,n,t)=>{t.d(n,{Z:()=>r});const r=t.p+"assets/images/ethernetframe-92802e257fbfc7c63146d67966016a99.png"}}]);