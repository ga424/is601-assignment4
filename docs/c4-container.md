# C4 Container Diagram - Calculator Application

This diagram shows the high-level containers (applications, processes) that make up the Calculator Application.

```mermaid
graph TB
    user["User<br/><i>Person</i><br/>A person who needs to perform arithmetic calculations"]
    
    subgraph calculatorApp["Calculator Application"]
        replModule["Calculator REPL<br/><i>Python Module</i><br/>Provides interactive command-line interface<br/>for entering operations and displaying results"]
        calculationEngine["Calculation Engine<br/><i>Python Module</i><br/>Factory-based system for creating<br/>and executing arithmetic calculations"]
        operationsModule["Operations Module<br/><i>Python Module</i><br/>Core arithmetic operation implementations<br/>(legacy support)"]
    end

    user -->|Enters commands<br/>stdin/stdout| replModule
    replModule -->|Creates calculations<br/>Function calls| calculationEngine
    calculationEngine -.->|Delegates to<br/>Function calls| operationsModule
```

## Description

The Calculator Application consists of three main containers:

### Containers

1. **Calculator REPL** (`app/calculator`)
   - Handles user input/output
   - Parses commands and validates input
   - Manages the interactive loop
   - Displays results and error messages

2. **Calculation Engine** (`app/calculation`)
   - Factory pattern implementation for creating calculations
   - Registry of available calculation types
   - Execution of arithmetic operations
   - Supports: add, subtract, multiply, divide, power

3. **Operations Module** (`app/operations`)
   - Legacy static methods for arithmetic operations
   - Provides core calculation logic
   - Used by calculation classes

### Interactions

- User inputs commands to the REPL module
- REPL creates calculation instances via the Calculation Engine
- Calculation Engine uses the Factory pattern to instantiate appropriate calculation classes
- Calculation classes use Operations Module for actual arithmetic
