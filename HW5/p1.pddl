;; There is only one block, A, which is on the table.  A can with red
;; paint is on the table.  There is a clean brush on the table.  Our
;; goal is to have A be red, and the arm empty.

(define (problem 1)
  (:domain hw5)
  (:objects A B C )
  (:init (arm-empty)
    (block A)
    (on-table A)
    (clear A)
    (paint-can B red)
    (on-table B)
    (clear B)
    (brush C)
    (on-table C)
    (clear C)
    (clean C))
  (:goal (and (arm-empty) (color A red))))



