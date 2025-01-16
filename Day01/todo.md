# **Day 1: Refreshing Object-Oriented Python Basics**

## **Learning Objectives**
1. Review the core concepts of object-oriented programming (OOP) in Python.
2. Practice defining and using classes, objects, methods, and attributes.
3. Understand key OOP principles: encapsulation, inheritance, polymorphism, and abstraction.
4. Write Python scripts to solidify these concepts.

---

## **Schedule**

### **1. Concept Review (1–2 hours)**
- Basics of classes and objects.
- Instance vs. class attributes.
- Methods: Instance, Class, and Static.
- Special (Magic/Dunder) methods like `__init__`, `__str__`, and `__repr__`.
- OOP principles (encapsulation, inheritance, polymorphism, abstraction).

### **2. Hands-On Coding (2–3 hours)**
- Create a small project or script to apply these concepts. Example ideas:
  - A basic **Bank Account Management System**.
  - **Library Management** using classes and inheritance.
- Use multiple OOP features like inheritance, encapsulation, and magic methods.

### **3. DSA Warm-Up (1 hour)**
- Solve 2–3 beginner-level problems from platforms like LeetCode, HackerRank, or Codewars that involve basic array or string manipulation.

---

## **Practice Problem Suggestions**

### **Bank Account Class**
```python
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ${amount}. Current balance: ${self.balance}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrew ${amount}. Current balance: ${self.balance}")

    def __str__(self):
        return f"Account holder: {self.account_holder}, Balance: ${self.balance}"

# Example usage
account = BankAccount("John Doe", 500)
account.deposit(200)
account.withdraw(100)
print(account)
```

---

## **Deliverables for Day 1**
1. Create a GitHub repository (if not already done) to upload daily progress.
2. Push the code for the OOP practice project.
3. Solve 2–3 DSA problems and push your solutions.
4. Write a brief README/log for Day 1 summarizing what you learned.

---

## **Python Expertise Checklist**

### **Beginner Level**
- [ ] Python Basics: Syntax, keywords, input/output, comments.
- [ ] Variables and Data Types: Numbers (int, float, complex), strings, booleans.
- [ ] Control Flow: Conditional statements (`if`, `elif`, `else`), loops (`for`, `while`, `break`, `continue`).
- [ ] Basic Data Structures: Lists, tuples, dictionaries, sets, stack, queue.
- [ ] Functions: Definitions, parameters, return values, scope, default arguments.
- [ ] File Handling: Reading/writing text files, appending to files, handling file paths.
- [ ] Basic Libraries: `math`, `random`, `datetime`, `os`.
- [ ] Debugging Basics: Common errors, using `print` statements.
- [ ] Basic Regular Expressions: `re` module basics.

### **Mid-Level**
- [ ] Object-Oriented Programming: Classes, objects, inheritance, polymorphism, encapsulation, abstraction.
- [ ] Advanced Data Structures: Comprehensions (list, dict, set), iterators, generators (`yield`), linked lists, binary trees.
- [ ] Error Handling: Custom exceptions, exception chaining, proper use of `finally`.
- [ ] Modules and Packages: Importing, creating, and managing custom packages, using `__init__.py`.
- [ ] Functional Programming: `map`, `filter`, `reduce`, lambdas, closures, decorators.
- [ ] Python Standard Library: Modules like `itertools`, `functools`, `collections`, `pathlib`.
- [ ] Testing and Debugging: `unittest`, `pytest`, `mock`, debugging with `pdb` and IDE tools.
- [ ] Basic Networking: HTTP requests using `requests`, socket basics, basic web scraping with `BeautifulSoup`.
- [ ] Algorithms and Complexity: Sorting, searching, recursion basics.
- [ ] Logging: Using the `logging` module for structured logs.
- [ ] File Formats: Working with CSV, JSON, XML.
- [ ] Basic Multithreading and Multiprocessing.

### **Expert Level**
- [ ] Advanced OOP: Design patterns (Factory, Singleton, Observer), metaclasses, descriptors.
- [ ] Concurrency and Parallelism: Advanced multithreading, multiprocessing, `asyncio`, `concurrent.futures`.
- [ ] Performance Optimization: Profiling (`cProfile`, `timeit`), memory optimization, using `Cython`, `Numba`.
- [ ] Web Development: Frameworks like Flask, Django, FastAPI, creating REST APIs, working with websockets.
- [ ] Data Science and Machine Learning: Libraries like `NumPy`, `Pandas`, `Matplotlib`, `Scikit-learn`, `TensorFlow`, `PyTorch`, exploratory data analysis (EDA).
- [ ] Databases: SQL databases (`sqlite3`, `SQLAlchemy`, `PostgreSQL`), NoSQL (`MongoDB`, `Cassandra`), ORMs.
- [ ] Security: Hashing and encryption (`hashlib`, `cryptography`), secure coding practices, OWASP concepts.
- [ ] DevOps and Automation: Scripting, building CLI tools (`argparse`, `click`), task automation (`fabric`, `invoke`, `airflow`).
- [ ] Advanced Libraries: `json`, `yaml`, `HDF5`, `Parquet`, `openpyxl` for Excel.
- [ ] Best Practices: Writing clean, Pythonic code, following `PEP 8`, using `mypy` for type checking.
- [ ] Advanced Networking: APIs, advanced socket programming, real-time data transfer.
- [ ] Open Source Contributions: Contributing to Python projects, building reusable libraries.
- [ ] Distributed Systems: Message brokers like `RabbitMQ`, `Kafka`, handling distributed tasks with `Celery`.
- [ ] Deployment: Packaging with `setuptools`, using `Docker`, deploying applications to cloud platforms (AWS, Azure, GCP).
- [ ] Advanced Debugging and Profiling Tools: `line_profiler`, `memory_profiler`.
- [ ] Advanced Algorithmic Topics: Dynamic programming, graph algorithms, optimization problems.
- [ ] Big Data Handling: Using Python with big data frameworks like Spark (`PySpark`).
