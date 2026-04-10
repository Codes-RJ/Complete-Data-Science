# Contributing to Data Science Repository

Thank you for your interest in contributing to this Data Science Repository! 🎉 This document provides guidelines and instructions for contributing.

## 📋 Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How Can I Contribute?](#how-can-i-contribute)
- [Contribution Guidelines](#contribution-guidelines)
- [Style Guidelines](#style-guidelines)
- [Pull Request Process](#pull-request-process)

## Code of Conduct

By participating in this project, you agree to maintain a respectful and inclusive environment. Please:

- Use welcoming and inclusive language
- Be respectful of differing viewpoints
- Accept constructive criticism gracefully
- Focus on what's best for the community
- Show empathy towards other contributors

## How Can I Contribute?

### 🐛 Report Bugs
- Check existing issues before creating a new one
- Use the bug report template
- Include detailed steps to reproduce
- Specify your environment (OS, Python version, etc.)

### 💡 Suggest Enhancements
- Clearly describe the enhancement
- Explain why it would be valuable
- Provide examples if possible

### 📝 Add Content
- **New Topics**: Suggest sections not yet covered
- **Improve Existing Content**: Fix errors, add examples, clarify explanations
- **Add Projects**: Share your data science projects
- **Update Resources**: Add new books, courses, datasets
- **Interview Questions**: Add questions for any section

### 🔧 Fix Issues
- Look for issues labeled `good-first-issue` or `help-wanted`
- Comment that you're working on it

## Contribution Guidelines

### What We Accept

✅ **New Content**
- Tutorials and explanations
- Code examples and notebooks
- Practice exercises
- Interview questions
- Project ideas and implementations
- Resource recommendations

✅ **Improvements**
- Bug fixes in code or content
- Better explanations
- Additional examples
- Updated information
- Better formatting/structure

✅ **Translations**
- Translations to other languages (create a new branch)

### What We Don't Accept

❌ Spam or promotional content
❌ Plagiarized content
❌ Low-quality or incomplete contributions
❌ Breaking existing structure without discussion

## Style Guidelines

### File Naming
- Use `snake_case` for all files
- Numbers for ordering: `01_topic.md`, `02_topic.md`
- Descriptive names: `data_cleaning.md` not `dc.md`

### Markdown Formatting
- Use headings appropriately (`#`, `##`, `###`)
- Code blocks should specify language:
  \`\`\`python
  print("Hello, World!")
  \`\`\`
- Use tables for structured data
- Include examples where applicable

### Code Style

**Python**
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add comments for complex logic
- Include docstrings for functions

**R**
- Follow tidyverse style guide
- Use consistent naming conventions

**SQL**
- Use UPPERCASE for keywords
- Use lowercase for table/column names
- Format queries for readability

### Structure for Each Section

Each topic should generally follow this structure:

```markdown
# Topic Title

## Overview
Brief introduction

## Prerequisites
What learners should know before

## Key Concepts
Main concepts covered

## Code Examples
Practical examples

## Practice Exercises
Hands-on tasks

## Interview Questions
Common questions asked

## Additional Resources
Links for further learning
```

## Pull Request Process

### Step 1: Fork & Clone
```bash
# Fork the repository on GitHub
# Then clone your fork
git clone https://github.com/your-username/Data-Science-Repository.git
cd Data-Science-Repository

# Add upstream remote
git remote add upstream https://github.com/original-owner/Data-Science-Repository.git
```

### Step 2: Create Branch
```bash
# Create a descriptive branch name
git checkout -b feature/add-pandas-advanced
# or
git checkout -b fix/excel-formula-error
```

### Step 3: Make Changes
- Follow style guidelines
- Test your code if applicable
- Update documentation as needed

### Step 4: Commit
```bash
# Use conventional commit messages
git add .
git commit -m "feat: add advanced pandas tutorial"
git commit -m "fix: correct excel formula example"
git commit -m "docs: update contributing guide"
```

**Commit Message Format:**
- `feat:` New content or feature
- `fix:` Bug fix or correction
- `docs:` Documentation updates
- `style:` Formatting changes
- `refactor:` Code/content restructuring
- `test:` Adding tests
- `chore:` Maintenance tasks

### Step 5: Push & Create PR
```bash
git push origin feature/add-pandas-advanced
```

Then:
1. Go to the repository on GitHub
2. Click "Compare & pull request"
3. Fill in the PR template
4. Link any related issues

### Step 6: Review Process
- Maintainers will review your PR
- Address any requested changes
- Once approved, it will be merged

## Adding New Sections

If you want to add a completely new section:

1. **Open an issue first** discussing the proposed section
2. Wait for maintainer approval
3. Follow existing numbering pattern
4. Create a README.md for the section
5. Update the main README.md with links
6. Maintain consistent structure

## Adding Projects

When adding projects:

1. Place in appropriate level folder: `16_projects/01_beginner/`, `02_intermediate/`, or `03_advanced/`
2. Include:
   - Project description
   - Dataset source
   - Step-by-step guide
   - Expected outcomes
   - Solution/approach (if applicable)
3. Link to any notebooks in the `notebooks/` folder

## Recognition

Contributors will be:
- Listed in the CONTRIBUTORS.md file
- Acknowledged in release notes
- Featured in the repository README (for significant contributions)

---

**Thank you for contributing to making Data Science education accessible to everyone! 🙏**

*Happy Contributing! 🚀*