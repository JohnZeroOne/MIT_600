# Problem Set 7: Simulating the Spread of Disease and Virus Population Dynamics 
# Name: John Smith
# Collaborators:
# Time: 20m

import numpy as np
import random
import pylab
import matplotlib.pyplot as plt

''' 
Begin helper code
'''

class NoChildException(Exception):
    """
    NoChildException is raised by the reproduce() method in the SimpleVirus
    and ResistantVirus classes to indicate that a virus particle does not
    reproduce. You can use NoChildException as is, you do not need to
    modify/add any code.
    """

'''
End helper code
'''

#
# PROBLEM 1
#
class SimpleVirus(object):

    """
    Representation of a simple virus (does not model drug effects/resistance).
    """
    def __init__(self, maxBirthProb, clearProb):

        """
        Initialize a SimpleVirus instance, saves all parameters as attributes
        of the instance.        
        maxBirthProb: Maximum reproduction probability (a float between 0-1)        
        clearProb: Maximum clearance probability (a float between 0-1).
        """

        # ensure entry is within bounds
        assert isinstance(maxBirthProb, float)
        assert maxBirthProb > 0.00 and maxBirthProb < 1.00
        assert isinstance(clearProb, float)
        assert clearProb < 1.00 and clearProb > 0.00
        # instances
        self.maxBirthProb = maxBirthProb
        self.clearProb = clearProb

    def doesClear(self):

        """ Stochastically determines whether this virus particle is cleared from the
        patient's body at a time step. 
        returns: True with probability self.clearProb and otherwise returns
        False.
        """

        # decide if the virus clears
        if self.clearProb >= 0.50:
            return True
        return False
    
##      stochastic = random.random()
##      print stochastic
##      if stochastic >= 0.50:
##          return True
##      return False
    
    def reproduce(self, popDensity):

        """
        Stochastically determines whether this virus particle reproduces at a
        time step. Called by the update() method in the SimplePatient and
        Patient classes. The virus particle reproduces with probability
        self.maxBirthProb * (1 - popDensity).
        
        If this virus particle reproduces, then reproduce() creates and returns
        the instance of the offspring SimpleVirus (which has the same
        maxBirthProb and clearProb values as its parent).         

        popDensity: the population density (a float), defined as the current
        virus population divided by the maximum population.         
        
        returns: a new instance of the SimpleVirus class representing the
        offspring of this virus particle. The child should have the same
        maxBirthProb and clearProb values as this virus. Raises a
        NoChildException if this virus particle does not reproduce.               
        """

        # calculate probability
        probability = self.maxBirthProb*(1-popDensity)
        # create a new instance of virus with calculated probability
        SimpleVirus(random.random(), probability)

class SimplePatient(object):

    """
    Representation of a simplified patient. The patient does not take any drugs
    and his/her virus populations have no drug resistance.
    """    

    def __init__(self, viruses, maxPop):

        """

        Initialization function, saves the viruses and maxPop parameters as
        attributes.

        viruses: the list representing the virus population (a list of
        SimpleVirus instances)

        maxPop: the  maximum virus population for this patient (an integer)
        """

        self.viruses = viruses
        self.maxPop = maxPop

    def getTotalPop(self):

        """
        Gets the current total virus population. 
        returns: The total virus population (an integer)
        """
        virus_count = 0
        
        for virus in self.viruses:
            virus_count += 1

        return virus_count

    def update(self):

        """
        Update the state of the virus population in this patient for a single
        time step. update() should execute the following steps in this order:
        
        - Determine whether each virus particle survives and updates the list
        of virus particles accordingly.   
        - The current population density is calculated. This population density
          value is used until the next call to update() 
        - Determine whether each virus particle should reproduce and add
          offspring virus particles to the list of viruses in this patient.                    

        returns: The total virus population at the end of the update (an
        integer)
        """
        # bad practice, use helper variables
        for virus in enumerate(self.viruses[:]):
            if self.doesclear:
                self.viruses.remove(virus)
                
        for virus in self.viruses:
            self.reproduce(self.popDensity)
            
        virus_count = 0
        for virus in self.viruses:
            virus_count += 1

        return virus_count      

#
# PROBLEM 2
#
def simulationWithoutDrug():

    """
    Run the simulation and plot the graph for problem 2 (no drugs are used,
    viruses do not have any drug resistance).    
    Instantiates a patient, runs a simulation for 300 timesteps, and plots the
    total virus population as a function of time.    
    """

    SimpleVirus(0.1, 0.05)
    viruses = 100 * [SimpleVirus]
    SimplePatient(viruses, 1000)

    for i in range(300):
        self.update()
        plt.plot(i)
        plt.ylabel('Total virus population')
        plt.xlabel('Time step')
        plt.show()
    
