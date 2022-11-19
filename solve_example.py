# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 13:07:20 2022

@author: kerge
"""

import mckinsey_game_lib as mk


apexs = [] #list of apex predators
preds = [] #list of predators (any non-producer that is eaten by someone else)
prods = [] #list of producers

#FORMAT: mk.Organism('name', cals_needed, cals_provided, prey =['prey1', 'prey2', ...])
#Example:
#apexs.append(mk.Organism('tiger', 1000, 4000, prey = ['algae', 'turtle']))
#apexs.append(mk.Organism('', prey = []))
apexs.append(mk.Organism('bananafish',2100, 1750, prey = ['reef_chocobo', 'eren_jaeger_turtle', 'ringo_seastar']))
apexs.append(mk.Organism('india_pale_whale',2600, 2500, prey = ['uwu_fish','jack_edmonds_crab']))
apexs.append(mk.Organism('TORNADOxSHARK',2022, 3100, prey = ['eren_jaeger_turtle']))

#preds.append(mk.Organism('', prey = []))
preds.append(mk.Organism('uwu_fish',4100, 2400, prey = ['sponge','algae','coral']))
preds.append(mk.Organism('eren_jaeger_turtle',4300, 666, prey = ['algae']))
preds.append(mk.Organism('woomy_octopus',3900, 3300, prey = ['algae']))
preds.append(mk.Organism('epona_the_seahorse', 3100, 1776, prey = ['algae','woomy_octopus' ]))
preds.append(mk.Organism('reef_chocobo',3000, 3250, prey = ['uwu_fish','eren_jaeger_turtle',
                                                          'algae', 'sponge']))
preds.append(mk.Organism('jack_edmonds_crab',3290,420, prey = ['coral']))
preds.append(mk.Organism('ringo_seastar',1300, 2800, prey = ['epona_the_seahorse','reef_chocobo' ]))


#prods.append(mk.Organism('algae', 0, 2000))
#prods.append(mk.Organism('', ))
prods.append(mk.Organism('sponge', 0, 4200))
prods.append(mk.Organism('algae', 0, 4100))
prods.append(mk.Organism('coral', 0, 6000))

#reasonable ways to split number of apexs, preds, prods 
orgsplits = [[2,3,3], [1,4,3], [2,4,2], [3, 3, 2]]

#increase max_iter if you want to use more computation time, but this does the job.
for split in orgsplits:
    [feasibles, bestorgs, max_ob] = mk.find_opt(apexs, preds, prods, split,
             strategy = 'random search', max_iter = 10000, verbose = -1)

    if bestorgs == None:
        print('\nFailure with orgsplit', split)
    else:
        print('\nSuccess with orgsplit', split)
        
        print('\nHere is what happened with the best combo:')
        mk.simulate(bestorgs, verbose = 1)



    
    
    
    
    
    
    
    
    
    
    

