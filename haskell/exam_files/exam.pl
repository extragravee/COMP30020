/* append two lists 
append1([], C, C).
append1([A|B], C, [A|BC]) :-
	append1(B, C, BC).
*/

/* Find if element appears in a list
memb(Elt, [Elt|_]).
memb(Elt, [_|Tail]) :-
	memb(Elt, Tail).
*/

/* take 
take(N, List, Front) :-
	length(Front, N),
	append(Front, _, List).
*/

/* reverse a list 
rev1([], []).
rev1([A|BC], CBA) :-
	rev1(BC, CB),
	append(CB, [A], CBA).
*/

append2([], C, C).
append2([A|B], C, [A|BC]):-
	append2(B, C, BC).

/* factorial best 
factorial(0, 1).
factorial(N, F) :-
	N > 0,
	N1 is N-1,
	factorial(N1, F1),
	F is N * F1.*/

fact2(N, F) :-
	(   N =:= 0 ->
		F = 1
	;	N > 0,
		N1 is N-1,
		fact2(N1, F1),
		F is N * F1
	).

factorial(N, F) :-
	fact3(N, 1, F).

fact3(N, A, F) :-
	(N =:= 0 ->
	F=A
	;A1 is A * N,
	N1 is N-1,
	fact3(N1, A1, F)).

rev2(List, R) :-
	rev3(List, [], R).

rev3([], A, A).
rev3([A|BC], Accum, BCA) :-
	A1 = [A|Accum],
	rev3(BC, A1, BCA).

ints_between(N1, N2, [N1|Rest]):-
	(   N1<N2
	->  New is N1+1,
		ints_between(New, N2, Rest)
	;   Rest = []
	).

ints_between2(N1, N2, List):-
	(   N1<N2
	->  List = [N1|Rest],
		New is N1 + 1,
		ints_between(New, N2, Rest)
	;   List = [N1]
	).
	
/*
% 100 questions
	
% 1. last element of list
my_last(Elt, [_|T]) :-
	my_last(Elt, T).

my_last(Elt, [Elt]).

% 2. second last elem of list
second_last(Elt, [Elt,_]).
second_last(Elt, [_|Xs]) :-
	second_last(Elt,Xs).

% 3. Kth element of list
element_at([X|_], 1, X).
element_at([_|Xs], Index, Item) :-
	I is Index-1,
	element_at(Xs, I, Item).

% 4. Count elements in a list
num_elems(List, Num):-
	count_elems(List, 0, Num).

count_elems([], Num, Num).
count_elems([_|Xs], Acc, Num) :-
	A1 is Acc + 1,
	count_elems(Xs, A1, Num).

% 6. Check if list is palindrome
palindrome(W) :-
	reverse(W,W).

% 5. Reverse a list
myrev([], []).
myrev([A|BC], CBA) :-
	myrev(BC, CB),
	append(CB, [A], CBA).

my_rev2([], A, A).
my_rev2([X|Xs], Acc, R) :-
	my_rev2(Xs, [X|Acc], R).

% 7. flatten structure of nested list
my_flatten(List, List2) :-
	my_flatten2(List, [], List2).

my_flatten2([], Acc, Acc).

my_flatten2([X|Xs], Acc, List2) :-
	(   is_list(X)
	->  my_flatten2(X, [], L1),
	    append(Acc, L1, L2),
	    my_flatten2(Xs, L2, List2)
	;   append(Acc, [X], L2),
		my_flatten2(Xs, L2, List2)
	).
	
% 8. eleminate duplicates
distinct_list([X], [X]).
distinct_list([X, Y|Xs], List) :-
	(   X=Y
	->  distinct_list([X|Xs], List)
	;   append([X], L1, List),
	    distinct_list([Y|Xs], L1)
	).


% 9. pack consecutive duplicates to sublists
pack([], A, S):-
	reverse(S, A).
pack([X|Xs], A, Acc):-
	count(X, 1, Xs, C),
	length(New, C),
	append(New, Rest, [X|Xs]),
	A1 = [New|Acc],
	pack(Rest, A, A1).


count(_ , A, [], A).
count(X, Acc, [Y|Xs], S):-
	(   X = Y
    ->	A1 is Acc + 1,
		count(X, A1, Xs, S)
	;   count(X, Acc, [], S)
	).

% 10. run length encoding using 9.

encode_modified(L, X) :-
	pack(L, PackedL,[]),
	encode_modified2(PackedL, [], Y),
	reverse(Y, X).

encode_modified2([] , A, A).
encode_modified2([X|Xs], Acc, Y):-
	A1 = [L,H],
	head(X, H),
	length(X, L),
	Acc1 = [A1|Acc],
	encode_modified2(Xs, Acc1,Y).


head([X|_], X).

% 11. ?- encode2([a,a,a,a,b,c,c,a,a,d,e,e,e,e],X).
%        X = [[4,a],b,[2,c],[2,a],d,[4,e]]

encode2(L, X) :-
	encode_modified(L, L1),
	no_dups(L1, [],X).

no_dups([], A, B) :-
	reverse(A, B).
no_dups([[C,V]|Xs], Acc, X) :-
	(	C > 1
	->  A1 = [[C,V]|Acc]
	;   A1 = [V|Acc]
	),   
	no_dups(Xs, A1, X).

/* =================================================
TREES
Testing
tree(1,t(a,t(b,t(d,nil,nil),t(e,nil,nil)),t(c,nil,t(f,t(g,nil,nil),nil)))).
tree(2,t(a,nil,nil)).
tree(3,nil).
*/

