# **Copper File Format**

### **A human-readable, low-stress format for structured data and configuration**

**Copper**, or `.copr`, is a lightweight data format designed to be *pleasant for humans* and *simple for parsers*.  It replaces the punctuation maze of YAML, JSON, and XML with clean section headers, plain key-value pairs, and visual structure that mirrors how people actually write notes. It’s designed to be easy for humans to read and easy for machines to parse — a middle ground between free-form writing and data serialization.

Copper isn’t a markup language or a programming language. It’s a **comment system for thought** — a way to store structured ideas without nesting or syntax noise.

---

### **Philosophy**

* **Human first:** readable with a plain text editor.

* **Flat, not nested:** no hierarchies to get lost in.

* **Collaborative:** multiple people or AIs can work in the same file.

* **Durable:** text stays meaningful even without special tools.

* **Extensible:** structured enough for automation, simple enough for writing.

---

### **File Concepts**

| Symbol | Purpose |
| ----- | ----- |
| `[=Section=]` | Section header. Use any number of `=` for decoration. |
| `[Subsection]` | Next topic. Sequential, never nested. |
| `key: value` | Simple data pair. |
| `user@` | Marks a person or agent. All following text belongs to them until another `user@` appears. |
| `user@<timestamp>` | Later or asynchronous note from the same user. |
| `{code}` … `{/code}` | Multiline code cell. |
| `{commands}` … `{/commands}` | Machine-readable actions or instructions. |
| Plain text | Default content — free comments, reasoning, or conversation. |

---

### **Design Rules**

1. **No nesting.** Each section is flat. If you need subtopics, start a new `[Subsection]`.

2. **Persistent authorship.** Text remains under the current `user@` until changed.

3. **Explicit closures.** Only braces `{}` use start/end markers. No ambiguous brackets.

4. **Readable structure.** Equal signs and blank lines are for clarity, not logic.

5. **Commandable.** Anything inside `{commands}` can drive scripts or build tools.

---

### **Example**

`[=FlowOS Module Runtime=]`  
`project: FlowOS`  
`version: 1.1`  
`created: 2025-10-27`

`GPT@`  
`Podman integration tested; rootless mode confirmed.`  
`{commands}`  
`promote: runtime_container`  
`{/commands}`

`Don@`  
`Need to verify volume mount persistence.`  
`{code}`  
`podman volume inspect gameblock_data`  
`{/code}`

`[UI Rendering]`  
`========`  
`This line of equals is only a visual divider.`

`GPT@`  
`No nested structures; treat each topic as its own section.`  
`{commands}`  
`create: RendererBlock`  
`{/commands}`

---

### **Why Copper**

* Works as plain text on any platform.

* Perfect for AI/human co-authoring, journaling, or collaborative coding notebooks.

* Easily parsed with simple regex or line scanners — no parser generators needed.

* Compatible with version control; diffs are obvious.

* Converts cleanly to JSON, Markdown, or HTML if you ever need export.

---

### **Future Goals**

* Build Copper-aware editors and viewers.

* Add lightweight schema validation for `{commands}`.

* Provide official converters for Markdown and JSON.

---

## **📜 License**

**Code (parsers, examples, tools):**  
 MIT License © 2025 *\[Your Name\]*

**Copper (.copr) format specification:**  
 Released under Creative Commons Zero 1.0 Universal (CC0)

This means you can use Copper freely in open-source or commercial projects, modify it, and create your own parsers or extensions — no permission required.

---

## **🧡 Acknowledgment**

Copper is named after *Copper*, the developer’s cat — a very handsome boy and tireless supervisor of all late-night coding sessions.

---

