# Excel-Convertor
# Excel Convertor

> A configurable open-source Python tool for transferring data from user Excel files into predefined Excel templates.

![Python](https://img.shields.io/badge/python-3.11+-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

---

## Features

- Read user Excel (.xlsx)
- Preserve template formatting
- Configurable mapping using YAML
- Persian date transformation
- Gender conversion
- Marital status conversion
- Validation engine
- Logging
- Command-line interface
- Extensible transformation system

---

## Project Structure

```text
excel-convertor/
```

---

## Installation

```bash
git clone https://github.com/YOUR_USERNAME/excel-convertor.git

cd excel-convertor

python -m venv .venv
```

Windows

```bash
.venv\Scripts\activate
```

Linux/macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

## Usage

```bash
python -m excel_convertor.cli \
    --input users.xlsx \
    --template templates/main.xlsx \
    --mapping mapping/default_mapping.yaml \
    --output output/result.xlsx
```

---

## Roadmap

- [x] Repository foundation
- [ ] Excel Reader
- [ ] Validator
- [ ] Mapping Engine
- [ ] CLI
- [ ] Tests
- [ ] GitHub Actions

---

## Contributing

Pull requests are welcome.

---

## License

MIT
