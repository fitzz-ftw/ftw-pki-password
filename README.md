# ftw-pki-password

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: LGPL v2.1](https://img.shields.io/badge/License-LGPL_v2.1-blue.svg)](https://www.gnu.org/licenses/old-licenses/lgpl-2.1.html)
[![Coverage: 100%](https://img.shields.io/badge/coverage-100%25-brightgreen.svg)](#)

A dedicated security tool within the **ftw-pki** suite, designed to manage and encapsulate high-complexity CA passphrases.

## 🛠 Features

* **Passphrase Transformation:** Converts large-scale passphrase files (e.g., 80+ characters for Root CAs) into secure, encrypted containers.
* **Multi-Operator Support:** Enables multiple individuals to access a central CA passphrase using their own personal passwords, ensuring accountability and security.
* **CA Integrity:** Specifically built to meet the requirements of `caroot` (passphrases ~80+ chars) and `intermed` (passphrases ~50+ chars).
* **Encrypted Storage:** Utilizes specialized modules for the secure storage and handling of sensitive secrets.


## 📖 Documentation & Usage

As this tool directly handles the security of Root and Intermediate CAs, understanding its mechanisms is vital:

* **CLI Interface:** Provides an intuitive command-line interface. Use `--help` after installation to see available commands and options.
* **Technical Details:** Full documentation regarding encryption logic and role separation is available in the `doc/source/` directory and can be built via Sphinx.

---
© 2026 ftw-pki Contributors