/* check if valid tree*/
is_tree(nil).
is_tree(t(_, L, R)) :- is_tree(L), is_tree(R).

/* BST from list */
construct(List, T) :-
	construct(List, T, nil).

construct([], A,A).
construct([X|Xs], T, Acc) :-
	intset_insert(X, Acc, A1),
	construct(Xs, T, A1).

intset_insert(N, nil, t(N,nil, nil)).
%intset_insert(N, t(N,L, R), t(N,L, R)).
intset_insert(N, t(X,L, R), Set1) :-
    (   N<X
    ->  Set1 = t(X,Left, R),
        intset_insert(N, L, Left)
    ;   Set1 = t(X,L, Right),
        intset_insert(N, R, Right)
    ).

% search bst
intset_member(Elt, tree(_, Elt, _)).
intset_member(Elt, tree(L, X, _)) :-
    Elt < X,
    intset_member(Elt, L).

intset_member(Elt, tree(_, X, R)) :-
    Elt > X,
    intset_member(Elt, R).

% in order traversal
tree_list(empty, []).
tree_list(node(L, Elt, R), List) :-
    tree_list(L, L1),
    append(L1, [Elt| R1], List),
    tree_list(R, R1).

% fancy optimised version of in order traversal
tree_list(Tree, List) :-
	tree_list(Tree, List, []).

tree_list(empty, List, List).
tree_list(node(Left,Elt,Right), List, List0) :-
	tree_list(Left, List, List1),
	List1 = [Elt|List2],
	tree_list(Right, List2, List0).

% ===============================================

% replace one occurrence of item in list
replace(E1, [Elt|Rest1], E2, [Elt|Rest2]) :-
    replace(E1, Rest1, E2, Rest2).

replace(E1, [E1| Rest1], E2, [E2| Rest2]) :-
    Rest1 = Rest2.

% zip two lists in A-B format
zip([], [], []).
zip([A|As], [B|Bs], [A-B|Rest]) :-
    zip(As, Bs, Rest).

% check if A's items appear in same order in Bs
sublist([], _).

sublist([X|Xs], [X|Ys]) :-
    sublist(Xs, Ys).

sublist([X|Xs], [_Y|Ys]) :-
    sublist([X|Xs], Ys).

% all distinct combinations of list
combs([],[]).
combs([Head|Tail],[Head|Tail2]) :-
        combs(Tail,Tail2).
combs([_|Tail],Tail2) :-
        combs(Tail,Tail2).

% filter
filter(_, [], []).
filter(P, [X|Xs], Filtered) :-
    (   call(P, X)
    ->  Filtered = [X|Filtered1]
    ;   Filtered = Filtered1),
        filter(P, Xs, Filtered1).

% count distinct number of items in list
count_distinct([], C, C).
count_distinct([Head|Tail], Accum, Count) :-
    (   member(Head, Tail)
    ->  count_distinct(Tail, Accum, Count)
    ;   A1 is Accum + 1,
        count_distinct(Tail, A1, Count)).

        

/* LIBRARY FUNCTIONS */
% EXCLUDES C1 AND C2
setof(X-Y, (C1, C2)^(knows(X,Y), employee(X, C1),
employee(Y, C2), X\=Y, C1\=C2),L).

