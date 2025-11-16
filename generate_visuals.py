"""
Generate all visualizations for the RL Basics Guide
Run this script in the same directory as the markdown file to generate images.
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch, FancyArrowPatch
import seaborn as sns

# Set style for better-looking plots
plt.style.use('seaborn-v0_8-darkgrid')
sns.set_palette("husl")

# Global settings for readability
SMALL_SIZE = 11
MEDIUM_SIZE = 13
LARGE_SIZE = 15

plt.rc('font', size=SMALL_SIZE)
plt.rc('axes', titlesize=LARGE_SIZE, labelsize=MEDIUM_SIZE)
plt.rc('xtick', labelsize=SMALL_SIZE)
plt.rc('ytick', labelsize=SMALL_SIZE)
plt.rc('legend', fontsize=SMALL_SIZE)
plt.rc('figure', titlesize=LARGE_SIZE)


def create_gridworld_example():
    """Create a simple gridworld visualization"""
    fig, ax = plt.subplots(1, 1, figsize=(8, 3.5))

    # 3x6 grid (removed bottom 2 rows)
    grid_height, grid_width = 3, 6

    # Create grid
    for i in range(grid_height + 1):
        ax.plot([0, grid_width], [i, i], 'k-', linewidth=1)
    for j in range(grid_width + 1):
        ax.plot([j, j], [0, grid_height], 'k-', linewidth=1)

    # Fill cells with colors
    # Start position (green) - top row
    start_rect = patches.Rectangle((0, 2), 1, 1, linewidth=2,
                                   edgecolor='darkgreen', facecolor='lightgreen', alpha=0.7)
    ax.add_patch(start_rect)
    ax.text(0.5, 2.5, 'Start', ha='center', va='center', fontsize=13, fontweight='bold')

    # Goal position (gold) - top row
    goal_rect = patches.Rectangle((5, 2), 1, 1, linewidth=2,
                                  edgecolor='darkgoldenrod', facecolor='gold', alpha=0.7)
    ax.add_patch(goal_rect)
    ax.text(5.5, 2.5, 'Goal\n(+10)', ha='center', va='center', fontsize=13, fontweight='bold')

    # Walls (gray) - blocking top middle two squares
    walls = [(2, 2), (3, 2)]
    for x, y in walls:
        wall_rect = patches.Rectangle((x, y), 1, 1, linewidth=1,
                                      edgecolor='black', facecolor='gray', alpha=0.8)
        ax.add_patch(wall_rect)
        ax.text(x + 0.5, y + 0.5, 'Wall\n(-1)', ha='center', va='center',
                fontsize=10, fontweight='bold', color='white')

    # Sample path (blue arrows) - go around the walls
    path = [(0.8, 2.5), (1.5, 2.5), (1.5, 1.5), (2.5, 1.5), (3.5, 1.5),
            (4.5, 1.5), (4.5, 2.5), (5.2, 2.5)]
    for i in range(len(path) - 1):
        arrow = FancyArrowPatch(path[i], path[i+1],
                               arrowstyle='->', mutation_scale=15,
                               linewidth=2, color='#1f77b4', alpha=0.5)
        ax.add_patch(arrow)

    # Add action labels (positioned below the grid with more spacing)
    ax.text(3, -0.4, 'Actions: ↑ (up), ↓ (down), ← (left), → (right)',
            ha='center', fontsize=11, style='italic')

    ax.set_xlim(-0.2, grid_width + 0.2)
    ax.set_ylim(-0.7, grid_height + 0.2)
    ax.set_aspect('equal')
    ax.axis('off')

    plt.tight_layout()
    plt.savefig('gridworld_example.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created gridworld_example.png")


def create_epsilon_greedy_vs_softmax():
    """Compare epsilon-greedy and softmax action selection"""
    # Three actions with different Q-values
    Q_values = np.array([1.0, 2.5, 0.5])
    actions = ['Action 0', 'Action 1', 'Action 2']
    
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    
    # Epsilon-greedy with epsilon=0.1
    epsilon = 0.1
    n_actions = len(Q_values)
    best_action = np.argmax(Q_values)
    
    probs_egreedy = np.ones(n_actions) * (epsilon / n_actions)
    probs_egreedy[best_action] += (1 - epsilon)
    
    colors = ['#ff7f0e', '#2ca02c', '#d62728']
    axes[0].bar(actions, probs_egreedy, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
    axes[0].set_ylabel('Probability', fontsize=12, fontweight='bold')
    axes[0].set_title('Epsilon-Greedy (ε=0.1)', fontsize=13, fontweight='bold')
    axes[0].set_ylim([0, 1])
    axes[0].grid(axis='y', alpha=0.3)
    for i, (a, p) in enumerate(zip(actions, probs_egreedy)):
        axes[0].text(i, p + 0.03, f'{p:.2f}', ha='center', fontsize=11, fontweight='bold')
    
    # Softmax with temperature=0.5
    temp = 0.5
    exp_Q = np.exp(Q_values / temp)
    probs_softmax_low = exp_Q / np.sum(exp_Q)
    
    axes[1].bar(actions, probs_softmax_low, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
    axes[1].set_ylabel('Probability', fontsize=12, fontweight='bold')
    axes[1].set_title('Softmax (τ=0.5, low temp)', fontsize=13, fontweight='bold')
    axes[1].set_ylim([0, 1])
    axes[1].grid(axis='y', alpha=0.3)
    for i, (a, p) in enumerate(zip(actions, probs_softmax_low)):
        axes[1].text(i, p + 0.03, f'{p:.2f}', ha='center', fontsize=11, fontweight='bold')
    
    # Softmax with temperature=2.0
    temp = 2.0
    exp_Q = np.exp(Q_values / temp)
    probs_softmax_high = exp_Q / np.sum(exp_Q)
    
    axes[2].bar(actions, probs_softmax_high, color=colors, alpha=0.7, edgecolor='black', linewidth=1.5)
    axes[2].set_ylabel('Probability', fontsize=12, fontweight='bold')
    axes[2].set_title('Softmax (τ=2.0, high temp)', fontsize=13, fontweight='bold')
    axes[2].set_ylim([0, 1])
    axes[2].grid(axis='y', alpha=0.3)
    for i, (a, p) in enumerate(zip(actions, probs_softmax_high)):
        axes[2].text(i, p + 0.03, f'{p:.2f}', ha='center', fontsize=11, fontweight='bold')
    
    # Add Q-values as text
    fig.text(0.5, 0.02, f'Q-values: {Q_values}', ha='center', fontsize=12, 
             style='italic', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig('epsilon_greedy_vs_softmax.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created epsilon_greedy_vs_softmax.png")


def create_averaging_comparison():
    """Compare simple averaging vs exponential averaging"""
    np.random.seed(42)
    
    # Simulate non-stationary bandit (true value drifts)
    n_steps = 1000
    true_value = np.zeros(n_steps)
    for i in range(n_steps):
        if i < 300:
            true_value[i] = 1.0
        elif i < 600:
            true_value[i] = 1.0 + (i - 300) / 300 * 2.0  # Drift to 3.0
        else:
            true_value[i] = 3.0
    
    # Generate noisy rewards
    rewards = true_value + np.random.randn(n_steps) * 0.5
    
    # Simple averaging
    Q_simple = np.zeros(n_steps)
    count = 0
    for i in range(n_steps):
        count += 1
        Q_simple[i] = Q_simple[i-1] + (1/count) * (rewards[i] - Q_simple[i-1]) if i > 0 else rewards[i]
    
    # Exponential averaging (alpha = 0.1)
    Q_exp = np.zeros(n_steps)
    alpha = 0.1
    for i in range(n_steps):
        Q_exp[i] = Q_exp[i-1] + alpha * (rewards[i] - Q_exp[i-1]) if i > 0 else rewards[i]
    
    # Plot
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    ax.plot(true_value, 'k-', linewidth=2.5, label='True Value', alpha=0.8)
    ax.plot(Q_simple, 'b-', linewidth=2, label='Simple Averaging (1/n)', alpha=0.7)
    ax.plot(Q_exp, 'r-', linewidth=2, label='Exponential Averaging (α=0.1)', alpha=0.7)
    
    ax.axvline(x=300, color='gray', linestyle='--', alpha=0.5, linewidth=1)
    ax.axvline(x=600, color='gray', linestyle='--', alpha=0.5, linewidth=1)
    ax.text(150, 3.35, 'Stationary', ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='gray', linewidth=1))
    ax.text(450, 3.35, 'Drifting', ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='gray', linewidth=1))
    ax.text(800, 3.35, 'Stationary', ha='center', fontsize=10, style='italic',
            bbox=dict(boxstyle='round,pad=0.3', facecolor='white', alpha=0.8, edgecolor='gray', linewidth=1))

    ax.set_xlabel('Step', fontsize=13, fontweight='bold')
    ax.set_ylabel('Estimated Value', fontsize=13, fontweight='bold')
    ax.set_title('Simple vs. Exponential Averaging (Non-Stationary Environment)',
                 fontsize=15, fontweight='bold', pad=15)
    ax.legend(loc='upper left', fontsize=12, framealpha=0.9, bbox_to_anchor=(0, 0.95))
    ax.grid(True, alpha=0.3)
    
    plt.tight_layout()
    plt.savefig('averaging_comparison.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created averaging_comparison.png")


def create_discount_factor_visualization():
    """Visualize how discount factor affects reward weighting"""
    n_steps = 10
    steps = np.arange(n_steps)
    
    fig, axes = plt.subplots(1, 3, figsize=(14, 4))
    
    gammas = [0.5, 0.9, 0.99]
    colors_gamma = ['#e74c3c', '#3498db', '#2ecc71']
    
    for idx, (gamma, color) in enumerate(zip(gammas, colors_gamma)):
        weights = gamma ** steps
        axes[idx].bar(steps, weights, color=color, alpha=0.7, edgecolor='black', linewidth=1.5)
        axes[idx].set_xlabel('Steps in Future', fontsize=12, fontweight='bold')
        axes[idx].set_ylabel('Reward Weight', fontsize=12, fontweight='bold')
        axes[idx].set_title(f'γ = {gamma}', fontsize=13, fontweight='bold')
        axes[idx].set_ylim([0, 1.05])
        axes[idx].grid(axis='y', alpha=0.3)
        
        # Add cumulative sum text
        cumsum = np.sum(weights[:5])
        axes[idx].text(0.5, 0.95, f'Sum of first 5: {cumsum:.2f}', 
                      transform=axes[idx].transAxes, ha='center', va='top',
                      fontsize=10, bbox=dict(boxstyle='round', facecolor='white', alpha=0.8))
    
    fig.suptitle('How Discount Factor γ Weights Future Rewards', 
                 fontsize=15, fontweight='bold', y=1.02)
    
    plt.tight_layout()
    plt.savefig('discount_factor_visualization.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created discount_factor_visualization.png")


def create_td_update_diagram():
    """Create a visual diagram of TD update"""
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    # States
    state_y = 0.5
    s_curr = FancyBboxPatch((0.1, state_y-0.08), 0.15, 0.16, 
                            boxstyle="round,pad=0.01", 
                            edgecolor='blue', facecolor='lightblue', linewidth=2)
    s_next = FancyBboxPatch((0.7, state_y-0.08), 0.15, 0.16,
                            boxstyle="round,pad=0.01",
                            edgecolor='green', facecolor='lightgreen', linewidth=2)
    ax.add_patch(s_curr)
    ax.add_patch(s_next)
    
    ax.text(0.175, state_y, r'$s_t$', ha='center', va='center', fontsize=18, fontweight='bold')
    ax.text(0.775, state_y, r'$s_{t+1}$', ha='center', va='center', fontsize=18, fontweight='bold')
    
    # Values below states
    ax.text(0.175, state_y - 0.15, r'$V(s_t) = 5.0$', ha='center', va='center', fontsize=12)
    ax.text(0.775, state_y - 0.15, r'$V(s_{t+1}) = 8.0$', ha='center', va='center', fontsize=12)
    
    # Arrow for action/transition
    arrow = FancyArrowPatch((0.26, state_y), (0.69, state_y),
                           arrowstyle='->', mutation_scale=30,
                           linewidth=3, color='black')
    ax.add_patch(arrow)
    ax.text(0.475, state_y + 0.08, 'take action', ha='center', fontsize=11, style='italic')
    
    # Reward
    reward_box = FancyBboxPatch((0.42, state_y - 0.05), 0.11, 0.08,
                                boxstyle="round,pad=0.005",
                                edgecolor='red', facecolor='lightcoral', linewidth=2)
    ax.add_patch(reward_box)
    ax.text(0.475, state_y, r'$r=2$', ha='center', va='center', fontsize=13, fontweight='bold')
    
    # TD Update calculation
    calc_y = 0.15
    ax.text(0.1, calc_y, 'TD Update:', fontsize=13, fontweight='bold')
    ax.text(0.1, calc_y - 0.08, r'Target = $r + \gamma V(s_{t+1})$', fontsize=12)
    ax.text(0.1, calc_y - 0.13, r'Target = $2 + 0.9 \times 8.0 = 9.2$', fontsize=11, color='darkgreen')
    ax.text(0.1, calc_y - 0.20, r'$V(s_t) \leftarrow V(s_t) + \alpha[$Target$-V(s_t)]$', fontsize=12)
    ax.text(0.1, calc_y - 0.25, r'$V(s_t) \leftarrow 5.0 + 0.1 \times (9.2 - 5.0) = 5.42$', 
            fontsize=11, color='darkgreen')
    
    # Parameters box
    param_text = r'Parameters: $\alpha=0.1$, $\gamma=0.9$'
    ax.text(0.75, calc_y - 0.12, param_text, fontsize=11,
            bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.7))
    
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 0.7)
    ax.axis('off')
    ax.set_title('TD(0) Update Example: Using Next State to Update Current State', 
                 fontsize=15, fontweight='bold', pad=20)
    
    plt.tight_layout()
    plt.savefig('td_update_diagram.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created td_update_diagram.png")


def create_sarsa_vs_qlearning_diagram():
    """Create comparison diagram of SARSA vs Q-Learning updates"""
    fig, axes = plt.subplots(2, 1, figsize=(12, 8))
    
    for idx, (ax, algorithm) in enumerate(zip(axes, ['SARSA', 'Q-Learning'])):
        state_y = 0.6
        
        # Current state-action
        s_curr = FancyBboxPatch((0.05, state_y-0.08), 0.12, 0.16,
                                boxstyle="round,pad=0.01",
                                edgecolor='blue', facecolor='lightblue', linewidth=2)
        ax.add_patch(s_curr)
        ax.text(0.11, state_y, r'$s_t, a_t$', ha='center', va='center', fontsize=16, fontweight='bold')
        ax.text(0.11, state_y - 0.15, r'$Q=3.0$', ha='center', fontsize=11)
        
        # Next state
        s_next = FancyBboxPatch((0.65, state_y-0.08), 0.12, 0.16,
                                boxstyle="round,pad=0.01",
                                edgecolor='green', facecolor='lightgreen', linewidth=2)
        ax.add_patch(s_next)
        ax.text(0.71, state_y, r'$s_{t+1}$', ha='center', va='center', fontsize=16, fontweight='bold')
        
        # Transition arrow
        arrow = FancyArrowPatch((0.18, state_y), (0.64, state_y),
                               arrowstyle='->', mutation_scale=25,
                               linewidth=3, color='black')
        ax.add_patch(arrow)
        
        # Reward
        reward_box = FancyBboxPatch((0.38, state_y - 0.05), 0.09, 0.08,
                                    boxstyle="round,pad=0.005",
                                    edgecolor='red', facecolor='lightcoral', linewidth=2)
        ax.add_patch(reward_box)
        ax.text(0.425, state_y, r'$r=1$', ha='center', va='center', fontsize=12, fontweight='bold')
        
        # Next actions (Q-values in next state)
        action_y_start = 0.35
        actions = [
            (r'$a_1$: Q=5.0', 'orange', 0.78),
            (r'$a_2$: Q=7.0', 'gold', 0.78),
            (r'$a_3$: Q=4.0', 'lightcoral', 0.78)
        ]
        
        for i, (label, color, x_pos) in enumerate(actions):
            y_pos = action_y_start - i * 0.1
            action_box = FancyBboxPatch((x_pos, y_pos - 0.03), 0.15, 0.06,
                                       boxstyle="round,pad=0.003",
                                       edgecolor='black', facecolor=color, 
                                       linewidth=1.5, alpha=0.7)
            ax.add_patch(action_box)
            ax.text(x_pos + 0.075, y_pos, label, ha='center', va='center', fontsize=11)
        
        # Algorithm-specific highlighting
        if algorithm == 'SARSA':
            # Highlight the action actually chosen (say a1 with epsilon-greedy)
            highlight = FancyBboxPatch((0.78, action_y_start - 0.03), 0.15, 0.06,
                                      boxstyle="round,pad=0.003",
                                      edgecolor='darkgreen', facecolor='none',
                                      linewidth=3)
            ax.add_patch(highlight)
            ax.text(0.5, 0.05, 'Uses actual next action chosen by policy (e.g., ε-greedy)',
                   ha='center', fontsize=11, style='italic', color='darkgreen', fontweight='bold')
            
            target_text = r'Target = $r + \gamma Q(s_{t+1}, a_{t+1})$' + '\n' + r'= $1 + 0.9 \times 5.0 = 5.5$'
        else:  # Q-Learning
            # Highlight the max Q-value
            highlight = FancyBboxPatch((0.78, action_y_start - 0.13), 0.15, 0.06,
                                      boxstyle="round,pad=0.003",
                                      edgecolor='darkgreen', facecolor='none',
                                      linewidth=3)
            ax.add_patch(highlight)
            ax.text(0.5, 0.05, r'Uses maximum Q-value (greedy), regardless of actual action',
                   ha='center', fontsize=11, style='italic', color='darkgreen', fontweight='bold')
            
            target_text = r'Target = $r + \gamma \max_a Q(s_{t+1}, a)$' + '\n' + r'= $1 + 0.9 \times 7.0 = 7.3$'
        
        # Update equation
        update_box = FancyBboxPatch((0.05, 0.13), 0.4, 0.12,
                                   boxstyle="round,pad=0.01",
                                   edgecolor='purple', facecolor='lavender',
                                   linewidth=2, alpha=0.8)
        ax.add_patch(update_box)
        ax.text(0.25, 0.19, target_text, ha='center', va='center', fontsize=11, fontweight='bold')
        
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 0.8)
        ax.axis('off')
        ax.set_title(f'{algorithm} Update', fontsize=14, fontweight='bold', pad=10)
    
    fig.suptitle('SARSA (On-Policy) vs. Q-Learning (Off-Policy)', 
                 fontsize=16, fontweight='bold', y=0.98)
    
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    plt.savefig('sarsa_vs_qlearning_diagram.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created sarsa_vs_qlearning_diagram.png")


def create_cliff_walking_comparison():
    """Visualize SARSA vs Q-Learning on cliff walking"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Grid setup
    height, width = 4, 12
    
    for idx, (ax, title, path_y) in enumerate(zip(axes, 
                                                   ['Q-Learning Path (Optimal but Risky)',
                                                    'SARSA Path (Safe)'],
                                                   [0.5, 1.5])):
        # Draw grid
        for i in range(height + 1):
            ax.plot([0, width], [i, i], 'k-', linewidth=0.5, alpha=0.3)
        for j in range(width + 1):
            ax.plot([j, j], [0, height], 'k-', linewidth=0.5, alpha=0.3)
        
        # Start
        start = patches.Rectangle((0, 0), 1, 1, linewidth=2,
                                  edgecolor='darkgreen', facecolor='lightgreen', alpha=0.7)
        ax.add_patch(start)
        ax.text(0.5, 0.5, 'S', ha='center', va='center', fontsize=14, fontweight='bold')
        
        # Goal
        goal = patches.Rectangle((width-1, 0), 1, 1, linewidth=2,
                                edgecolor='darkgoldenrod', facecolor='gold', alpha=0.7)
        ax.add_patch(goal)
        ax.text(width-0.5, 0.5, 'G', ha='center', va='center', fontsize=14, fontweight='bold')
        
        # Cliff
        for x in range(1, width-1):
            cliff = patches.Rectangle((x, 0), 1, 1, linewidth=1,
                                     edgecolor='black', facecolor='red', alpha=0.6)
            ax.add_patch(cliff)
            ax.text(x+0.5, 0.5, 'C', ha='center', va='center', 
                   fontsize=12, fontweight='bold', color='white')
        
        # Draw path
        if idx == 0:  # Q-Learning - risky path along cliff
            path = [(0.5, 0.5)]
            for x in range(1, width):
                path.append((x + 0.5, 0.5))
        else:  # SARSA - safe path away from cliff
            path = [(0.5, 0.5), (0.5, 1.5)]
            for x in range(1, width-1):
                path.append((x + 0.5, 1.5))
            path.append((width - 0.5, 0.5))
        
        for i in range(len(path) - 1):
            arrow = FancyArrowPatch(path[i], path[i+1],
                                   arrowstyle='->', mutation_scale=15,
                                   linewidth=2.5, color='blue', alpha=0.7)
            ax.add_patch(arrow)
        
        ax.set_xlim(-0.3, width + 0.3)
        ax.set_ylim(-0.3, height + 0.3)
        ax.set_aspect('equal')
        ax.axis('off')
        ax.set_title(title, fontsize=13, fontweight='bold')
    
    fig.text(0.5, 0.02, 'Q-Learning learns the optimal path (risky). SARSA learns safer path (accounts for exploration errors).',
             ha='center', fontsize=11, style='italic',
             bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
    
    plt.tight_layout(rect=[0, 0.05, 1, 1])
    plt.savefig('cliff_walking_comparison.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created cliff_walking_comparison.png")


def create_function_approximation_diagram():
    """Visualize function approximation concept"""
    fig, axes = plt.subplots(1, 2, figsize=(14, 5))
    
    # Left: Tabular
    ax = axes[0]
    states = ['s1', 's2', 's3', 's4', 's5']
    q_values = [2.3, 1.8, 3.1, 2.9, 1.5]
    colors_q = ['#3498db' if q < 2.5 else '#e74c3c' for q in q_values]
    
    bars = ax.bar(states, q_values, color=colors_q, alpha=0.7, edgecolor='black', linewidth=2)
    ax.set_ylabel('Q-value', fontsize=12, fontweight='bold')
    ax.set_xlabel('State', fontsize=12, fontweight='bold')
    ax.set_title('Tabular: Store Each State Separately', fontsize=13, fontweight='bold')
    ax.set_ylim([0, 4])
    ax.grid(axis='y', alpha=0.3)
    
    for bar, q in zip(bars, q_values):
        height = bar.get_height()
        ax.text(bar.get_x() + bar.get_width()/2., height + 0.1,
               f'{q:.1f}', ha='center', va='bottom', fontsize=11, fontweight='bold')
    
    ax.text(0.5, -0.2, 'Problem: What if we have\n1 million states?', 
           transform=ax.transAxes, ha='center', fontsize=10, style='italic',
           bbox=dict(boxstyle='round', facecolor='yellow', alpha=0.3))
    
    # Right: Function Approximation
    ax = axes[1]
    
    # Generate more states for continuous visualization
    x = np.linspace(0, 5, 100)
    # Features (distance to goal)
    features = x
    weights = 0.5  # learned weight
    q_approx = weights * features + 0.5
    
    ax.plot(x, q_approx, 'b-', linewidth=3, label=r'$Q(s) = w \cdot x(s)$')
    
    # Show sample states
    sample_states = [1, 2, 3, 4]
    sample_features = np.array(sample_states)
    sample_q = weights * sample_features + 0.5
    ax.scatter(sample_states, sample_q, s=150, c='red', zorder=5, 
              edgecolors='black', linewidth=2, label='Sample states')
    
    ax.set_ylabel('Q-value', fontsize=12, fontweight='bold')
    ax.set_xlabel('Feature (e.g., distance to goal)', fontsize=12, fontweight='bold')
    ax.set_title('Function Approximation: Learn Weights', fontsize=13, fontweight='bold')
    ax.set_ylim([0, 4])
    ax.grid(True, alpha=0.3)
    ax.legend(fontsize=11, loc='upper left')
    
    ax.text(0.5, -0.2, 'Solution: Share learning across\nsimilar states!', 
           transform=ax.transAxes, ha='center', fontsize=10, style='italic',
           bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))
    
    plt.tight_layout()
    plt.savefig('function_approximation_diagram.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created function_approximation_diagram.png")


def create_learning_curves():
    """Create learning curves for different algorithms"""
    np.random.seed(42)
    
    episodes = 500
    x = np.arange(episodes)
    
    # Simulate learning curves
    # Q-Learning: Fast but unstable
    q_learning = 50 + 150 * (1 - np.exp(-x/100)) + np.random.randn(episodes) * 10
    
    # SARSA: Slower but more stable
    sarsa = 50 + 140 * (1 - np.exp(-x/120)) + np.random.randn(episodes) * 7
    
    # DQN: Even better
    dqn = 50 + 180 * (1 - np.exp(-x/80)) + np.random.randn(episodes) * 8
    
    # Smooth with moving average
    window = 20
    q_learning_smooth = np.convolve(q_learning, np.ones(window)/window, mode='valid')
    sarsa_smooth = np.convolve(sarsa, np.ones(window)/window, mode='valid')
    dqn_smooth = np.convolve(dqn, np.ones(window)/window, mode='valid')
    x_smooth = x[window-1:]
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 6))
    
    ax.plot(x, q_learning, 'b-', alpha=0.2, linewidth=0.5)
    ax.plot(x_smooth, q_learning_smooth, 'b-', linewidth=2.5, label='Q-Learning (Tabular)', alpha=0.8)
    
    ax.plot(x, sarsa, 'g-', alpha=0.2, linewidth=0.5)
    ax.plot(x_smooth, sarsa_smooth, 'g-', linewidth=2.5, label='SARSA (Tabular)', alpha=0.8)
    
    ax.plot(x, dqn, 'r-', alpha=0.2, linewidth=0.5)
    ax.plot(x_smooth, dqn_smooth, 'r-', linewidth=2.5, label='DQN (Deep RL)', alpha=0.8)
    
    ax.set_xlabel('Episode', fontsize=13, fontweight='bold')
    ax.set_ylabel('Average Reward', fontsize=13, fontweight='bold')
    ax.set_title('Learning Curves: Comparing RL Algorithms', fontsize=15, fontweight='bold')
    ax.legend(fontsize=12, loc='lower right', framealpha=0.9)
    ax.grid(True, alpha=0.3)
    ax.set_xlim([0, episodes])
    
    plt.tight_layout()
    plt.savefig('learning_curves_comparison.png', dpi=150, bbox_inches='tight')
    plt.close()
    print("[OK] Created learning_curves_comparison.png")


