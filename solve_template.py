# -*- coding: utf-8 -*-
"""
A template for beating the McKinsey assessment game. 
Just fill in the data and run. 
You need to choose organisms that can all live in the same ecosystem though, 
since this does not account for that. 
"""

import mckinsey_game_lib as mk


apexs = []
preds = []
prods = []

#FORMAT: mk.Organism('name', cals_needed, cals_provided, prey =['prey1', 'prey2', ...])
#apexs.append(mk.Organism('tiger', 1000, 4000, prey = ['algae', 'turtle']))
#apexs.append(mk.Organism(, prey = []))
apexs.append(mk.Organism('', prey = []))
apexs.append(mk.Organism('', prey = []))
apexs.append(mk.Organism('', prey = []))
apexs.append(mk.Organism('', prey = []))

#preds.append(mk.Organism('', prey = []))
preds.append(mk.Organism('', prey = []))
preds.append(mk.Organism('', prey = []))
preds.append(mk.Organism('', prey = []))
preds.append(mk.Organism('', prey = []))
preds.append(mk.Organism('', prey = []))
preds.append(mk.Organism('', prey = []))

#prods.append(mk.Organism('algae', 0, 2000))
#prods.append(mk.Organism(''))
prods.append(mk.Organism('',))
prods.append(mk.Organism('',))
prods.append(mk.Organism('',))


#reasonable ways to split number of apexs, preds, prods 
#Example if 8 organisms are needed: 
#orgsplits = [[2,3,3], [1,4,3], [2,4,2], [3, 3, 2]]
orgsplits = [[ , , ], [ , , ], [ , , ], [ , , ]]

#increase max_iter if you want to use more computation time, but this does the job.
for split in orgsplits:
    [feasibles, bestorgs, max_ob] = mk.find_opt(apexs, preds, prods, split,
             strategy = 'random search', max_iter = 20000, verbose = -1)

    if bestorgs == None:
        print('\nFailure with orgsplit', split)
    else:
        print('\nSuccess with orgsplit', split)
        print('The best organism combination was:')
        for i in range(len(bestorgs)):
            print(bestorgs[i].name)
        print('with', max_ob, 'excess calories at the end.')
        
        print('\nHere is what happened with the best combo:')
        mk.simulate(bestorgs, verbose = 1)

    
    
    
    
    
    
    
    
    
    
    

