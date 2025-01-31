# Snake AI 🐍

<p align="center">
  <img src="./assets/sanke_logo.jpg" alt="Snake AI Logo" width="200"/>
</p>

## About The Project

Snake AI is an implementation of the classic Snake game with a reinforcement learning agent that learns to play the game optimally. The project uses PyTorch to create a Deep Q-Learning model that improves its gameplay through experience.

## Features

- Classic Snake game implementation with PyGame
- Deep Q-Learning neural network using PyTorch
- Real-time training visualization
- Performance tracking with matplotlib
- Both human playable and AI training modes

## Demo
https://github.com/user-attachments/assets/177f469d-afe3-4886-83ba-a122f4cde06e

## Learning Process

```mermaid
flowchart TD
    A[Game State] --> B[Agent Gets State]
    B --> C[State Processing]
    C -->|11 Input Values| D[Neural Network]
    D --> E{Action Selection}
    E -->|Exploration| F[Random Move]
    E -->|Exploitation| G[Predicted Best Move]
    F --> H[Execute Action]
    G --> H
    H --> I[Get Reward]
    I --> J{Game Over?}
    J -->|Yes| K[Train Long Memory]
    J -->|No| L[Train Short Memory]
    K --> M[Reset Game]
    L --> N[Update State]
    M --> A
    N --> A
    
    subgraph "State Values"
    SV1[Danger Straight]
    SV2[Danger Right]
    SV3[Danger Left]
    SV4[Direction]
    SV5[Food Location]
    end
    
    subgraph "Rewards"
    R1[Eat Food: +10]
    R2[Game Over: -10]
    R3[Survive: 0]
    end
```
## Traning process 

The agent uses an epsilon-greedy strategy for exploration :

- Initial random moves for exploration
- Gradually transitions to exploitation of learned patterns
- Stores experiences in memory
- Trains in both short-term and long-term memory phases





## Getting Started

### Prerequisites

```bash
- Python 3.7+
- PyTorch
- Pygame
- Matplotlib
- NumPy
- Python3-tk


