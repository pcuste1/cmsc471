;; There is only one block, A, which is on the table.  A sprayer with
;; red paint is on the table.  Our goal is to have A be red and the
;; arm empty.

(define (problem 0)
  (:domain hw5)
  (:objects A B )
  (:init (arm-empty)
	 (block A)
	 (on-table A)
	 (clear A)
         (sprayer B red)
	 (on-table B)
	 (clear B))
  (:goal (and (arm-empty) (color A red))))



