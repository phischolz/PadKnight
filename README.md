# PadKnight
## Coding Challenge

A Horse on the Phonepad:
Imagine you place a knight chess piece on a phone dial pad. This chess piece moves in an uppercase “L” shape: two steps horizontally followed by one vertically, or one step horizontally then two vertically: 

https://imgur.com/a/RoKf8Sg 

Pay no attention to the poorly-redacted star and pound keys
Suppose you dial keys on the keypad using only hops a knight can make. Every time the knight lands on a key, we dial that key and make another hop. The starting position counts as being dialed.

Your mission is now “Write a software that solves the following question:
How many distinct numbers can you dial in N hops from a particular starting position?”

## Solution Notes
* Numbers with exactly N digits, given a starting Point: reachability(pad, N)
* Numbers with UP TO N digits, given starting Point: Sum over reachability(pad, i) with i = 1...N
* Numbers with up to/exactly N digits, any starting point: the previous solutions, summed up over all starting points.
