# Environment Setup

This document details environment requirements for {{ cookiecutter.project_name }}.

---

## Quick Start

```bash
# 1. Run preflight check
./scripts/sdd preflight

# 2. Fix any issues reported

# 3. Ready to work
```

---

## Requirements

### Git

Git is required for the SDD branching workflow.

```bash
# Check
git --version

# Install (macOS)
xcode-select --install

# Install (Ubuntu)
sudo apt install git
```

### Python (Optional)

If your project uses Python:

```bash
# Check version
python3 --version

# Recommended: Use uv for environment management
pip install uv

# Create virtual environment
uv venv --python {{ cookiecutter.python_version }}
source .venv/bin/activate

# Install dependencies
uv pip install -r requirements.txt
```

---

## Project-Specific Setup

Add your project-specific setup instructions here:

```bash
# Example: Database setup
# createdb myproject

# Example: Environment variables
# cp .env.example .env
# Edit .env with your values

# Example: API credentials
# Configure ~/.config/myproject/credentials.json
```

---

## Verification

After setup, verify everything works:

```bash
# Run preflight
./scripts/sdd preflight

# All checks should pass
```

---

## Troubleshooting

### Common Issues

**Git not initialized:**
```bash
git init
```

**Python version mismatch:**
```bash
# Install pyenv for version management
curl https://pyenv.run | bash
pyenv install {{ cookiecutter.python_version }}
pyenv local {{ cookiecutter.python_version }}
```

**Missing directories:**
```bash
mkdir -p specs plans knowledge
```

---

## Getting Help

If setup issues persist:
1. Check CLAUDE.md for project-specific requirements
2. Review error messages from `./scripts/sdd preflight`
3. Ask in project communication channels
