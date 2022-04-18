import matplotlib.pyplot as plt

class Newton:
    # Class to solve polynom interpolation problems using Newton's polynomial
    # interpolation
    def __init__(self, x, y):
        # x -> x-values of dataset
        # y -> y-values of dataset
        # cache -> dictionary to store the calculated values
        self._x = x
        self._y = y
        self._cache = {}
        self._newton(0, len(self._x)-1)

    def _newton(self, j, k):
        # Recursive function to calculate the coefficients used for the method
        # The important values are stored at self._cache[0][j]
        # Each value gets cached.
        # Input are the indices j and k to represent the position of the
        # calculated value in the method

        # Check if value is already cached:
        if not j in self._cache:
            self._cache[j] = {}
        if not k in self._cache[j]:
            if j == k: # Base case
                out = self._y[j]
                # Calculate and cache value if not already happened
            else:
                out = ((self._newton(j+1, k) - self._newton(j, k-1))
                       /(self._x[k] - self._x[j]))
            self._cache[j][k] = out
            # print('j={}, k={}, y={}'.format(j, k, out))
        else:
            out = self._cache[j][k]
        # print('j={}, k={}, f={}'.format(j,k,out))
        return out

    def _solve(self, j, evalp):
        # Class intern function to evaluate the polynom at position evalp
        if j == len(self._cache)-1:
            return self._cache[0][j]
        return self._cache[0][j] + (evalp-self._x[j]) * self._solve(j+1, evalp)

    def solve(self, evalp):
        # Value of evaluated polynomial at position evalp, calculation happens
        # at _solve function
        return self._solve(0, evalp)


    def factors(self):
        # Returns list of coefficients used for the polynomial
        return [self._cache[0][i] for i in range(len(self._cache))]

    def knots(self):
        # returns x-values of dataset
        return self._x

    def values(self):
        # returns y-values of dataset
        return self._y

    def show_data(self):
        # Plots the points of input x- and y-values
        # Matplotlib is necessary for this function
        fig, ax = plt.subplots()
        plt.scatter(self._x, self._y, color='red')
        fig.show()


# Testbench
if __name__ == "__main__":
    x = [-2, -1, 1, 3]
    y = [8, 0, 2, -12]
    result = [8, -8, 3, -1] # Control values
    pipp = Newton(x, y)
    fac = pipp.factors()
    print(fac)
    print('The correct result is:')
    print(result)
    print(50*'-')
    print('Evaluating of x = 2:')
    print(pipp.solve(2))
    print('The correct result is:')
    print('0')
    pipp.show_data()