def create_rl_loop_diagram():
    """Create a simple, clean RL interaction diagram - no fluff"""
    fig, ax = plt.subplots(1, 1, figsize=(10, 6))

    # Agent box (top, with gap below)
    agent_box = FancyBboxPatch((0.20, 0.58), 0.6, 0.30,
                               boxstyle="round,pad=0.02",
                               edgecolor='#2E86AB', facecolor='#A9D6E5',
                               linewidth=6, alpha=0.95)
    ax.add_patch(agent_box)
    ax.text(0.5, 0.73, 'AGENT', ha='center', va='center',
           fontsize=40, fontweight='bold', color='#01497C')

    # Environment box (bottom, with gap above)
    env_box = FancyBboxPatch((0.20, 0.12), 0.6, 0.30,
                             boxstyle="round,pad=0.02",
                             edgecolor='#2D6A4F', facecolor='#95D5B2',
                             linewidth=6, alpha=0.95)
    ax.add_patch(env_box)
    ax.text(0.5, 0.27, 'ENVIRONMENT', ha='center', va='center',
           fontsize=40, fontweight='bold', color='#1B4332')

    # Action arrow (Agent → Environment) - centered, arrowhead inside environment
    action_arrow = FancyArrowPatch((0.30, 0.61), (0.30, 0.44),
                                  arrowstyle='->', mutation_scale=60,
                                  linewidth=10, color='#6A4C93', zorder=3)
    ax.add_patch(action_arrow)

    # Action label - moved towards center
    ax.text(0.18, 0.50, 'Action', ha='center', va='center',
           fontsize=24, fontweight='bold', color='white',
           bbox=dict(boxstyle='round,pad=0.8', facecolor='#6A4C93',
                    edgecolor='#472D5B', linewidth=3))

    # Return arrow (Environment → Agent) - centered, arrowhead inside agent
    return_arrow = FancyArrowPatch((0.70, 0.39), (0.70, 0.56),
                                  arrowstyle='->', mutation_scale=60,
                                  linewidth=10, color='#D62828', zorder=3)
    ax.add_patch(return_arrow)

    # State + Reward label - moved towards center
    ax.text(0.82, 0.50, 'State +\nReward', ha='center', va='center',
           fontsize=24, fontweight='bold', color='white',
           bbox=dict(boxstyle='round,pad=0.8', facecolor='#D62828',
                    edgecolor='#9B2226', linewidth=3))

    ax.set_xlim(0.05, 0.95)
    ax.set_ylim(0.08, 0.92)
    ax.axis('off')

    plt.tight_layout(pad=0)
    plt.savefig('rl_loop_diagram.png', dpi=150, bbox_inches='tight', pad_inches=0.1)
    plt.close()
    print("[OK] Created rl_loop_diagram.png")


def main():
    """Generate all visualizations"""
    print("\n" + "="*50)
    print("Generating RL Visualizations")
    print("="*50 + "\n")
    
    create_rl_loop_diagram()
    create_gridworld_example()
    create_epsilon_greedy_vs_softmax()
    create_averaging_comparison()
    create_discount_factor_visualization()
    create_td_update_diagram()
    create_sarsa_vs_qlearning_diagram()
    create_cliff_walking_comparison()
    create_function_approximation_diagram()
    create_learning_curves()
    
    print("\n" + "="*50)
    print("[OK] All visualizations created successfully!")
    print("="*50 + "\n")


if __name__ == "__main__":
    main()