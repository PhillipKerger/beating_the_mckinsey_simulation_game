# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 22:42:43 2022

@author: phillips_pc
"""

import numpy as np
import copy as cp

class Organism(): 
    '''
    This is the main class for Organisms, which have the following attributes:
        name: string, name of the organism
        needs: calories needed
        provides: calories provided
        prey: list of strings, names of the prey organisms of this organism
        ate: number of calories it has eaten (0 when initialized)
        got_eaten: number of calories of this organism that have been eaten (0 when initialized)
    
    
    Add the data the following way: orgtype.append(Organism('name', needs, provides, prey))
    'None' as prey indicates a producer (it's the default, so just don't pass anything in that case)
    
    example:    
    preds.append(Organism('squid', 2000, 3000, ['algae', 'sardine', 'sponge'])))
    
    '''
    def __init__(self, name, needs = None, provides = None, prey = None):
        self.name = name
        self.needs = needs
        self.provides = provides
        self.ate = 0
        self.got_eaten = 0
        self.prey = prey


def sort_by_cals_provided(orgs):
    #sort organisms by eating order
    is_sorted = False
    while is_sorted == False:
        is_sorted = True
        for i in range(len(orgs)-1):
            if orgs[i].provides < orgs[i+1].provides:
                [orgs[i], orgs[i+1]] = [orgs[i+1], orgs[i]]
                is_sorted = False
    return orgs

def simulate(orgs, verbose = 0):
    '''
    This function simulates the ecosystem for one round with the selected list of organisms.

    Parameters
    ----------
    orgs : list whose entries are Organism objects. 

    Returns
    -------
    The number of excess calories in the system at the end if no organism went extinct, 
    or -1 if a species went extinct.

    '''
    #sort orgs by eating order (so by calories provided -- does the eating order actually matter though?)
    orgs = sort_by_cals_provided(orgs)
    if verbose > 0: 
        print('\n')
        for k in range(len(orgs)):
            print(orgs[k].name)
    for i in range(len(orgs)):
        eater = orgs[i]; 
        #skip if producer
        if eater.prey == None: 
            continue
        if verbose > 0: 
            print(eater.name, 'is eating.')
        #find indices of two possible preys
        prey1 = None
        prey2 = None
        
        preyinds = []
        for j in range(len(orgs)):
            if orgs[j].name in eater.prey:
                preyinds.append(j)
        
        
        maxprov1 = 0
        prey1ind = None
        for j in preyinds:
            if (orgs[j].provides-orgs[j].got_eaten)> maxprov1:
                maxprov1 = orgs[j].provides-orgs[j].got_eaten
                prey1ind = j
                
        maxprov2 = 0
        prey2ind = None
        for j in preyinds:
            if (orgs[j].provides-orgs[j].got_eaten)> maxprov2 and j != prey1ind:
                maxprov2 = orgs[j].provides-orgs[j].got_eaten
                prey2ind = j
        
        if maxprov1 > maxprov2: 
            prey2ind = None
        
        if not(prey1ind==None):
            prey1 = orgs[prey1ind]
        else:
            if verbose > -1:
                print('Failure; no prey for a predator.')
            return -1
        
        #if theres only one prey option
        if prey2ind == None: 
                #eat prey 1
                prey1.got_eaten += eater.needs
                eater.ate += eater.needs
                if verbose > 0:
                    print(eater.name, 'ate', eater.needs, 'calories of', prey1.name,'.')
            
        #if there are two prey options
        else: 
            prey2 = orgs[prey2ind]
            #check if they provide equal cals
            if (prey1.provides-prey1.got_eaten == prey2.provides-prey2.got_eaten): #eat from them equally in this case
                prey1.got_eaten += eater.needs/2
                prey2.got_eaten += eater.needs/2
                eater.ate += eater.needs
                if verbose > 0:
                    print(eater.name, 'ate', eater.needs/2, 'calories of', prey1.name,'.')
                    print(eater.name, 'ate', eater.needs/2, 'calories of', prey2.name,'.')
            else: #prey1 provides more
                prey1.got_eaten += eater.needs
                eater.ate += eater.needs
                if verbose > 0:
                    print(eater.name, 'ate', eater.needs, 'calories of', prey1.name,'.')
        #check if someone went extinct
        if prey1.got_eaten >= prey1.provides:
            if verbose > -1:
                print('Failure;', prey1.name,'was eaten to extinction.')
            return -1
        if not(prey2 == None) and prey2.got_eaten >= prey2.provides:
            if verbose > -1:
                print('Failure;', prey1.name,'was eaten to extinction.')
            return -1
    
    excess_cals = 0
    for i in range(len(orgs)):
        excess_cals += orgs[i].provides - orgs[i].got_eaten
    if excess_cals > 0:
        if verbose > -1:
            print('\nSuccess, with', excess_cals, 'cal excess.')
            print('Organisms used:')
            for i in range(len(orgs)):
                print(orgs[i].name)
            print(' ')
    return excess_cals 


def find_opt(apexs, preds, provs, orgsplit,
             strategy = 'random search', max_iter = 10000, verbose = 0):
    '''
    This function tries to find the best organism choice for the ecosystem game. 
    Input organisms are separated by apex predators, predators, and producers. 
    Anything not a producer or apex predator (eaten by None) should be a 'predator',
    though this only matters for the orgsplit argument. 

    Parameters
    ----------
    apexs : List of Organisms
        List of the apex predators available.
    preds : List of Organisms
        List of the predators (non-apex) available
    provs : List of Organisms
        List of providers (zero cals needed)
    orgsplit : List of length 3 of integers
        how many of each [apex, preds, provs]. 
        Needs to add up to however many organisms we're supposed to have. 
        This should be chosen intelligently (e.g. 1 apex predator, 4 predators, 3 producers could be reasonable)
    strategy : string, optional
        Say which strategy we want to use to find the optimum. 
        The default is 'random search', and nothing else has been coded yet. 
        Blind RS is sufficient as the search space is pretty small, so no need to do anything complex, 
        as of the state of the game 11/18/2022.

    Returns
    -------
    the optimal choice of organisms given the chosen split, 
    of those tested, wrt to maximizing excess calories left in the system after the feeding is done. 
    '''
    #grab the number of apex, predator, and provider organisms we want 
    apexnum = orgsplit[0]
    prednum = orgsplit[1]
    provnum = orgsplit[2]
    
    feas_orgs = []
    
    count = 0
    maxob = -1
    best_orgs = None
    
    while count < max_iter:
        #grab random Organism indices (sampling without replacement)
        apexinds = np.random.choice(np.arange(len(apexs), dtype = int),size = (apexnum), replace = False)
        predinds = np.random.choice(np.arange(len(preds), dtype = int), size = (prednum),replace = False)
        provinds = np.random.choice(np.arange(len(provs), dtype = int), size = (provnum),replace = False)
    
        apex_orgs = [apexs[i] for i in apexinds]
        pred_orgs = [preds[i] for i in predinds]
        prov_orgs = [provs[i] for i in provinds]
        orgs = apex_orgs+pred_orgs+prov_orgs
       
        obval = simulate(cp.deepcopy(orgs), verbose = verbose)
        
        if obval > 0:
            feas_orgs.append(orgs.copy())
            if obval > maxob:
                maxob = obval
                best_orgs = orgs.copy()
        count +=1
    return [feas_orgs, best_orgs, maxob]