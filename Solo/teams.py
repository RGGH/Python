Python 3.6.8 (default, Aug 20 2019, 17:12:48) 
[GCC 8.3.0] on linux
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 7, in <module>
    team.append(players[1])
TypeError: 'set' object does not support indexing
>>> 
========================== RESTART: /home/ian/t.py ==========================
['bob']
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 8, in <module>
    players.remove(players[1])
AttributeError: 'tuple' object has no attribute 'remove'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 8, in <module>
    players.remove([1])
AttributeError: 'tuple' object has no attribute 'remove'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 8, in <module>
    players.remove(1)
AttributeError: 'tuple' object has no attribute 'remove'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 8, in <module>
    players.remove[1]
AttributeError: 'tuple' object has no attribute 'remove'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 8, in <module>
    players.delete([1])
AttributeError: 'tuple' object has no attribute 'delete'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 9, in <module>
    players.delete([1])
AttributeError: 'tuple' object has no attribute 'delete'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 7, in <module>
    team.append(players[1])
TypeError: 'set' object does not support indexing
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 9, in <module>
    players.delete(1)
AttributeError: 'tuple' object has no attribute 'delete'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 9, in <module>
    players.remove(1)
AttributeError: 'tuple' object has no attribute 'remove'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 9, in <module>
    players.remove[1]
TypeError: 'builtin_function_or_method' object is not subscriptable
>>> 
========================== RESTART: /home/ian/t.py ==========================
['bob']
['dave', 'jim', 'ray', 'ted']
>>> 
========================== RESTART: /home/ian/t.py ==========================
['bob']
['dave', 'jim', 'ray', 'ted']
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 7, in <module>
    team.append(choice.players)
AttributeError: 'function' object has no attribute 'players'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 7, in <module>
    p1 = choice.players()
AttributeError: 'function' object has no attribute 'players'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 7, in <module>
    p1 = choice.players
AttributeError: 'function' object has no attribute 'players'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 7, in <module>
    p1 = random.choice(players)
NameError: name 'random' is not defined
>>> 
========================== RESTART: /home/ian/t.py ==========================
[]
['dave', 'jim', 'ray', 'ted']
>>> 
========================== RESTART: /home/ian/t.py ==========================
['jim']
['dave', 'jim', 'ray', 'ted']
>>> 
========================== RESTART: /home/ian/t.py ==========================
['ray']
['dave', 'bob', 'jim', 'ted']
>>> 
========================== RESTART: /home/ian/t.py ==========================
['ray']
['dave', 'bob', 'jim', 'ted']
>>> 
========================== RESTART: /home/ian/t.py ==========================
['dave']
['bob', 'jim', 'ray', 'ted']
['ray']
['bob', 'jim', 'ted']
>>> 
========================== RESTART: /home/ian/t.py ==========================
['dave']
['bob', 'jim', 'ray', 'ted']
['jim']
['bob', 'ray', 'ted']
['dave', 'ray']
['bob', 'ted']
['jim', 'bob']
['ted']
['dave', 'ray', 'ted']
[]
Traceback (most recent call last):
  File "/home/ian/t.py", line 19, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
['bob']
['dave', 'jim', 'ray', 'ted']
['ted']
['dave', 'jim', 'ray']
['bob', 'jim']
['dave', 'ray']
['ted', 'ray']
['dave']
>>> 
========================== RESTART: /home/ian/t.py ==========================
['Boo']
['dave', 'bob', 'jim', 'ray', 'ted', 'moo']
['dave']
['bob', 'jim', 'ray', 'ted', 'moo']
['Boo', 'ted']
['bob', 'jim', 'ray', 'moo']
['dave', 'bob']
['jim', 'ray', 'moo']
['Boo', 'ted', 'jim']
['ray', 'moo']
['dave', 'bob', 'ray']
['moo']
>>> 
========================== RESTART: /home/ian/t.py ==========================
['Boo']
['dave', 'bob', 'jim', 'ray', 'ted', 'moo', 'doo', 'loo']
['loo']
['dave', 'bob', 'jim', 'ray', 'ted', 'moo', 'doo']
['Boo', 'ray']
['dave', 'bob', 'jim', 'ted', 'moo', 'doo']
['loo', 'jim']
['dave', 'bob', 'ted', 'moo', 'doo']
['Boo', 'ray', 'bob']
['dave', 'ted', 'moo', 'doo']
['loo', 'jim', 'moo']
['dave', 'ted', 'doo']
['Boo', 'ray', 'bob', 'doo']
['dave', 'ted']
['loo', 'jim', 'moo', 'ted']
['dave']
>>> 
========================== RESTART: /home/ian/t.py ==========================
['ted']
['dave', 'bob', 'jim', 'ray', 'moo', 'Boo', 'doo', 'loo']
['loo']
['dave', 'bob', 'jim', 'ray', 'moo', 'Boo', 'doo']
['ted', 'bob']
['dave', 'jim', 'ray', 'moo', 'Boo', 'doo']
['loo', 'ray']
['dave', 'jim', 'moo', 'Boo', 'doo']
['ted', 'bob', 'jim']
['dave', 'moo', 'Boo', 'doo']
['loo', 'ray', 'dave']
['moo', 'Boo', 'doo']
['ted', 'bob', 'jim', 'moo']
['Boo', 'doo']
['loo', 'ray', 'dave', 'Boo']
['doo']
['ted', 'bob', 'jim', 'moo', 'doo']
[]
Traceback (most recent call last):
  File "/home/ian/t.py", line 19, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
