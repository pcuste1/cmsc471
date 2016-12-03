;; Block A is on the table, B is on A and C on B.  On the table are a
;; water bucket, a red sprayer, cans of blue and green paint and a
;; clean brush.  The goal is to make A red, B green and C blue and to
;; have A on B, B on C and C on the table and the brush clean and arm
;; empty.

(define (problem 4)
  (:domain hw5)
  (:objects A B C D E F G H )
  (:init (arm-empty)
  	 (block A)
	 (on-table A)
	 (block B)
	 (on B A)
	 (block C)
	 (on C B)
	 (clear C)
	 (water-bucket D)
	 (on-table D)
	 (clear D)
	 (sprayer E red)
	 (on-table E)
	 (clear E)
	 (paint-can F blue)
	 (on-table F)
	 (clear F)
	 (paint-can G green)
	 (on-table G)
	 (clear G)
	 (brush H)
	 (on-table H)
	 (clear H)
	 (clean H))

(:goal (and (arm-empty)
       (color A red)
       (color B green)
       (color C blue)
       (on-table C)
       (on B C)		
       (on A B)
       (clear A)
       (clean H)
)))


