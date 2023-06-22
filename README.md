# AI_
`In Lab_01`:                                                                                                                                            

In this we have implement two methods –Gradient Descent method and Newton’s method for function minimalization(please, be aware that the user should have a possibility to select which method will be takenfor function minimalization).
 With case of stopping conditions
 {
•Maximum number of iterations
•Desiredvalue 𝐹(𝑥)or 𝐺(𝑥)to  reach(so  the  processis  finished  when 𝐹(𝑥)≥𝑣𝑎𝑙𝑢𝑒_𝑡𝑜_𝑟𝑒𝑎𝑐ℎ/ 𝐺(𝑥)≥𝑣𝑎𝑙𝑢𝑒_𝑡𝑜_𝑟𝑒𝑎𝑐ℎ)
•Maximum computation time
 }
 
 
 `In Lab_02`:
 
 
 In this we have implementation must have the following componentsand fulfil the following requirements:
 •Roulette-wheel selection with scaling
 •Single point crossover
 •FIFO replacement strategy
 •Genetic algorithm must use binary vectors
  The user should also have a possibility to specify diversified parameters of the algorithm. They are as follows:
  •The problem dimensionality
  •The range of searched integers as 𝑑≥1that for each dimension i, −2^d≤𝑥(i)<2^d
  •Function parameters A, b, c
  •The algorithm parameters as: population size, crossover probability, mutation probability, number of algorithms iterations
  
  `In Lab_03`:
  
  Program that plays tic-tac-toe with the user on a 3×3board. The game continues until one of the players wins or it is a draw. The first player to get 3 of his/her marks in a row (up, down, across, or diagonally)wins.
  `Algorithm: min-max with alpha-beta pruning.` 
  
  `Lab_04`:
  `Solve  problems using Prolog.`
  Convert an input number N to English words. N <= 1000
  `Example:`
 ` ?- to_words(45)
 "forty five"
 ?- to_words(394)
 "three hundred and ninety four"`

 `lab_05`:
 Create an implementation of the Q-Learning algorithm to solve a toy Reinforcement Learning problem. Use
the environment provided from OpenAI gym library. The original gym library is no longer updated, however,
there is a continued development on a fork of gym called gymnasium. We use gymnasium for this exercise.
Use the following environments for each lab variants:
1. `Taxi. Use "Taxi-v3"`
2. ` FrozenLake. Use the arguments "FrozenLake-v1" and map_name="8x8" for gym.make()`
Read each environment documentation to learn the problem, how to reach the goal, what are the possible
actions, what states to observe, rewards and termination conditions.


  