['bob']
['dave', 'jim', 'ray', 'ted', 'moo', 'Boo', 'doo', 'loo']
['ray']
['dave', 'jim', 'ted', 'moo', 'Boo', 'doo', 'loo']
Traceback (most recent call last):
  File "/home/ian/t.py", line 31, in <module>
    print("Team A " + teamA)
TypeError: must be str, not list
>>> 
========================== RESTART: /home/ian/t.py ==========================
['doo']
['dave', 'bob', 'jim', 'ray', 'ted', 'moo', 'Boo', 'loo']
['ted']
['dave', 'bob', 'jim', 'ray', 'moo', 'Boo', 'loo']
Traceback (most recent call last):
  File "/home/ian/t.py", line 28, in <module>
    print("Team A " + teamA)
TypeError: must be str, not list
>>> 
========================== RESTART: /home/ian/t.py ==========================
['dave']
['bob', 'jim', 'ray', 'ted', 'moo', 'Boo', 'doo', 'loo']
['moo']
['bob', 'jim', 'ray', 'ted', 'Boo', 'doo', 'loo']
Team A ['dave']
Traceback (most recent call last):
  File "/home/ian/t.py", line 29, in <module>
    print ("Team B" + teamB)
TypeError: must be str, not list
>>> 
========================== RESTART: /home/ian/t.py ==========================
['doo']
['dave', 'bob', 'jim', 'ray', 'ted', 'moo', 'Boo', 'loo']
['bob']
['dave', 'jim', 'ray', 'ted', 'moo', 'Boo', 'loo']
Team A ['doo']
Team B['bob']
['doo', 'Boo']
['dave', 'jim', 'ray', 'ted', 'moo', 'loo']
['bob', 'jim']
['dave', 'ray', 'ted', 'moo', 'loo']
Team A ['doo', 'Boo']
Team B['bob', 'jim']
['doo', 'Boo', 'ted']
['dave', 'ray', 'moo', 'loo']
['bob', 'jim', 'ray']
['dave', 'moo', 'loo']
Team A ['doo', 'Boo', 'ted']
Team B['bob', 'jim', 'ray']
['doo', 'Boo', 'ted', 'loo']
['dave', 'moo']
['bob', 'jim', 'ray', 'moo']
['dave']
Team A ['doo', 'Boo', 'ted', 'loo']
Team B['bob', 'jim', 'ray', 'moo']
['doo', 'Boo', 'ted', 'loo', 'dave']
[]
Traceback (most recent call last):
  File "/home/ian/t.py", line 20, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
['moo']
['loo']
Team A ['moo']
Team B['loo']
['moo', 'doo']
['loo', 'bob']
Team A ['moo', 'doo']
Team B['loo', 'bob']
['moo', 'doo', 'ray']
['loo', 'bob', 'ted']
Team A ['moo', 'doo', 'ray']
Team B['loo', 'bob', 'ted']
['moo', 'doo', 'ray', 'dave']
['loo', 'bob', 'ted', 'Boo']
Team A ['moo', 'doo', 'ray', 'dave']
Team B['loo', 'bob', 'ted', 'Boo']
['moo', 'doo', 'ray', 'dave', 'jim']
Traceback (most recent call last):
  File "/home/ian/t.py", line 20, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['dave']
