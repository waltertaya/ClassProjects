% Facts
symptom('Maize Dwarf Mosaic Virus', yellow_leaves).
symptom('Maize Dwarf Mosaic Virus', stunted_growth).
symptom('Northern Corn Leaf Blight', brown_spots).
symptom('Northern Corn Leaf Blight', wilting).
symptom('Powdery Mildew', white_powder_on_leaves).
symptom('Powdery Mildew', yellowing).

% Rules
disease(MaizeDisease) :-
    symptom(MaizeDisease, _).

% Symptoms for a specific disease
symptoms_for_disease(Disease, Symptoms) :-
    setof(Symptom, symptom(Disease, Symptom), Symptoms).

% Example queries
% Query by providing symptoms
?- disease(MaizeDisease), write('The likely maize disease is: '), write(MaizeDisease), nl.

% Query by providing disease name and display symptoms
?- symptoms_for_disease('Maize Dwarf Mosaic Virus', Symptoms), write('Symptoms for Maize Dwarf Mosaic Virus: '), write(Symptoms), nl.

