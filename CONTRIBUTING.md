# Contributing to Quill

Thank you for your interest in contributing to Quill! We welcome contributions from everyone, whether you're fixing a bug, adding a feature, improving documentation, or creating example games.

## 🌟 Ways to Contribute

### 1. Report Bugs
Found a bug? Please open an issue with:
- A clear title and description
- Steps to reproduce the bug
- Expected vs actual behavior
- Your OS and Quill version
- Sample code that demonstrates the issue

### 2. Suggest Features
Have an idea? Open an issue with:
- Clear description of the feature
- Use cases and examples
- Why it would be useful
- Potential implementation ideas (optional)

### 3. Improve Documentation
- Fix typos or unclear explanations
- Add more examples
- Translate documentation
- Create tutorials or guides

### 4. Submit Code
- Fix bugs
- Add new features
- Improve performance
- Write tests

### 5. Create Examples
- Write example games or programs
- Share interesting use cases
- Create educational tutorials

## 🚀 Getting Started

### Fork and Clone
```bash
# Fork the repository on GitHub, then:
git clone https://github.com/YOUR_USERNAME/Quill.git
cd Quill
```

### Set Up Development Environment
```bash
# Quill requires Python 3.8+
python --version  # Check your version

# Install in development mode
cd core
python -m pip install -e .
```

### Make Your Changes
1. Create a new branch: `git checkout -b feature/your-feature-name`
2. Make your changes
3. Test your changes thoroughly
4. Commit with clear messages: `git commit -m "Add feature: description"`

### Test Your Changes
```bash
# Run existing examples to ensure nothing broke
cd examples
python ../core/Quill.py example_simple.quill

# Test your specific changes
python ../core/Quill.py your_test.quill
```

## 📝 Code Style Guidelines

### Quill Code (`.quill` files)
- Use lowercase for variable names: `player_health`, `enemy_count`
- Use descriptive names: `calculate_damage()` not `calc_dmg()`
- Add comments for complex logic
- Keep functions small and focused
- Indent with 4 spaces

**Good:**
```Quill
# Calculate player damage based on weapon and stats
function calculate_damage(weapon, strength) do
    set base_damage = weapon.power
    set bonus = strength * 2
    return base_damage + bonus
end
```

**Avoid:**
```Quill
func cd(w,s) do
set d=w.p+s*2
return d
end
```

### Python Code (Core Interpreter)
- Follow PEP 8 style guide
- Use type hints where possible
- Write docstrings for functions and classes
- Keep functions under 50 lines when possible
- Add comments for complex algorithms

**Good:**
```python
def evaluate_expression(self, node: ASTNode) -> Any:
    """
    Evaluate an expression node and return its value.
    
    Args:
        node: The AST node to evaluate
        
    Returns:
        The evaluated value (int, str, bool, etc.)
    """
    if node.type == 'NUMBER':
        return int(node.value)
    # ... more logic
```

### Documentation
- Use clear, simple language
- Provide code examples
- Include expected output
- Explain *why*, not just *what*

## 🔍 Pull Request Process

### Before Submitting
- [ ] Test your changes thoroughly
- [ ] Update documentation if needed
- [ ] Add examples if adding features
- [ ] Ensure code follows style guidelines
- [ ] Write clear commit messages

### Submitting
1. Push to your fork: `git push origin feature/your-feature-name`
2. Open a Pull Request on GitHub
3. Fill out the PR template completely
4. Link any related issues

### PR Description Should Include
- **What**: What does this PR do?
- **Why**: Why is this change needed?
- **How**: How does it work?
- **Testing**: How did you test it?
- **Screenshots**: If UI changes (optional)

### Example PR Description
```markdown
## Add `wait()` function for timed pauses

### What
Adds a new built-in `wait()` function that pauses execution for a specified number of seconds.

### Why
Many games need dramatic pauses (e.g., "The door slowly opens..."). Currently no way to do this.

### How
- Added `wait()` to built-in functions in `interpreter.py`
- Uses Python's `time.sleep()` internally
- Takes one parameter: seconds (int or float)

### Testing
- Tested with `wait(1)`, `wait(2.5)`
- Created example game in `examples/demo_wait.quill`
- No performance issues observed

### Example Usage
\```Quill
say "Opening the ancient tomb..."
wait(2)
say "You hear a loud creak..."
wait(1)
say "The door swings open!"
\```
```

## 🐛 Bug Fix Guidelines

### For Bug Fixes
- Reference the issue number: "Fixes #123"
- Explain the root cause
- Describe your solution
- Add a test case if possible

### Example Bug Fix
```markdown
## Fix: Division by zero crash in calculator example

Fixes #45

### Problem
Calculator crashes when dividing by zero instead of showing error message.

### Root Cause
`interpreter.py` line 234 doesn't check denominator before division.

### Solution
Added check for zero denominator, returns error message instead.

### Testing
- Tested `10 / 0` → shows "Error: Cannot divide by zero"
- Tested `10 / 2` → still works correctly (returns 5)
```

## ✅ Checklist for Contributors

Before submitting a PR, ensure:

- [ ] Code works on your local machine
- [ ] No syntax errors or warnings
- [ ] Documentation updated (if needed)
- [ ] Examples added (if adding features)
- [ ] Commit messages are clear
- [ ] Branch is up to date with main
- [ ] PR description is complete

## 🤝 Code of Conduct

### Our Standards
- Be respectful and inclusive
- Welcome newcomers and beginners
- Provide constructive feedback
- Focus on what's best for the community
- Show empathy towards others

### Unacceptable Behavior
- Harassment or discriminatory language
- Personal attacks or trolling
- Publishing others' private information
- Spam or off-topic content

### Reporting Issues
If you experience or witness unacceptable behavior, please report it by opening an issue or contacting the maintainers.

## 📚 Resources

### Documentation
- [Keywords Reference](docs/Quill_KEYWORDS_REFERENCE.md)
- [Getting Started Guide](docs/GETTING_STARTED.md)
- [Language Reference](docs/LANGUAGE_REFERENCE.md)

### Examples
- Check `examples/` folder for working code
- Look at `games/` for complete game examples

### Need Help?
- Open an issue with the "question" label
- Check existing issues for similar questions
- Read the documentation first

## 🎓 First Time Contributors

Never contributed to open source before? Welcome! Here's how to start:

1. **Start Small**: Look for issues labeled `good-first-issue`
2. **Ask Questions**: Don't hesitate to ask for clarification
3. **Learn by Example**: Read existing code and PRs
4. **Take Your Time**: Quality over speed
5. **Have Fun**: Contributing should be enjoyable!

### Good First Issues
- Fix typos in documentation
- Add comments to existing code
- Create simple example programs
- Improve error messages
- Write tests for existing features

## 🏆 Recognition

Contributors will be:
- Listed in the project's README
- Credited in release notes
- Mentioned in documentation they helped create

## 📞 Contact

- **GitHub Issues**: For bugs and feature requests
- **Pull Requests**: For code contributions
- **Discussions**: For questions and ideas

## 📜 License

By contributing, you agree that your contributions will be licensed under the MIT License.

---

**Thank you for making Quill better!** 🎉

Every contribution, no matter how small, helps make programming more accessible to beginners worldwide.
