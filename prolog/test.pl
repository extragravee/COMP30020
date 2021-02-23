p(a,b).   p(b,c).   p(c,d).

q(X,Y) :- p(X,Y).
q(X,Y) :- p(Y,X).

r(X,Z) :- p(X,Z).
r(X,Z) :- p(X,Y), r(Y,Z).