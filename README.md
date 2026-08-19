# Digital Logic Circuit Simulator

A dynamic, object-oriented digital logic gate simulator and truth table generator built entirely in Python. 

This project bridges hardware engineering principles with software architecture, allowing users to input complex boolean expressions, which are then parsed and compiled into functional logic gate architectures in memory.

## 🚀 Features

* **Algorithmic Parsing:** Implements Dijkstra's Shunting Yard algorithm to convert standard infix boolean expressions into Reverse Polish Notation (RPN).
* **Object-Oriented Architecture (OOP):** Utilizes abstract base classe ('LogicGate') and polymorphism ('AndGate', 'OrGate', 'NotGate') to simulate physical hardware behavior.
* **Dynamic Truth Tables:** Automatically calculates and generates comprehensive truth tables for 2^n possible states of N-variable circuits.
* **Defensive Programming:** Includes robust error handling and syntax validation to prevent crashes from invalid user inputs.

## 💻 Tech Stack

* **Language:** Python 
* **Core Concepts:** OOP, Data Structures (Stacks/Queues),Shunting Yard Algorithm.
## ⚙️ How to Run

1. Clone the repository to your local machine:

        git clone https://github.com/NivYehoshua/digital-logic-simulator.git

2. Navigate to the project directory and run the simulator:

        python simulator.py

3. Follow the on-screen prompts to enter the number of inputs and your boolean expression (e.g., `A AND ( B OR C )`).

## 📸 Example Output
<img width="642" height="429" alt="image" src="https://github.com/user-attachments/assets/38713c8a-9287-4ac4-98af-a03f4c7e520b" />

