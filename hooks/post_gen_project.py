#!/usr/bin/env python3
"""Post-generation hook for SDD template."""

import os
import subprocess

def main():
    # Make scripts executable
    scripts_dir = os.path.join(os.getcwd(), "scripts")
    for script in os.listdir(scripts_dir):
        script_path = os.path.join(scripts_dir, script)
        os.chmod(script_path, 0o755)

    # Initialize git repository
    subprocess.run(["git", "init"], check=True, capture_output=True)
    subprocess.run(["git", "add", "."], check=True, capture_output=True)
    subprocess.run(
        ["git", "commit", "-m", "Initial SDD project structure"],
        check=True,
        capture_output=True
    )

    print("""
================================================================================
  {{ cookiecutter.project_name }} created successfully!
================================================================================

Next steps:

  1. Review CLAUDE.md (the constitution)
  2. Read docs/FOR_HUMANS.md or docs/FOR_AGENTS.md
  3. Run ./scripts/sdd preflight to check your environment
  4. Start with exploration - validate your assumptions!

Workflow: Explore → Spec → Plan → Impl → Verify

Commands:
  ./scripts/sdd help           Show all commands
  ./scripts/sdd preflight      Check environment
  ./scripts/sdd spec-release   Create a spec version

================================================================================
""")

if __name__ == "__main__":
    main()
