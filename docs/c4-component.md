# C4 Component Diagram - Calculator Application

This diagram shows the internal components within each container of the Calculator Application.

```mermaid
graph TB
    subgraph replContainer["Calculator REPL"]
        calculator["Calculator<br/><i>Python Class</i><br/>Main REPL loop and command dispatcher"]
        inputParser["Input Parser<br/><i>Method</i><br/>Parses and validates user input"]
        outputFormatter["Output Formatter<br/><i>Methods</i><br/>Formats results and error messages"]
    end

    subgraph calculationContainer["Calculation Engine"]
        calcFactory["CalculationFactory<br/><i>Python Class</i><br/>Factory for creating calculation instances"]
        calcRegistry["Calculation Registry<br/><i>Class Attribute</i><br/>Maps operation names to calculation classes"]
        calcBase["Calculation Base<br/><i>Abstract Class</i><br/>Base class defining calculation interface"]
        addCalc["AddCalculation<br/><i>Python Class</i><br/>Addition operation implementation"]
        subCalc["SubtractCalculation<br/><i>Python Class</i><br/>Subtraction operation implementation"]
        mulCalc["MultiplyCalculation<br/><i>Python Class</i><br/>Multiplication operation implementation"]
        divCalc["DivideCalculation<br/><i>Python Class</i><br/>Division operation implementation"]
        powCalc["PowerCalculation<br/><i>Python Class</i><br/>Exponentiation operation implementation"]
    end

    subgraph opsContainer["Operations Module"]
        operations["Operations<br/><i>Python Class</i><br/>Static methods for arithmetic operations"]
    end

    calculator --> inputParser
    calculator --> outputFormatter
    calculator --> calcFactory
    
    calcFactory --> calcRegistry
    calcFactory -.-> addCalc
    calcFactory -.-> subCalc
    calcFactory -.-> mulCalc
    calcFactory -.-> divCalc
    calcFactory -.-> powCalc
    
    addCalc --> calcBase
    subCalc --> calcBase
    mulCalc --> calcBase
    divCalc --> calcBase
    powCalc --> calcBase
    
    addCalc -.-> operations
    subCalc -.-> operations
    mulCalc -.-> operations
    divCalc -.-> operations
```

## Description

This diagram shows the detailed component structure within each container of the Calculator Application.

### Calculator REPL Components

1. **Calculator**
   - Main class managing the REPL loop
   - Coordinates input parsing and output formatting
   - Handles exceptions and error recovery

2. **Input Parser**
   - `_parse_input()` method
   - Validates command format
   - Extracts operation and operands
   - Converts strings to numeric types

3. **Output Formatter**
   - `_print_welcome()` method
   - Formats calculation results
   - Displays error messages

### Calculation Engine Components

1. **CalculationFactory**
   - Central factory class
   - `create_calculation()` class method
   - `register_calculation()` decorator for registration
   - Manages the calculation registry

2. **Calculation Registry**
   - `calculations` class attribute (dict)
   - Maps operation names to calculation classes
   - Populated via decorator pattern at import time

3. **Calculation (Base)**
   - Abstract base class (ABC)
   - Defines `execute()` abstract method
   - Provides `__str__()` and `__repr__()` methods
   - Stores operands (a, b)

4. **Calculation Implementations**
   - **AddCalculation**: `a + b`
   - **SubtractCalculation**: `a - b`
   - **MultiplyCalculation**: `a * b`
   - **DivideCalculation**: `a / b` (with zero check)
   - **PowerCalculation**: `a ** b`

### Operations Module Components

1. **Operations**
   - Static class with arithmetic methods
   - Legacy support for direct operation calls
   - Methods: `addition()`, `subtraction()`, `multiplication()`, `division()`

## Design Patterns

- **Factory Pattern**: CalculationFactory creates calculation instances based on operation type
- **Registry Pattern**: Decorator-based registration of calculation classes
- **Template Method**: Calculation base class defines structure, subclasses implement `execute()`
- **Strategy Pattern**: Different calculation classes represent different arithmetic strategies
