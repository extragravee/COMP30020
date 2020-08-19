%check if element is member of a list
%=====================================
%base case, true if Elt is the first element
member(Elt, [Elt|_]).

%Elt is member of list IF Elt is member of Rest of the list
%head of predicate here splits the list into two parts (first time this runs the two parts are
%empty list | entire list
member(Elt, [_|Rest]) :-
	member(Elt, Rest).

%check if two elements are adjacent
%=====================================
adjacent(E1, E2, List) :-
%joining something to E1, E2 | Rest, to form List
	append(_, [E1, E2| _], List).
	
%method2
adjacent2(E1, E2, [E1, E2|_]).
adjacent2(E1, E2, [_|Rest]):-
	adjacent2(E1, E2, Rest).

