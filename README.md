# **Copper File Format**

### **A human-readable, low-stress format for structured data and configuration**

**Copper**, or `.copr`, is a lightweight data format designed to be *pleasant for humans* and *simple for parsers*.  
 It replaces the punctuation maze of YAML, JSON, and XML with clean section headers, plain key-value pairs, and visual structure that mirrors how people actually write notes.

---

## **✨ Core Philosophy**

1. **Readable first.** If you can’t edit it in Notepad without fear, it’s not Copper.

2. **Predictable structure.** Everything is just sections, objects, and key-value pairs.

3. **Minimal syntax.** No nesting horror, no dangling commas, no indentation rituals.

4. **UTF-8 text forever.** It should work on every system, from mainframe to mobile.

---

## **🧩 Basic Example**

`{== Character ==}`  
`[Hero]`  
`name: Rina`  
`role: Pilot`  
`skills: Navigation, Repair`

`[Companion]`  
`name: Jax`  
`species: Droid`  
`notes: Can cook but refuses to.`

`{== Ship ==}`  
`model: Starling IV`  
`registry: 88-RZC`  
`crew: Rina, Jax`

Readable. Diff-friendly. And trivial to parse.

---

## **🧠 File Structure Summary**

| Element | Syntax | Meaning |
| ----- | ----- | ----- |
| **Section** | `{== Name ==}` | Top-level grouping |
| **Subsection** | `[-- Name --]` | Nested grouping |
| **Key-Value Pair** | `key: value` | Data assignment |
| **List (inline)** | `skills: Navigation, Repair` | Comma-separated |
| **List (block)** | `skills:\n - Navigation` | Multi-line form |
| **Multiline text** | \` | `after`:\` |
| **Comments** | `#` or `//` | Ignored by parser |

---

## **💡 Use Cases**

* Configuration files for applications or games

* Machine learning metadata or pattern libraries

* Worldbuilding data for RPG systems

* Any situation where YAML feels too brittle and JSON too ugly

---

## **🛠️ Example Parser (Python)**

`from pathlib import Path`  
`from pprint import pprint`

`def parse_copr(path):`  
    `data, section, subsection = {}, None, None`  
    `lines = Path(path).read_text(encoding="utf-8").splitlines()`  
    `for line in lines:`  
        `line = line.strip()`  
        `if not line or line.startswith(("#", "//")):`  
            `continue`  
        `if line.startswith("{") and line.endswith("}"):`  
            `section = line.strip("{}= ").strip()`  
            `data[section] = {}`  
            `subsection = None`  
        `elif line.startswith("[") and line.endswith("]"):`  
            `subsection = line.strip("[]- ").strip()`  
            `data[section][subsection] = {}`  
        `elif ":" in line:`  
            `k, v = [p.strip() for p in line.split(":", 1)]`  
            `target = data[section][subsection] if subsection else data[section]`  
            `target[k] = v`  
    `return data`

`pprint(parse_copr("example.copr"))`

---

## **📜 License**

**Code (parsers, examples, tools):**  
 MIT License © 2025 *\[Your Name\]*

**Copper (.copr) format specification:**  
 Released under Creative Commons Zero 1.0 Universal (CC0)

This means you can use Copper freely in open-source or commercial projects, modify it, and create your own parsers or extensions — no permission required.

---

## **🧭 Project Goals**

* Publish a formal 1.0 specification.

* Provide parsers in Python, Rust, and JavaScript.

* Offer a validator CLI and a VSCode syntax highlighter.

* Encourage use in data-driven game design and AI pipelines.

---

## **🧡 Acknowledgment**

Copper is named after *Copper*, the developer’s cat — a very handsome boy and tireless supervisor of all late-night coding sessions.

---
