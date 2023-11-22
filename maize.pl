% Rules
disease(MaizeDisease) :-
    symptom(yellow_leaves),
    symptom(stunted_growth),
    MaizeDisease = 'Maize Dwarf Mosaic Virus'.

disease(MaizeDisease) :-
    symptom(brown_spots),
    symptom(wilting),
    MaizeDisease = 'Northern Corn Leaf Blight'.

disease(MaizeDisease) :-
    symptom(white_powder_on_leaves),
    symptom(yellowing),
    MaizeDisease = 'Powdery Mildew'.

% Default rule
disease('No Specific Disease Found').

% Example usage
symptom(yellow_leaves).
symptom(stunted_growth).

?- disease(MaizeDisease), write('The likely maize disease is: '), write(MaizeDisease), nl.

