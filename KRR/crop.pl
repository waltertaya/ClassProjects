% Facts
symptom('Maize Dwarf Mosaic Virus', yellow_leaves).
symptom('Maize Dwarf Mosaic Virus', stunted_growth).
symptom('Northern Corn Leaf Blight', brown_spots).
symptom('Northern Corn Leaf Blight', wilting).
symptom('Powdery Mildew', white_powder_on_leaves).
symptom('Powdery Mildew', yellowing).
symptom('Southern Corn Leaf Blight', 'large_tan_lesions').
symptom('Southern Corn Leaf Blight', 'lesions_with_yellow_halos').
symptom('Corn Smut', 'swollen_galls_on_plant').
symptom('Corn Smut', 'black_powdery_masses').

% Rules
disease(MaizeDisease) :-
    symptom(MaizeDisease, _).

% Symptoms for a specific disease
symptoms_for_disease(Disease, Symptoms) :-
    setof(Symptom, symptom(Disease, Symptom), Symptoms).

% Predicate to start the diagnosis
start_diagnosis :-
    write('Welcome to the Maize Disease Diagnosis System!'), nl,
    write('Please answer the following questions to help identify the maize disease.'), nl,
    ask_symptoms.

% Predicate to ask the user about symptoms
ask_symptoms :-
    write('Do the leaves of your maize plants appear yellow? (yes/no): '),
    read(Response),
    process_response(Response).

% Predicate to process user responses
process_response(yes) :-
    diagnose('Maize Dwarf Mosaic Virus').
process_response(no) :-
    write('Do you observe brown spots on the leaves of your maize plants? (yes/no): '),
    read(Response),
    process_brown_spots_response(Response).

% Predicate to process user responses related to brown spots
process_brown_spots_response(yes) :-
    diagnose('Northern Corn Leaf Blight').
process_brown_spots_response(no) :-
    write('Do you see a white powder on the leaves of your maize plants? (yes/no): '),
    read(Response),
    process_powdery_mildew_response(Response).

% Predicate to process user responses related to powdery mildew
process_powdery_mildew_response(yes) :-
    diagnose('Powdery Mildew').
process_powdery_mildew_response(no) :-
    write('Do you observe large tan lesions on the leaves of your maize plants? (yes/no): '),
    read(Response),
    process_southern_leaf_blight_response(Response).

% Predicate to process user responses related to southern leaf blight
process_southern_leaf_blight_response(yes) :-
    diagnose('Southern Corn Leaf Blight').
process_southern_leaf_blight_response(no) :-
    write('Do you notice swollen galls on the plant? (yes/no): '),
    read(Response),
    process_corn_smut_response(Response).

% Predicate to process user responses related to corn smut
process_corn_smut_response(yes) :-
    diagnose('Corn Smut').
process_corn_smut_response(no) :-
    write('Unable to diagnose the disease. Please consult with a plant pathologist.').
    
% Predicate to diagnose and print the disease
diagnose(Disease) :-
    write('The likely maize disease is: '), write(Disease), nl,
    symptoms_for_disease(Disease, Symptoms),
    write('Symptoms for '), write(Disease), write(': '), write(Symptoms), nl.
