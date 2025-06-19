"""
Statically vs Dynamically Typed
"""
"""🧠 Think: "Declared vs. Discovered" """
# Statically typed: Types are declared before runtime
# Example (C++): int x = 5;
# Dynamically typed: Types are inferred during runtime
# Example (Python): x = 5

"""
Strong vs Weak Typing
"""
"""🧠 Strong: types are enforced. Weak: types are bendy. """
# Strong typing: No implicit type conversions
# Example (Python): "5" + 1 → ❌ TypeError
# Weak typing: Implicit type coercion allowed
# Example (JavaScript): "5" + 1 → "51"

"""
Programming Paradigms
"""
"""🧠 Procedural: do this. OOP: who’s doing it. Functional: transform data. """
# Procedural: Step-by-step logic, shared state
# Example: C, early Python
# Object-Oriented (OOP): Code organized in objects/classes
# Example: Python, Java, C++
# Functional: Uses pure functions and immutability
# Example: Haskell, functional JS
# Declarative: You describe *what* to do, not *how*
# Example: SQL, HTML

"""
Interpreted vs Compiled
"""
"""🧠 Compiled is like baking a cake. Interpreted is cooking while reading the recipe. """
# Interpreted: Executes code line-by-line at runtime
# Example: Python, JavaScript
# Compiled: Translates code to machine instructions first
# Example: C, Go, Rust

"""
Memory Management and Garbage Collection
"""
"""🧠 Garbage Collection = Janitor for memory. """
# Manual memory management: You allocate and free memory
# Example: C with malloc/free
# Automatic (Garbage Collection): Runtime cleans up unused memory
# Example: Python, Java, Go

"""
Summary Table
"""
"""🧠 Quick glance for comparing languages """
# Language     | Strong/Weak | Static/Dynamic | Interpreted/Compiled | Memory
# ---------------------------------------------------------------------------
# Python       | Strong      | Dynamic        | Interpreted          | GC
# C++          | Strong      | Static         | Compiled             | Manual
# JavaScript   | Weak        | Dynamic        | Interpreted (JIT)    | GC
# Java         | Strong      | Static         | Compiled to bytecode | GC
