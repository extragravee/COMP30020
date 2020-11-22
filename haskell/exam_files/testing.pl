/*
Testing
tree(1,t(a,t(b,t(d,nil,nil),t(e,nil,nil)),t(c,nil,t(f,t(g,nil,nil),nil)))).
tree(2,t(a,nil,nil)).
tree(3,nil).
*/

/* check if valid tree*/
is_tree(nil).
is_tree(tree(_, L, R)) :- is_tree(L), is_tree(R).