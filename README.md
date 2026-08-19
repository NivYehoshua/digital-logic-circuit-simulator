# Digital Logic Circuit Simulator

A dynamic, object-oriented digital logic gate simulator and truth table generator built entirely in Python. 

This project bridges hardware engineering principles with software architecture, allowing users to input complex boolean expressions, which are then parsed and compiled into functional logic gate architectures in memory.

## 🚀 Features

* **Algorithmic Parsing:** Implements Dijkstra's Shunting Yard algorithm to convert standard infix boolean expressions into Reverse Polish Notation (RPN).
* **Object-Oriented Architecture (OOP):** Utilizes abstract base classes and polymorphism (`LogicGate`, `AndGate`, `OrGate`, `NotGate`) to simulate physical hardware behavior.
* **Memory Efficiency:** Implements a Symbol Table (Dictionary) to manage input pins, ensuring multiple instances of the same variable point to the exact same object in memory.
* **Dynamic Truth Tables:** Automatically calculates and generates comprehensive truth tables for 2^n possible states of N-variable circuits.
* **Defensive Programming:** Includes robust error handling and syntax validation to prevent crashes from invalid user inputs.

## 💻 Tech Stack

* **Language:** Python 3.x
* **Core Concepts:** OOP, Data Structures (Stacks/Queues), Graph Logic, Shunting Yard Algorithm.

## ⚙️ How to Run

1. Clone the repository to your local machine:
   ```bash
   git clone [https://github.com/NivYehoshua/digital-logic-simulator.git](https://github.com/NivYehoshua/digital-logic-simulator.git)
