"use strict";(self.webpackChunkef_website_template=self.webpackChunkef_website_template||[]).push([[837],{3905:(e,n,t)=>{t.d(n,{Zo:()=>d,kt:()=>m});var r=t(7294);function i(e,n,t){return n in e?Object.defineProperty(e,n,{value:t,enumerable:!0,configurable:!0,writable:!0}):e[n]=t,e}function a(e,n){var t=Object.keys(e);if(Object.getOwnPropertySymbols){var r=Object.getOwnPropertySymbols(e);n&&(r=r.filter((function(n){return Object.getOwnPropertyDescriptor(e,n).enumerable}))),t.push.apply(t,r)}return t}function l(e){for(var n=1;n<arguments.length;n++){var t=null!=arguments[n]?arguments[n]:{};n%2?a(Object(t),!0).forEach((function(n){i(e,n,t[n])})):Object.getOwnPropertyDescriptors?Object.defineProperties(e,Object.getOwnPropertyDescriptors(t)):a(Object(t)).forEach((function(n){Object.defineProperty(e,n,Object.getOwnPropertyDescriptor(t,n))}))}return e}function s(e,n){if(null==e)return{};var t,r,i=function(e,n){if(null==e)return{};var t,r,i={},a=Object.keys(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||(i[t]=e[t]);return i}(e,n);if(Object.getOwnPropertySymbols){var a=Object.getOwnPropertySymbols(e);for(r=0;r<a.length;r++)t=a[r],n.indexOf(t)>=0||Object.prototype.propertyIsEnumerable.call(e,t)&&(i[t]=e[t])}return i}var o=r.createContext({}),u=function(e){var n=r.useContext(o),t=n;return e&&(t="function"==typeof e?e(n):l(l({},n),e)),t},d=function(e){var n=u(e.components);return r.createElement(o.Provider,{value:n},e.children)},p={inlineCode:"code",wrapper:function(e){var n=e.children;return r.createElement(r.Fragment,{},n)}},c=r.forwardRef((function(e,n){var t=e.components,i=e.mdxType,a=e.originalType,o=e.parentName,d=s(e,["components","mdxType","originalType","parentName"]),c=u(t),m=i,f=c["".concat(o,".").concat(m)]||c[m]||p[m]||a;return t?r.createElement(f,l(l({ref:n},d),{},{components:t})):r.createElement(f,l({ref:n},d))}));function m(e,n){var t=arguments,i=n&&n.mdxType;if("string"==typeof e||i){var a=t.length,l=new Array(a);l[0]=c;var s={};for(var o in n)hasOwnProperty.call(n,o)&&(s[o]=n[o]);s.originalType=e,s.mdxType="string"==typeof e?e:i,l[1]=s;for(var u=2;u<a;u++)l[u]=t[u];return r.createElement.apply(null,l)}return r.createElement.apply(null,t)}c.displayName="MDXCreateElement"},557:(e,n,t)=>{t.r(n),t.d(n,{assets:()=>o,contentTitle:()=>l,default:()=>p,frontMatter:()=>a,metadata:()=>s,toc:()=>u});var r=t(7462),i=(t(7294),t(3905));const a={},l="**Numtrip Blog**",s={permalink:"/EF-Informatik/Numtrip",editUrl:"https://github.com/Gerhard-69/EF-Informatik/tree/main/blog/Numtrip.md",source:"@site/blog/Numtrip.md",title:"**Numtrip Blog**",description:"Numtrip ist ein Denkspiel das \xe4hnlichkeiten dem sehr popul\xe4ren Spiel 2048 hat. Das Feld besteht auf gleich viel Reihen und Zeilen. Die Felder sind gef\xfcllt zuf\xe4lligen geraden Zahlen. Man kann ein Feld ausw\xe4hlen, wenn ein anligendes Feld mit der selben Zahl gef\xfcllt werden diese und die mit diesem Feld anliegende Verbunden. Das ausgew\xe4hlte feld wird verdoppelt. Das ganze geht so bis man 1024 erreicht hat.",date:"2023-01-27T14:37:17.000Z",formattedDate:"27. Januar 2023",tags:[],readingTime:.78,hasTruncateMarker:!1,authors:[],frontMatter:{},nextItem:{title:"Top-Down-Entwurf",permalink:"/EF-Informatik/Top-Down-Entwurf"}},o={authorsImageUrls:[]},u=[],d={toc:u};function p(e){let{components:n,...t}=e;return(0,i.kt)("wrapper",(0,r.Z)({},d,t,{components:n,mdxType:"MDXLayout"}),(0,i.kt)("h1",{id:"ziel-des-spiels"},"Ziel des Spiels"),(0,i.kt)("p",null,"Numtrip ist ein Denkspiel das \xe4hnlichkeiten dem sehr popul\xe4ren Spiel 2048 hat. Das Feld besteht auf gleich viel Reihen und Zeilen. Die Felder sind gef\xfcllt zuf\xe4lligen geraden Zahlen. Man kann ein Feld ausw\xe4hlen, wenn ein anligendes Feld mit der selben Zahl gef\xfcllt werden diese und die mit diesem Feld anliegende Verbunden. Das ausgew\xe4hlte feld wird verdoppelt. Das ganze geht so bis man 1024 erreicht hat."),(0,i.kt)("h1",{id:"umsetzung-des-spiels"},"Umsetzung des Spiels"),(0,i.kt)("h1",{id:"gr\xf6sste-herrausforderung"},"Gr\xf6sste Herrausforderung"),(0,i.kt)("p",null,"Ich bin beim Programmieren sehr oft auf Probleme gestossen die ich mal mehr mal weniger elegant gel\xf6st habe. Ein Problem auf das ich immer wieder gestossen bin hat sich in meiner feldverschiebung definition abgespielt. Diese hat zwar immer funktioniert aber nie ganz, da ich nie smart genug war mehrere senarien zu testen und sie dann nur f\xfcr einen speziellen fall funktioniert hat. Also musste ich immer wieder zu der Definition zur\xfcckkehren um mir erneut gedanken dazu zu machen. "),(0,i.kt)("h1",{id:"tipps"},"Tipps"))}p.isMDXComponent=!0}}]);