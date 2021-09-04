class EquationsSolver:
    """This class solves a systeme of linear equations using the Gaussian elimination. 
       It takes in the coefficients as list.
    """
    _matrix = []
    def __init__(self,*li,vector):
        """Takes in the coefficients of the equations as lists. 
           The last argument is always the the b vector, and it's a named argument. 
           The rows are written as lists.
        """
        self.vector = vector
        for i in li:
            self._matrix.append(i)
    def eliminate(self):
        """Turns the matrix into an upper triangular matrix. 
            It takes no arguments!!
        """
        for k in range(len(self._matrix)):
            if self._matrix[k][k] == 0:
                print("Can not perform the operaton")
                break
            else:
                for i in range(k+1,len(self._matrix)):
                    c = self._matrix[i][k]/self._matrix[k][k]
                    self.vector[i] -= c*self.vector[k]
                    self._matrix[i][k] = 0
                    for j in range(k+1,len(self._matrix)):
                        self._matrix[i][j] -= c*self._matrix[k][j]
        if self._matrix[len(self._matrix)-1][len(self._matrix)-1] == 0:
                        print("Can not perform the operaton")
    def show(self):
        """Prints the coefficients of the system of linear equation. 
           It takes zero parameters.
        """       
        i = len(self._matrix)
        j = len(self._matrix[0])
        print(i,j)

        print("The matrix is a %sx%s matrix with the ff elements"%(len(self._matrix),len(self._matrix)))
        for a in range(i):
            for b in range(j):
                print(self._matrix[a][b],end='\t')
            print('\n')
        print("The vector after elimination is below\n")
        for d in self.vector:
            print(d,end='\n')
    def getAnswer(self):
        """Prints the solution of the system of linear equations. 
           It takes zero arguments.
        """
        sum = 0
        x = []
        for n in range(len(self._matrix)):
            x.append(0)
        m = len(self._matrix)
        x[len(self._matrix)-1] = self.vector[m-1]/self._matrix[m-1][m-1]
        i = len(self._matrix)-2
        while i >= 0:
            sum = self.vector[i]
            for j in range(i+1,len(self._matrix)):
                sum -= self._matrix[i][j]*x[j]
            x[i] = sum/self._matrix[i][i]
            i -= 1
        for a in x:
            print(a,end='\n')
#testing the module
if __name__ == "__main__":
    mat = EquationsSolver([2,1,2,5],[1,6,4,0],[4,8,5,1],vector=[6,10,26,35])
    mat.eliminate()
    mat.show()
    mat.getAnswer()



        


