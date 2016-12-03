;; Block A is on the table, block B on A and there is nothing on B.  A
;; water bucket, a brush, a A blue sprayer and a red paint can are on
;; the table and clear.  The goal is to for A to be colored red and B
;; blue and the brush be clean.

(define (problem 1)
  (:domain hw5)
  (:objects A B C D E F )
  (:init (arm-empty)
         ;;... block A is on the table ...
	 (block A)
	 (on-table A)
	 ;;... block B is on block A and there's nothing on B ...
	 (block B)
	 (on B A)
	 (clear B)
	 ;;... there is a blue sprayer on the table and nothing is on it ...
	 (sprayer C blue)
	 (on-table C)
	 (clear C)
	 ;;... there is a red paint can on the table and noting is on it ...
	 (paint-can D red)
	 (on-table D)
	 (clear D)
	 ;;... there is a clean brush on the table and nothing is on it  ...
	 (brush E)
	 (on-table E)
	 (clear E)
	 (clean E)
	 ;;... there is a water bucket on the table and nothing is on it ...
	 (water-bucket F)
	 (on-table F)
	 (clear F)
      )
  (:goal (and (arm-empty)
              ;;... A is red ...
	      (color A red)
              ;;... B is blue ...
	      (color B blue)
              ;;... the brush is clean ...
	      (clean E)
           )))





