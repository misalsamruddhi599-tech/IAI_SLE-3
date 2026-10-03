

# AI Contribution Log: SLE-3 Architectural Design (Full C4 Model)


---

## 1. AI Tool Usage Summary :

* **AI Tool Utilized:**  Gemini
* **Primary Role:** Generative AI was used as a collaborative assistant for structural decomposition, C4 model abstraction framing, Draw.io diagram blueprinting, and technical documentation drafting.

---

## 2. Specific Scope of AI Assistance :

AI tools were leveraged across the following architectural stages:

1. **C4 Model Abstraction Breakdown:**
   - Assisted in mapping the SLE-2 benchmark code into the standard C4 hierarchy (Context, Container, Component, and Code levels).
   - Recommended appropriate container and component boundaries to separate I/O operations from timer measurement logic.

2. **Diagram Blueprinting & Connectivity Layouts:**
   - Provided formatted text layouts and directional arrow relationships ($A \to B$) for importing and constructing visual diagrams in Draw.io.
   - Suggested standardized C4 styling guidelines (e.g., color differentiation between external actors, core software boundaries, and internal components).

3. **Documentation Structure & Markdown Formatting:**
   - Helped format `README.md` and `AI_Contribution_Log.md` using clean Markdown tables, bold headers, and LaTeX math representations.
   - Assisted in drafting the architectural rationale for design decisions (such as micro-delay loops and reversed DFS adjacency handling).

---

## 3. Student Independent Contributions :

All core design validation, diagram generation, code execution, and report compilation were performed independently by the student:

* **System Execution & Metric Gathering:**  
  Ran `SLE2_BFS_vs_DFS.py` within local environment to execute all 3 test cases (Best Case: Goal $1$, Average Case: Goal $600$, Worst Case: Goal $1199$) across $3$ runs per case to verify timing measurements and expansion behavior.
* **Visual Diagram Creation (Draw.io):**  
  Manually constructed, styled, aligned, and exported all four C4 Model visual diagrams (`Level 1` to `Level 4`) using Draw.io based on system design rules.
* **Visual QA & Label Correction:**  
  Reviewed text labels, directional arrows, and module boundaries in all generated diagram PNG files to ensure 100% technical accuracy with Python code functionality.
* **Final Report Compilation:**  
  Assembled the complete `SLE-3_Architectural_Design_Report.pdf`, combining context explanations, diagram images, component tables, and design rationales.

---

## 4. Architectural Summary Matrix :

| C4 Level | Diagram Name | Primary Focus / System Scope | key Technical Elements |
| :--- | :--- | :--- | :--- |
| **Level 1** | System Context | External system boundaries & user interaction | Evaluator, Profiling Engine, Inputs ($Start, Goal, Runs$), Outputs ($Time, Expanded Nodes$) |
| **Level 2** | Container Diagram | High-level module breakdown & data flow | Input Module, Graph Generator, Profiling Core, Traversal Memory, Timeit Logger |
| **Level 3** | Component Diagram | Internal mechanics of Profiling Engine Core | Benchmark Controller, BFS Component, DFS Component, Goal Evaluator (2000-loop delay) |
| **Level 4** | Code Diagram | Mapping C4 components to Python code | `create_graph()`, `bfs()`, `dfs()`, `profile_algorithm()`, `print_case_result()` |

---

## 5. Architectural Rationale Verification :

| Design Decision | Purpose / Impact | Student Verification |
| :--- | :--- | :--- |
| **Decoupled Graph Generator** | Prevents dictionary initialization times from skewing algorithm runtime benchmarks. | Confirmed via `timeit` profiling isolation. |
| **2,000 Compute Delay Loop** | Stabilizes timer precision by overcoming OS-level CPU context switching noise. | Verified timing repeatability across 3 runs. |
| **Reversed DFS Neighbors** | Guarantees right-to-left deterministic tree traversal matching theoretical DFS behavior. | Verified stack output order during execution. |

---

## 6. AI Usage Statement & Student Declaration :

> **AI Usage Statement:**  
> AI tools (ChatGPT / Gemini) were used transparently for conceptual C4 model structuring, diagram text blueprinting, and documentation formatting support.

> **Student Declaration:**  
> I declare that all visual C4 architecture diagrams were created, styled, verified, and exported by me. All benchmarking code execution, data validation, design decision rationales, and report compilations represent my own authentic work.