# =========================================================================== #
#                                VALIDITY                                     #
# =========================================================================== #
# =========================================================================== #
# Project: Visualate                                                          #
# Version: 0.1.0                                                              #
# File: \model_validation.py                                                  #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Thursday November 28th 2019, 1:49:18 pm                        #
# Last Modified: Thursday November 28th 2019, 1:50:37 pm                      #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2019 Decision Scients                                         #
# =========================================================================== #
"""Model validation and verification module.""" 
#%%
import numpy as np
# --------------------------------------------------------------------------- #
#                                 LEVERAGE                                    #
# --------------------------------------------------------------------------- #
def leverage(X):
    """Computes leverage.

    Leverage is a measure of how far away an independent variable values of an 
    observation are from those of other observations.

    The formula is:
    ..math::
        h_{ii} = [\mathbb{H}]_{ii}, where
        H = X(X^TX)^{-1}X^T
    """
    hat = X.dot(np.linalg.inv(X.T.dot(X)).dot(X.T)) 
    hii = np.diagonal(hat)
    return hii
print(leverage.__doc__)

# --------------------------------------------------------------------------- #
#                           RESIDUAL ANALYSIS                                 #
# --------------------------------------------------------------------------- #
def standardized_residuals(model, X, y, return_predictions=False):
    """Computes standardized residuals.

    Standardized residuals (sometimes referred to as "internally studentized 
    residuals") are defined for each observation, i = 1, ..., n as an 
    ordinary residual divided by an estimate of its standard deviation:
    ..math:: r_i = \\frac{e_i}{\\sqrt{MSE(1-h_{ii})}}

    Parameters
    ----------
    model : Estimator or BaseEstimator
        ML Studio or Scikit Learn estimator

    X : ndarray or DataFrame of shape n x m
        A matrix of n instances with m features

    y : ndarray or Series of length n
        An array or series of target or class values 
    """
    # Compute residuals
    y_pred = model.predict(X)
    residuals = y - y_pred
    
    # Compute Leverage
    leverage = (X * np.linalg.pinv(X).T).sum(1)
    
    # Compute degrees of freedom and MSE
    rank = np.linalg.matrix_rank(X)
    df = X.shape[0] - rank
    mse = np.dot(residuals, residuals) / df

    # Calculate standardized 
    standardized_residuals = residuals / np.sqrt(mse) * np.sqrt(1-leverage)        
    
    # Return standardized residuals and optionally the predictions
    if return_predictions:
        return standardized_residuals, y_pred
    else:
        return standardized_residuals

def studentized_residuals(model, X, y, return_predictions=False):
    """Computes studentized residuals.

    Studentized residuals are just a deleted residual divided by its estimated
    standard deviation. This turns out to be equivalent to the ordinary residual
    divided by a factor that includes the mean square error based on the 
    estimated model with the ith observation deleted, MSE(i), and the leverage, hii
    .. math:: r_i = \\frac{e_i}{\\sqrt{MSE_{(i)}(1-h_{ii})}}

    Parameters
    ----------
    model : Estimator or BaseEstimator
        ML Studio or Scikit Learn estimator

    X : ndarray or DataFrame of shape n x m
        A matrix of n instances with m features

    y : ndarray or Series of length n
        An array or series of target or class values 
    """
    # Compute residuals
    y_pred = model.predict(X)
    residuals = y - y_pred
    
    # Compute Leverage
    leverage = (X * np.linalg.pinv(X).T).sum(1)
    
    # Compute degrees of freedom and MSE
    rank = np.linalg.matrix_rank(X)
    df = X.shape[0] - rank
    mse = np.dot(residuals, residuals) / df

    # Calculate studentized residuals 
    studentized_residuals = residuals / np.sqrt(mse) * np.sqrt(1-leverage)

    # Return studentized residuals and optionally the predictions
    if return_predictions:
        return studentized_residuals, y_pred
    else:
        return studentized_residuals   
    

# %%