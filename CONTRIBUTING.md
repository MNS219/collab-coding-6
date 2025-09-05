# Contributing Guide — Collaborative Coding (Group 6)

Welcome to our collaborative coding project! Please follow these steps and rules to keep our workflow smooth.

---

## Roles
- **Admin/Integrator**: Sets up repo, manages merges, writes final driver in `main.py`.
- **Contributors (4)**: Each adds ONE function in `main.py` and a matching test file.

---

## Workflow
1. **Branching**
   - Create a new branch for your work:
     ```
     git checkout -b feat/<your-name>-function
     ```
2. **Add Your Function**
   - Open `main.py` and find your placeholder section.
   - Implement your function with:
     - Clear **docstring** (Args, Returns, Author).
     - Proper error handling if needed.
   - Example:
     ```python
     def my_function(x: int) -> int:
         """
         Returns x squared.

         Args:
             x: integer

         Returns:
             int: x squared

         Author:
             Your Name (Roll No.)
         """
         return x * x
     ```
3. **Write Tests**
   - Create/update your own test file `test_func_<name>.py`.
   - Use `pytest` conventions (`assert` statements).
   - Example:
     ```python
     from main import my_function

     def test_my_function_basic():
         assert my_function(3) == 9
     ```
4. **Commit & Push**
   - Use meaningful commit messages:
     - `feat: add <your-name> function`
     - `test: add unit tests for <your-name>`
   - Push branch and open a Pull Request (PR).

5. **Pull Request (PR)**
   - Request at least **one peer review**.
   - Address review comments.
   - Ensure tests pass before merge.

---

## Code Style
- Language: Python 3.x
- Follow [PEP 8](https://peps.python.org/pep-0008/) (basic readability).
- Each function must include:
  - Docstring
  - Author tag (Name + Roll No.)
- Keep functions small, focused, and easy to test.

---

## Tests
- Use **pytest**.
- Cover normal inputs and at least one edge case.
- Ensure `pytest` runs without errors:
