(define acc
  (lambda (x)
    (lambda (i)
      (set! x (+ x i))
      x)))