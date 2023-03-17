# Cheatsheet API's

eine API macht es für den Server möglich die Daten der Website zu verarbeiten. Sie ist nicht sichtbar.

HTTP request: HTTP steht für Hyper-Text Tranfer Protocol und steht zeigt dem Server dass er sich an die HTTP Regeln halten muss. Diese bestehen aus vier Sachen.   

URL: ist der Name der Website und der sie im Web gefunden werden kann   

Method: Besteht aus vier: GET, POST, PUT und DELETE sie beschreiben was der Server machen soll   

Headers: Beschreibt das Format bzw. welches von welchem Gerät die Anfrage kommt. Das ist nötig damit der Server die Website im richtigen Format schickt. Beschreibt auch was im Body ist sowie zusätzliche Informationen wie Zeit etc.   

Body: Enthält die Daten die der Nutzer zum Server schickt.

JSON: Ist ein Textformat, dass von den meisten API's übernommen ist. Es hat zwei Teile, keys und values. Keys repräsentiert ein Attribut über das Object. Der Key braucht ein value.

```"crust": "original"```   
Bei einer Pizza wären die Krustenart oder die Toppings der key und die dicke der Kruste oder Pepperoni als Topping das value.

XML: Ist wie JSON ein Textformat, dass aber weniger benutzt wird. XML besteht aus einer Node (Key bei JSON) und einem Value.   

```<crust>original</crust>```

Polling: Wenn man immer wieder die gleich Anfrage an den Server schickt.

# Blog API mit Node-RED:
Um eine API mit Node-Red zu erstellen muss man in einem Flow einen "http in", einen "function" und einen "http response" Node benutzen. In den http in Node kann man den Namen der URL bestimmen mit der man den Node und damit auch die function aufrufen kann. In dem functions Node kann man dann z.B den Value vom Key in ein Emoji ändern. http response schickt die Änderung zurück an den "Anfrager".    
```
let emoji = msg.payload.text;

emoji = emoji.replace(/hello/g, '👋');
emoji = emoji.replace(/marc/g, '🏃‍♀️');
emoji = emoji.replace(/noah/g, '🤷‍♀️');

msg.payload = {
    msg: emoji
};

return msg;
```
so könnte der Code in einem function Node aussehen, wichtig die Code muss im Funktion tab sein. Die erste Zeile bestimmt was im Key stehen muss damit der Value geändert wird. Z.B könnte so ```msg.payload.python;``` stehen so müsste man python in den Key schreiben.   
Zeile 2-4 bestimmen welcher Text in welches Emoji geändert wird bei meinem Beispiel werden die Worte hello, marc und noah durch emojis getauscht Diese müssen in den Value vom Key geschrieben werden.   
## Erfahrungen
Ich hatte anfangs durchaus Probleme mit der Erstellung der API. Das erste Problem, dass ich hatte war bei der URL bei welcher ich Probleme hatte die richtige einzugeben. Man muss nähmlich von der URL der Website alles bis zum .com löschen und dann die Endung die man im http in Node bestimmt hat hinzufügen.    
Mein zweites Problem hatte ich beim Code für den function Node. Erstmal musste ich rausfinden bei welchem Tab ich den Code reinschreiben bzw. reinkopieren muss damit er auch funktioniert. Ein letztes Problem hatte ich, dass ich nicht wusste, dass ich noch einen Key brauche und was in dem Key steht. Wie das jetzt geht habe ich ja schon erklärt. Debug Nodes helfen einem sehr gut dabei zu sehen ob man die URL erreicht hat und oder wo das Problem liegt, dass es nicht weiter geht.