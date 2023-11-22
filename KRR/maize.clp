(watch all)

(defrule rule1
  (symptom yellow-leaves)
  (symptom stunted-growth)
  =>
  (assert (disease Maize-Dwarf-Mosaic-Virus))
)

(defrule rule2
  (symptom brown-spots)
  (symptom wilting)
  =>
  (assert (disease Northern-Corn-Leaf-Blight))
)

(defrule rule3
  (symptom white-powder-on-leaves)
  (symptom yellowing)
  =>
  (assert (disease Powdery-Mildew))
)

(defrule default-rule
  =>
  (assert (disease No-Specific-Disease-Found))
)

(defrule print-result
  (declare (salience -1))
  ?f <- (disease ?d)
  =>
  (printout t "The likely maize disease is: " ?d crlf)
  (retract ?f)
)

