% checking whether the student is a DEKUT student
% facts
has(john, id).
has(mark, id).
has(walter, id).

taking(john, course).
taking(edward, course).
taking(kagiri, course).
taking(walter, course).

knows(john, lectureHall).
knows(walter, lectureHall).

% rules
is_student(X) :- has(X, id), taking(X, course), knows(X, lectureHall).