Team B['doo']
Team A ['dave', 'ray']
Team B['doo', 'jim']
Team A ['dave', 'ray', 'moo']
Team B['doo', 'jim', 'Boo']
Team A ['dave', 'ray', 'moo', 'loo']
Team B['doo', 'jim', 'Boo', 'ted']
Traceback (most recent call last):
  File "/home/ian/t.py", line 20, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['loo']
Team B['ray']
Team A ['loo', 'jim']
Team B['ray', 'bob']
Team A ['loo', 'jim', 'doo']
Team B['ray', 'bob', 'Boo']
Team A ['loo', 'jim', 'doo', 'ted']
Team B['ray', 'bob', 'Boo', 'dave']
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['loo']
Team B['ted']
Team A ['loo', 'ray']
Team B['ted', 'bob']
Team A ['loo', 'ray', 'moo']
Team B['ted', 'bob', 'jim']
Team A ['loo', 'ray', 'moo', 'dave']
Team B['ted', 'bob', 'jim', 'doo']
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['jim']
Team B['ted']
Team A ['jim', 'loo']
Team B['ted', 'ray']
Team A ['jim', 'loo', 'moo']
Team B['ted', 'ray', 'doo']
Team A ['jim', 'loo', 'moo', 'Boo']
Team B['ted', 'ray', 'doo', 'dave']
Traceback (most recent call last):
  File "/home/ian/t.py", line 20, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['ted']
Team B['jim']
Team A ['ted', 'doo']
Team B['jim', 'bob']
Team A ['ted', 'doo', 'ray']
Team B['jim', 'bob', 'Boo']
Team A ['ted', 'doo', 'ray', 'dave']
Team B['jim', 'bob', 'Boo', 'loo']
Traceback (most recent call last):
  File "/home/ian/t.py", line 20, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['ray']
Team B['loo']
Team A ['ray', 'dave']
Team B['loo', 'jim']
Team A ['ray', 'dave', 'moo']
Team B['loo', 'jim', 'Boo']
Team A ['ray', 'dave', 'moo', 'ted']
Team B['loo', 'jim', 'Boo', 'doo']
Traceback (most recent call last):
  File "/home/ian/t.py", line 20, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 11, in <module>
    while (players) > 0:
TypeError: '>' not supported between instances of 'list' and 'int'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Traceback (most recent call last):
  File "/home/ian/t.py", line 11, in <module>
    while (players) > 1:
TypeError: '>' not supported between instances of 'list' and 'int'
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['doo']
Team B['moo']
Team A ['doo', 'loo']
Team B['moo', 'bob']
Team A ['doo', 'loo', 'jim']
Team B['moo', 'bob', 'ray']
Team A ['doo', 'loo', 'jim', 'dave']
Team B['moo', 'bob', 'ray', 'Boo']
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['bob']
Team B['ted']
Team A ['bob', 'dave']
Team B['ted', 'Boo']
Team A ['bob', 'dave', 'doo']
Team B['ted', 'Boo', 'loo']
Team A ['bob', 'dave', 'doo', 'ray']
Team B['ted', 'Boo', 'loo', 'moo']
Traceback (most recent call last):
  File "/home/ian/t.py", line 20, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['dave']
Team B['bob']
Team A ['dave', 'doo']
Team B['bob', 'ted']
Team A ['dave', 'doo', 'Boo']
Team B['bob', 'ted', 'ray']
Team A ['dave', 'doo', 'Boo', 'moo']
Team B['bob', 'ted', 'ray', 'jim']
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['woo']
Team B['Boo']
Team A ['woo', 'jim']
Team B['Boo', 'dave']
Team A ['woo', 'jim', 'bob']
Team B['Boo', 'dave', 'doo']
Team A ['woo', 'jim', 'bob', 'moo']
Team B['Boo', 'dave', 'doo', 'ted']
Traceback (most recent call last):
  File "/home/ian/t.py", line 20, in <module>
    p2 = choice(players)
  File "/usr/lib/python3.6/random.py", line 260, in choice
    raise IndexError('Cannot choose from an empty sequence') from None
IndexError: Cannot choose from an empty sequence
>>> 
========================== RESTART: /home/ian/t.py ==========================
Team A ['Boo']
Team B['ray']
Team A ['Boo', 'ted']
Team B['ray', 'woo']
Team A ['Boo', 'ted', 'doo']
Team B['ray', 'woo', 'dave']
Team A ['Boo', 'ted', 'doo', 'moo']
Team B['ray', 'woo', 'dave', 'bob']
>>> 
