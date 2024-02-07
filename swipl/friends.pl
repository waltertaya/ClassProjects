% example.pl

% Facts
likes(john, pizza).
likes(mary, chocolate).
likes(jane, pizza).

% Rules
friend(X, Y) :- likes(X, Z), likes(Y, Z).

