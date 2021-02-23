Declarative Programming
=======================
Repo for COMP30020 subject at UniMelb. In this subject I learnt contraint logic programming using Prolog, as well as function programming using Haskell. 

Table of contents
-----------------
<a href="#intro"> Introduction </a>
<a href="#p1"> Project 1 - Cribbage (Prolog) </a>
<a href="#p2"> Project 2 - Musical Chord (Haskell) </a>

Introduction <a name = "intro"> </a>
------------
I built 2 projects. One using prolog to play the card game <a href= "https://en.wikipedia.org/wiki/Cribbage">Cribbage</a>. And a second project to play Musical chord (description in folder).

Project 1 - Cribbage (Prolog) <a name = "p1"> </a>
-----------------------------
No one plays this game anymore, but the gist is: <br>

You are trying to build the best hand using the starting hand - 2 cards, and 4 out of the 5 cards dealt to you. You can have:
- Combinations of any number of cards totalling fifteen
- Runs (3 to 5 card straight)
- Pairs (Multiple pairs are scored pair by pair but may be referred to as three or four of a kind.)
- Flush (A four-card flush scores four and cannot include the starter card; a five-card flush scores five.)
- Having a jack of the same suit as the starter card ("one for his nob [or nobs or nibs]", sometimes called the "right" jack)

The script receives the starting hand, and statistically decides which hands being played would have the highest probability of winning. Of course this project doesn't account for the human tells component / bluffing / strategic playing based on what the opponents play. It's just a theoretical way of coving the maths side of the game. I thoroughly hated myself writing code in prolog, but being able to write code about a problem, by simply defining the problem properly and prolog's backtracking work its magic was very interesting. I hope I never use prolog again though.

Project 2 - Musical Chord (Haskell) <a name = "p2"> </a>
-----------------------------------
For a Musician game, one player is the composer and the other is the performer. The composer begins by selecting a three-pitch musical chord, where each pitch comprises a musical note, one of A, B, C, D, E, F, or G, and an octave, one of 1, 2, or 3. This chord will be the target for the game. The order of pitches in the target is irrelevant, and no pitch may appear more than once. This game does not include sharps or flats, and no more or less than three notes may be included in the target.

Once the composer has selected the target chord, the performer repeatedly chooses a similarly defined chord as a guess and tells it to the composer, who responds by giving the performer the following feedback:

 - how many pitches in the guess are included in the target (correct pitches)
 - how many pitches have the right note but the wrong octave (correct notes)
 - how many pitches have the right octave but the wrong note (correct octaves) 
