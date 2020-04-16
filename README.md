# Reinforcement Learning 
## Implementations of Common AI Algorithms used in RL. 
##### This codebase is an implementation of the algorithms discussed in the 'Reinforcement Learning' course by David Silver. Notes from the course are recorded in this README document.

## What is Reinforcement Learning?
Unlike supervised learning, where each training data point is tagged with a 'correct' answer, reinforcement learning agents dont have a set of training data tagged with labels.

Instead, an agent takes a series of **actions** through an environment and gets a series of signals that tells it how well its doing. These signals are called **rewards**, and the goal of any RL agent is to learn a series of actions that maximize the total reward through an environment.

An aspect unique to RL is it's temporal notion of time. An agent starts at an initial **state** and at each timestemp takes an action which moves it into a new **state**. Examples:

    1. Moving a chess piece, changes the state of a game board
    2. Investing 10,000 in the market changes the state of your portfolio from cash to company stock. 

