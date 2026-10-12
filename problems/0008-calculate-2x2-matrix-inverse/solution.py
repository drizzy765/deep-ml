

def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
   a, b = matrix[0][0], matrix[0][1]
   c, d = matrix[1][0], matrix[1][1]

   # determinant of a matrix
   det = a*d - b*c
   # return none if 0 if matrix is singular invertible
   if det == 0:
      return None
   # return the inverse calculation 1/det([d,-b],[-c, a])
   return [
      [d/det, -b/det],
      [-c/det, a/det]
   ]
  

