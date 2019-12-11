# Quizz (2019-11-20)

## Python iPython


## :o: Commentaires

```SQL
# Je suis un commentaire sur une seule ligne
# Je commence par un hashtag suivi d'UN ESPACE

"""
Je suis un bloc de commentaires
# Je commence et termine par TROIS double-quote 

@author je suis un decorateur pemettant de specifier le nom de l'auteur
"""

```

## :a: Structure d'un programme


:one: Entrée/Sortie

:pushpin: Entrée :

```python
>>> int(input(""))
```


:pushpin: Sortie :

```python
>>> print("")
```

:pushpin: block : Indentation de 3 espaces

```python
>>>    print("Indentation")
```

:pushpin: Erreur :

```
>>>    print("Indentation");
  File "<stdin>", line 1
    print("Indentation");
    ^
IndentationError: unexpected indent
```


## :two: Variables

##### :m: declaration :

```python
>>> x = 3
```

##### :m: types :

```python
>>> type(x)
<class 'int'>
```

| Type                 |  Python               | Format                   |
|----------------------|-----------------------|--------------------------|
| Nombre               | int, float            | 1 - 10, 1.0 - 10.0       |  
| Bouléen              | bool                  | True, False              |
| Chaine de caracteres | str                   | '1', "2.6", '2009-12-02' |


## :b: Structure de données

:pushpin: Variable

```python
>>> x = 3
```

:pushpin: Tableau

* str

```python
>>> x = 'Erna'
```

* afficher premier caractere

```python
>>> print(x[0])
```

* fonction externe `longueur`

```python
>>> len(x)
```

* fonction interne `capitalize`

```python
>>> print(x.capitalize())
```

:pushpin: Tuple

```python
>>> x = ( "Corlings", 20, 5401.23)
```



## :ab: Structure de contrôle et decisions

:m: Controle

:p: Operateurs

* Ordre des operateurs: `+- = GD, */ prioritaire et parenthese`

* `+ -  * / // % **` Calcul

:pushpin: Comparaison

`>  >=  < !=`

:pushpin: membre

`in not in`

:pushpin: logique

`and or`

:pushpin: example de logique

`3> 2 ** 3 and 3 == 3`

:m: Decisions

`if else: elif: `

:m: Intervalles

`range(0, 9)`


:m: Boucles

:pushpin: For

```python
for c in 'Boreal':
   print(c)
```

:pushpin: While

```python
while True:
   print('Que faire?')
```

:warning: Boucle infinie à arrêter avec `Ctrl-C`


## :o2: git Commands

##### :m: git `<command>`
    
```
$ git clone ...
```

```
$ git add ...
```

```
$ git commit ...
```

##### :m: configuration

```
$ git config --global --edit
```

