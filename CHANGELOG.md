# Changelog

All notable changes to this project will be documented in this file.

## [0.0.3a3] - 2026-05-18

### Removed
- Remove the deprecated `pwcall` keyword argument and its internal processing from the `PasswdFile` constructor.

### Changed
- Shift password testing strategy in doctests (`get_started_passwd_file.rst`, `get_started_programms.rst`) from argument injection to direct monkeypatching of standard `getpass.getpass`.
- Clean up the Sphinx configuration (`conf.py`) by removing the unused `platformdirs` intersphinx mapping.
- Switch from internal `securify` type mappings to standard library `collections.abc.Callable` types.

---

## [0.0.3a1] - 2026-05-17
### Added
- Integrated `ftw-securify` for protected password input via TTY.
- Major documentation refactor to support the updated package structure.


## [0.0.3a1] - Unreleased
### Added
- Integrated `ftw-securify` for protected password input via TTY.
- Major documentation refactor to support the updated package structure.

### Changed
- Updated packaging metadata to modern standards (`pyproject.toml`).
- Refactored core modules to improve internal consistency.

---

## [0.0.2] - 2026-05-14
### Added
- Implemented full API documentation following PEP 257 and Sphinx rules for:
  - `programms`
  - `passwd_file`
  - `cli_parser`
  - `protocols`

### Changed
- Restructured package: Moved CLI logic to the `programms` module.
- Optimized Sphinx configuration for smoother documentation builds.

---

## [0.0.1] - 2026-05-14
### Added
- Initial commit: Basic structure of the `ftw-pki-password` package.
