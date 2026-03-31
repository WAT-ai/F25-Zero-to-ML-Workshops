# Workshop 9: Reinforcement Learning Basics

_Implement RL algorithms and watch agents learn from scratch!_

## Overview

Reinforcement Learning (RL) is how agents learn to make decisions by interacting with an environment and receiving rewards. In this workshop, you'll implement three classic RL algorithms — from the simplest bandit problem to tabular Q-Learning and SARSA — and develop intuition for key RL concepts like exploration vs exploitation, on-policy vs off-policy learning, and Q-value estimation.

### What You'll Learn

- **Exploration vs Exploitation**: The core trade-off in RL, via the multi-armed bandit
- **Q-Learning**: Off-policy temporal difference control on FrozenLake
- **Deep Q-Networks (DQN)**: Replace the Q-table with a neural network to handle continuous state spaces
- **Policy & Value Visualisation**: Inspect the learned policy and state-value function V(s)
- **Gymnasium**: The standard Python library for RL environments

### Workshop Structure

1. **PDF**: Reinforcement Learning concepts
   - States, actions, rewards, and policies
   - Bellman equations and value functions
   - Overview of tabular RL methods
2. **Notebook**: Implementing RL algorithms
   - **Part 1** — Multi-Armed Bandit: epsilon-greedy exploration
   - **Part 2** — Q-Learning on FrozenLake: tabular Q-learning with decaying epsilon, policy & value visualisation, slippery ice variant
   - **Part 3** — Deep Q-Network on CartPole: neural network as Q-function, replay buffer, target network

## Setup Instructions

### Step 1: Create Virtual Environment
```bash
python -m venv rl-env

source rl-env/bin/activate  # On Windows: rl-env\Scripts\activate
```

### Step 2: Install Dependencies
```bash
pip install numpy matplotlib jupyter gymnasium torch

```

Then open the `rl_workshop.ipynb` notebook.

## Troubleshooting

### Package Installation Issues
**Installation fails**
- Ensure virtual environment is activated
- Try upgrading pip: `pip install --upgrade pip`

**Import errors**
- Verify you're using the correct kernel in Jupyter
- Restart the kernel if you just installed packages
- Check installation: `python -c "import gymnasium; print(gymnasium.__version__)"`

### Algorithm Issues
**Agent not learning / win rate stays near 0**
- Check that your Q-update is implemented correctly (target vs current Q value)
- Try increasing `n_episodes` — some environments need more training
- Verify epsilon is decaying and not staying at 1.0

**DQN not learning / loss exploding**
- Check your replay buffer sampling — ensure you're sampling random batches, not sequential transitions
- Verify the target network is updated periodically, not every step
- Try reducing the learning rate or clipping gradients

### Next Steps
After this workshop, you'll be ready to:
- Learn about policy gradient methods and actor-critic algorithms (used in RLHF for LLMs)
- Try more Gymnasium environments: `MountainCar-v0`, `LunarLander-v3`, Atari games

## When You're Done

```bash
deactivate

git checkout main
```
