# Cheatsheet API's

eine API macht es für den Server möglich die Daten der Website zu verarbeiten. Sie ist nicht sichtbar.

HTTP request: HTTP steht für Hyper-Text Tranfer Protocol und steht zeigt dem Server dass er sich an die HTTP Regeln halten muss. Diese bestehen aus vier Sachen.   

URL: ist der Name der Website und der sie im Web gefunden werden kann   

Method: Besteht aus vier: GET, POST, PUT und DELETE sie beschreiben was der Server machen soll   

Headers: Beschreibt das Format bzw. welches von welchem Gerät die Anfrage kommt. Das ist nötig damit der Server die Website im richtigen Format schickt. Beschreibt auch was im Body ist sowie zusätzliche Informationen wie Zeit etc.   

Body: Enthält die Daten die der Nutzer zum Server schickt.

JSON: Ist ein Textformat, dass von den meisten API's übernommen ist. Es hat zwei Teile, keys und values. Keys repräsentiert ein Attribut über das Object. Der Key braucht ein value.
```py
"crust": "original"
```  
Bei einer Pizza wären die Krustenart oder die Toppings der key und die dicke der Kruste oder Pepperoni als Topping das value.

XML: Ist wie JSON ein Textformat, dass aber weniger benutzt wird. XML besteht aus einer Node (Key bei JSON) und einem Value.   
```py
<crust>original</crust>
```  
Polling: Wenn man immer wieder die gleich Anfrage an den Server schickt.