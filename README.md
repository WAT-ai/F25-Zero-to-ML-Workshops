# Workshop 9: Reinforcement Learning Basics

_Implement RL algorithms and watch agents learn from scratch!_

## Overview

Reinforcement Learning (RL) is how agents learn to make decisions by interacting with an environment and receiving rewards. In this workshop, you'll implement three classic RL algorithms — from the simplest bandit problem to tabular Q-Learning and SARSA — and develop intuition for key RL concepts like exploration vs exploitation, on-policy vs off-policy learning, and Q-value estimation.

### What You'll Learn

- **Exploration vs Exploitation**: The core trade-off in RL, via the multi-armed bandit
- **Q-Learning**: Off-policy temporal difference control on FrozenLake
- **SARSA**: On-policy TD control and how it differs from Q-Learning
- **Policy Visualisation**: Inspect what your agent has actually learned
- **Gymnasium**: The standard Python library for RL environments

### Workshop Structure

1. **PDF**: Reinforcement Learning concepts
   - States, actions, rewards, and policies
   - Bellman equations and value functions
   - Overview of tabular RL methods
2. **Notebook**: Implementing RL algorithms
   - **Part 1** — Multi-Armed Bandit (30 min): epsilon-greedy exploration
   - **Part 2** — Q-Learning on FrozenLake (45 min): tabular Q-learning with decaying epsilon
   - **Part 3** — SARSA vs Q-Learning on CliffWalking (15 min): on-policy vs off-policy comparison

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

**Q-Learning and SARSA look the same**
- Make sure SARSA uses `Q[next_state, next_action]` (actual next action) not `max Q[next_state]`

### Next Steps
After this workshop, you'll be ready to:
- Explore Deep Q-Networks (DQN), which replace the Q-table with a neural network
- Learn about policy gradient methods and actor-critic algorithms
- Try more Gymnasium environments: `CartPole-v1`, `MountainCar-v0`, `LunarLander-v3`

## When You're Done

```bash
deactivate

git checkout main
```
