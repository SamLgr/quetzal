Systeem Quetzal E-Shop:
- Workers en users worden beide bijgehouden in een lijst (CircularLinkedList en DoubleList zijn makkelijk afwisselbaar)
- Afgehandelde bestellingen worden bijgehouden in BSTTable maar kan zeer snel naar andere geavanceerde tabelimplementatie veranderd worden
- Chocolade melk objecten worden bijgehouden in een hashmap
- Iedere cyclus wordt informatie uit het systeem bijgehouden in een LogInfo lijst
- Bij log commando wordt CreateLogFile uitgevoerd, voor elke cycle wordt informatie uit LogInfo naar een HTML-bestand geschreven

Test:
- Doctests voor alle klassen bevinden zich in Test.py
- Input bestanden kunnen voor alle ADTs omgezet worden naar DOT-bestanden en ofwel via graphviz library of via webgraphviz omgezet worden naar een grafische weergave: output is terug te vinden in '/output' of in de main directory
--> Kan via CreateGraph voor BST, TTFT, Stack en CircularLinkedList
--> Kan via functieoproep naar writeDotFile() voor DoubleList en Queue (bevindt zich in de klassen zelf)
--> Kan via functieoproep naar dotDebug() voor RBTree en Hashmap (bevindt zich in de klassen zelf)
