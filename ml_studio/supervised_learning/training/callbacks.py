# %%
# =========================================================================== #
#                                  CALLBACKS                                  #
# =========================================================================== #
# =========================================================================== #
# Project: ML Studio                                                          #
# Version: 0.1.14                                                             #
# File: \callbacks.py                                                         #
# Python Version: 3.8.0                                                       #
# ---------------                                                             #
# Author: John James                                                          #
# Company: Decision Scients                                                   #
# Email: jjames@decisionscients.com                                           #
# ---------------                                                             #
# Create Date: Monday August 19th 2019, 7:36:03 pm                            #
# Last Modified: Saturday November 30th 2019, 10:35:55 am                     #
# Modified By: John James (jjames@decisionscients.com)                        #
# ---------------                                                             #
# License: Modified BSD                                                       #
# Copyright (c) 2019 Decision Scients                                         #
# =========================================================================== #

"""Module containing functionality called during the training process.

Note: The CallbackList and Callback abstract base classes were inspired by
the Keras implementation.  
"""
import abc as ABC
from collections import deque
import datetime
import numpy as np
import types
# --------------------------------------------------------------------------- #
#                             CALLBACK LIST                                   #
# --------------------------------------------------------------------------- #
class CallbackList(object):
    """Container of callbacks."""

    def __init__(self, callbacks=None):
        """CallbackList constructor
        
        Parameters
        ----------
        callbacks : list
            List of 'Callback' instances.        
        """
        callbacks = callbacks or []
        self.callbacks = [c for c in callbacks]        
        self.params = {}
        self.model = None

    def append(self, callback):
        """Appends callback to list of callbacks.
        
        Parameters
        ----------
        callback : Callback instance            
        """
        self.callbacks.append(callback)

    def set_params(self, params):
        """Sets the parameters variable, and in list of callbacks.
        
        Parameters
        ----------
        params : dict
            Dictionary containing model parameters
        """
        self.params = params
        for callback in self.callbacks:
            callback.set_params(params)

    def set_model(self, model):
        """Sets the model variable, and in the list of callbacks.
        
        Parameters
        ----------
        model : Estimator or subclass instance 
        
        """
        self.model = model
        for callback in self.callbacks:
            callback.set_model(model)

    def on_batch_begin(self, batch, logs=None):
        """Calls the `on_batch_begin` methods of its callbacks.

        Parameters
        ----------
        batch : int
            Current training batch

        logs: dict
            Currently no data is set to this parameter for this class. This may
            change in the future.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_batch_begin(batch, logs)

    def on_batch_end(self, batch, logs=None):
        """Calls the `on_batch_end` methods of its callbacks.
        
        Parameters
        ----------
        batch : int
            Current training batch
        
        logs: dict
            Dictionary containing the data, cost, batch size and current weights
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_batch_end(batch, logs)

    def on_epoch_begin(self, epoch, logs=None):
        """Calls the `on_epoch_begin` methods of its callbacks.

        Parameters
        ----------        
        epoch: integer
            Current training epoch

        logs: dict
            Currently no data is passed to this argument for this method
            but that may change in the future.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_epoch_begin(epoch, logs)

    def on_epoch_end(self, epoch, logs=None):
        """Calls the `on_epoch_end` methods of its callbacks.
        This function should only be called during train mode.

        Parameters
        ----------
        epoch: int
            Current training epoch
        
        logs: dict
            Metric results for this training epoch, and for the
            validation epoch if validation is performed.
        """
        logs = logs or {}
        for callback in self.callbacks:
            callback.on_epoch_end(epoch, logs)

    def on_train_begin(self, logs=None):
        """Calls the `on_train_begin` methods of its callbacks.

        Parameters
        ----------
        logs: dict
            Currently no data is passed to this argument for this method
                but that may change in the future.
        """
        for callback in self.callbacks:
            callback.on_train_begin(logs)

    def on_train_end(self, logs=None):
        """Calls the `on_train_end` methods of its callbacks.

        Parameters
        ----------
        logs: dict
            Currently no data is passed to this argument for this method
                but that may change in the future.
        """
        for callback in self.callbacks:
            callback.on_train_end(logs)

    def __iter__(self):
        return iter(self.callbacks)

# --------------------------------------------------------------------------- #
#                             CALLBACK CLASS                                  #
# --------------------------------------------------------------------------- #
class Callback(object):
    """Abstract base class used to build new callbacks."""
    def __init__(self):
        """Callback class constructor."""
        self.params = None
        self.model = None

    def set_params(self, params):
        """Sets parameters from estimator.

        Parameters
        ----------
        params : dict
            Dictionary containing estimator parameters
        """ 
        self.params = params

    def set_model(self, model):
        """Stores model in Callback object.

        Parameters
        ----------
        model : Estimator
            Estimator object
        """
        self.model = model

    def on_batch_begin(self, batch, logs=None):
        """Logic executed at the beginning of each batch.

        Parameters
        ----------
        batch : int
            Current training batch
        
        logs: dict
            Dictionary containing the data, cost, batch size and current weights
        """        
        pass

    def on_batch_end(self, batch, logs=None):   
        """Logic executed at the end of each batch.
        
        Parameters
        ----------
        batch : int
            Current training batch
        
        logs: dict
            Dictionary containing the data, cost, batch size and current weights
        """                
        pass

    def on_epoch_begin(self, epoch, logs=None):
        """Logic executed at the beginning of each epoch.
        
        Parameters
        ----------
        epoch : int
            Current epoch
        
        logs: dict
            Dictionary containing the data, cost, batch size and current weights
        """                
        pass

    def on_epoch_end(self, epoch, logs=None):
        """Logic executed at the end of each epoch.
        
        Parameters
        ----------
        epoch : int
            Current epoch
        
        logs: dict
            Dictionary containing the data, cost, batch size and current weights
        """                      
        pass

    def on_train_begin(self, logs=None):
        """Logic executed at the beginning of training.
        
        Parameters
        ----------        
        logs: dict
            Dictionary containing the data, cost, batch size and current weights
        """                      
        pass

    def on_train_end(self, logs=None):
        """Logic executed at the end of training.
        
        Parameters
        ----------        
        logs: dict
            Dictionary containing the data, cost, batch size and current weights
        """               
        pass
