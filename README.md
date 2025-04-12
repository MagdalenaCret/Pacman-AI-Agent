# 🎮 PACMAN AI Project 👾

A comprehensive implementation of various AI search and decision-making algorithms for the classic Pacman game, developed for the Artificial Intelligence course at Technical University of Cluj-Napoca.

## 📋 Project Overview
This project implements intelligent agents for the Pacman game that can navigate mazes and make decisions using various AI algorithms. The project is divided into two main parts:

1. **🔍 Search Algorithms: Implementations of uninformed and informed search strategies**: Implementations of uninformed and informed search strategies
2. **🤖 Multi-Agent Search**: Adversarial and probabilistic search algorithms for dealing with ghost agents

## 🧠 Algorithms Implemented

### 🔍 Search Algorithms
- Depth-First Search (DFS)
- Breadth-First Search (BFS)
- Uniform Cost Search (UCS)
- A* Search
- Greedy Best-First Search
- Custom heuristics for corner problems and food collection

### 🤖 Multi-Agent Search
- Reflex Agent
- Minimax
- Alpha-Beta Pruning
- Expectimax
- Custom evaluation functions

## 🚀 How to Run

The project includes an autograder that can be run to test the implementations: 
  ```
python autograder.py
  ```
To run specific parts of the project:

# Search algorithms
  ```
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic
  ```

# Multi-agent algorithms
  ```
python pacman.py -p ReflexAgent -l testClassic
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3
  ```

## 📁 Project Structure

The project is organized as follows:

- `search.py`: Contains the search algorithms implementation
- `searchAgents.py`: Contains the search-based agents and heuristics
- `multiAgents.py`: Contains the adversarial and probabilistic search agents
- `pacman.py`: The main game engine
- `game.py`: The game logic
- `util.py`: Utility data structures and functions
- `graphicsDisplay.py`: Graphics for the game
- `autograder.py`: Automatic grader for the implementation

# 🎮 PACMAN AI Project 👾
A comprehensive implementation of various AI search and decision-making algorithms for the classic Pacman game, developed for the Artificial Intelligence course at Technical University of Cluj-Napoca.
📋 Project Overview
This project implements intelligent agents for the Pacman game that can navigate mazes and make decisions using various AI algorithms. The project is divided into two main parts:

🔍 Search Algorithms: Implementations of uninformed and informed search strategies
🤖 Multi-Agent Search: Adversarial and probabilistic search algorithms for dealing with ghost agents

🧠 Algorithms Implemented
🔍 Search Algorithms

🌲 Depth-First Search (DFS)
🌊 Breadth-First Search (BFS)
⚖️ Uniform Cost Search (UCS)
⭐ A* Search
🚀 Greedy Best-First Search
🧩 Custom heuristics for corner problems and food collection

🤖 Multi-Agent Search

💡 Reflex Agent
🎯 Minimax
✂️ Alpha-Beta Pruning
🎲 Expectimax
📊 Custom evaluation functions

🚀 How to Run
The project includes an autograder that can be run to test the implementations:
python autograder.py
To run specific parts of the project:
# Search algorithms
python pacman.py -l mediumMaze -p SearchAgent -a fn=dfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=bfs
python pacman.py -l mediumMaze -p SearchAgent -a fn=ucs
python pacman.py -l bigMaze -z .5 -p SearchAgent -a fn=astar,heuristic=manhattanHeuristic

# Multi-agent algorithms
python pacman.py -p ReflexAgent -l testClassic
python pacman.py -p MinimaxAgent -l minimaxClassic -a depth=4
python pacman.py -p AlphaBetaAgent -a depth=3 -l smallClassic
python pacman.py -p ExpectimaxAgent -l minimaxClassic -a depth=3

# 📥 Getting Started
To use this project:

📥 Clone the repository
 ```
 git clone https://github.com/MagdalenaCret/Pacman-AI-Agent
 ```

🐍 Make sure you have Python installed
🎮 Run any of the commands listed in the "How to Run" section
✅ Test your implementations using the autograder

## 👩‍💻 Author

- Maria-Magdalena Creț
- Academic Year 2024-2025

## 🙏 Acknowledgments

This project was developed as part of the Artificial Intelligence course at the Technical University of Cluj-Napoca, Faculty of Automation and Computer Science.

## 📚 References

- [Stack Overflow - BFS Algorithm for Pacman](https://stackoverflow.com/questions/29141501/how-to-implement-bfs-algorithm-for-pacman)
- [Wikipedia - A* Search Algorithm](https://en.wikipedia.org/wiki/A*_search_algorithm)
- [Medium - Graph Traversal in Python: A* Algorithm](https://medium.com/nerd-for-tech/graph-traversal-in-python-a-algorithm-27c30d67e0d0)
- [GeeksforGeeks - Uniform Cost Search](https://www.geeksforgeeks.org/uniform-cost-search-dijkstra-for-large-graphs)
- [Pacman Project Resources](https://rshcaroline.github.io/research/resources/pacman-report.pdf)
  
