\# Contributing to STMS



\## Development Guidelines



1\. Keep changes focused on one feature or improvement.

2\. Use a separate Git branch for each feature or documentation change.

3\. Write clear commit messages that describe the change.

4\. Run the automated tests before pushing changes.

5\. Open a Pull Request against the `main` branch.

6\. Review the changes before merging the Pull Request.



\## Branch Naming



Use descriptive branch names:



\- `feature/` for new features

\- `fix/` for bug fixes

\- `docs/` for documentation changes

\- `test/` for test-related changes



Examples:



\- `feature/task-validation`

\- `docs/project-guide`

\- `test/task-priority`



\## Testing



Run the tests from the project root:



```bash

python -m pytest -v

```



Only submit changes after checking the test results.



\## Pull Request Checklist



\- \[ ] Changes are focused and clearly described.

\- \[ ] Automated tests pass.

\- \[ ] Commit messages are meaningful.

\- \[ ] The target branch is `main`.

\- \[ ] The changes have been reviewed before merging.

