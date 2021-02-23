%check if element is member of a list
%=====================================
%base case, true if Elt is the first element
%member(Elt, [Elt|_]).

take(N, List, Front):-
	append(Front, _, List),
	length(Front, N).

%Elt is member of list IF Elt is member of Rest of the list
%head of predicate here splits the list into two parts (first time this runs the two parts are
%empty list | entire list
%member(Elt, [_|Rest]) :-
%	member(Elt, Rest).


%check if two elements are adjacent
%=====================================
adjacent(E1, E2, List) :-
%joining something to E1, E2 | Rest, to form List
	append(_, [E1, E2| _], List).
	
%method2
adjacent2(E1, E2, [E1, E2|_]).
adjacent2(E1, E2, [_|Rest]):-
	adjacent2(E1, E2, Rest).


%check if a list is a proper list
%=====================================
proper_list([]).
proper_list([_|Tail]) :-
	proper_list(Tail).
	

%check if every element of list is Elt
%=====================================
listof(_, []).
listof(Elt, [Elt|Rest]) :-
	listof(Elt,Rest).
	
	
%check if every element of list is Elt
%=====================================
allsame([Elt|List]) :-
	listof(Elt, List).
	
	
%check if E1 appears before E2 in List
%=====================================
before(E1, E2, List) :-
    append(_, [E1|Rest], List),
    member(E2, Rest).
    
%method2
before(E1, E2, [E1|List]):-
	member(E2, List).
before(E1, E2, [_, List]):-
	before(E1, E2, List).

%check if elems in X appear in Y, 
%can be anywhere, but same order
%===================================

sublist([],_).

sublist([X|Xs], [_|Ys]) :-
    sublist([X|Xs], Ys).

sublist([X|Xs], [X|Ys]) :-
   sublist(Xs, Ys).
   
%check cards
valid_card(card(Rank, _)) :-
        (integer(Rank) ->
        between(1, 10, Rank)
    ; memberchk(Rank, [ace, jack, queen, king])).   
	

%summing up a list
sumlist([] , 0).
sumlist([Head|Tail], Sum) :-
    sumlist(Tail, S1),
    Sum is Head + S1.
