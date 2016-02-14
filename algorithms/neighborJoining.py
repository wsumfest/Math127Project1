"""neighbor joining algorithm"""
import numpy


# FOR TESTING PUTPOSES:
# example matrix given in wiki:
#
#      a   b   c   d   e
# a [[ 0.  5.  9.  9.  8.]
# b  [ 5.  0.  10. 10. 9.]
# c  [ 9.  10. 0.  8.  7.]
# d  [ 9.  10. 8.  0.  3.]
# e  [ 8.  9.  7.  3.  0.]]
#
# From this, create a QMatrix, then join 2 vertices, which creates another matrix, 
# then create another QMatrix based on the new matrix... repeat until all 
# vertices are joined.

matrixSize = 5
testMatrix = numpy.zeros((matrixSize, matrixSize))

testMatrix[0][1] = 5
testMatrix[0][2] = 9
testMatrix[0][3] = 9
testMatrix[0][4] = 8
testMatrix[1][0] = 5
testMatrix[1][2] = 10
testMatrix[1][3] = 10
testMatrix[1][4] = 9
testMatrix[2][0] = 9
testMatrix[2][1] = 10
testMatrix[2][3] = 8
testMatrix[2][4] = 7
testMatrix[3][0] = 9
testMatrix[3][1] = 10
testMatrix[3][2] = 8
testMatrix[3][4] = 3
testMatrix[4][0] = 8
testMatrix[4][1] = 9
testMatrix[4][2] = 7
testMatrix[4][3] = 3





# Create a QMatrix 
# Use the following formula found on wiki:
# Q(i, j) = (n-2)*d(i, j) - (sum of row i) - (sum of column j)
# example: Q(a, b) = 3*5 - (5+9+9+8) - (5+10+10+9) = -50

def QMatrix(matrix):
	assert matrix.shape[0] == matrix.shape[1], 'matrix not square'

	# first make a nxn zero matrix, and fill it with the correct numbers.
	sizeOfMatrix = matrix.shape[0]
	QMatrix = numpy.zeros((sizeOfMatrix, sizeOfMatrix))

	# calculates the sum of a particular row
	def calcRowSum(row):
		rowSum = 0
		colCounter = 0
		while colCounter < sizeOfMatrix:
			rowSum += matrix[row][colCounter]
			colCounter += 1
		return rowSum

	# calculates the sum of a particular column
	def calcColSum(col):
		colSum = 0
		rowCounter = 0
		while rowCounter < sizeOfMatrix:
			colSum += matrix[rowCounter][col]
			rowCounter += 1
		return colSum


	for x in range(0, sizeOfMatrix):
		rowSum = calcRowSum(x)

		for y in range(0, sizeOfMatrix):
			if x == y:
				continue # don't wanna calculate values along the diagonal
			colSum = calcColSum(y)
			QMatrix[x][y] = (sizeOfMatrix - 2) * matrix[x][y] - colSum - rowSum
			
	return QMatrix

print QMatrix(testMatrix)



