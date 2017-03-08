"""
Some utility functions

- RMSE

"""


def root_mean_square_error(observed, modelled):
    """
    Root Mean Square Error (RMSE)

    Parameters
    -----------
    observed : np.ndarray or pd.DataFrame
        observed/measured values of the variable
    observed : np.ndarray or pd.DataFrame
        simulated values of the variable

    Notes
    -------
    * range: [0, inf]
    * optimum: 0
    """
    residuals = observed - modelled
    return np.sqrt((residuals**2).mean())
