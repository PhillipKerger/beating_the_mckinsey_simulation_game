# beating_the_mckinsey_simulation_game
Python code that beats the McKinsey PSG simulation provided by MConsulting Prep. <br>

This code finds a solution to the ecosystem portion of the McKinsey PSG simulation, provided by MConsulting Prep, upon the user inputting a list organisms to choose from. 
<br>
The McKinsey PSG simulation game, provided by MConsulting Prep, is a fun video game, the first portion of which consists of creating an ecosystem of various organisms that can survive all together. There is a tutorial that spells out the rules to the game, which are implemented in mkinsey_game_lib.py's simulate function. The find_opt function then can search for the best combination of organisms out of the given input list (with respect to excess calories in the system at the end). Details are spelled out in the code. The user needs to only pick a part of the ecosystem that is habitable to many organisms, and then input the organism data of those organisms that can survive in the chosen location. The user also chooses some 'splits' of how many apex predators, regular predators, and producer organisms should be considered. The code succeeds in fingding the optimal solutions (wrt to excess calories) in the simulation game. 
<br>
mckinsey_sim_game_lib.py contains useful functions for winning the simulation game. <br>
solve_example.py provides an example of how the data should be input in order to find a solution.
solve_template.py provides a useful template for easily inputting the data. 
<br>
<br>
This code is to be used purely for the purpose of having fun in the video game McKinsey PSG Simulation by MConsulting Prep, which should not be confused with the McKinsey Problem Solving Game that is given to McKinsey applicants. 
