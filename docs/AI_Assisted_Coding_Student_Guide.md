# Learning to Code with Chat LLMs and AI Coding Agents

**A short student guide | Introduction to Data Science | MSc in Data Science for Social Sciences | University of Aveiro**  
**Updated:** 21 October 2026

## 1. What you should learn

Use a conversational large language model (LLM) or a coding agent in Visual Studio Code (VS Code) to **formulate programming tasks, develop Python code, understand its design, execute it, diagnose errors, and evaluate results**. This is a guide to AI-assisted programming and learning, *not* to any particular data-science method.

A chat LLM can explain concepts and suggest code. An IDE-integrated agent (such as GitHub Copilot, Codex, or Claude Code) may also inspect project files, create or modify code, and run commands, subject to its access and permissions. **The goal is not simply to obtain working code: you must learn why it works, when it may fail, and how to adapt it yourself.**

## 2. A practical learning workflow

1. **Specify the task.** Describe the question, available files, data columns, intended outputs, Python experience, permitted libraries, and what would count as success. Use anonymised or synthetic examples when appropriate.
2. **Discuss the approach.** Ask the assistant for a short implementation plan, its assumptions, and one simpler alternative. Request an explanation of unfamiliar concepts before choosing an approach.
3. **Ask it to implement the code.** Explicitly instruct the agent to create or edit named files, write small readable functions, and include clear run instructions. Keep changes limited to the agreed task. A plan is *not* the final deliverable.
4. **Turn the implementation into a lesson.** Ask what each function accepts and returns, how data flow through the program, why particular operations or libraries were selected, and what alternatives would change. Ask for a small worked example and a question you must answer independently.
5. **Run, inspect, and debug.** Execute the code on a small example; check intermediate outputs and edge cases. When something fails, provide the *actual* error and ask for an explanation of its cause as well as a correction. Distinguish tests genuinely executed from tests only proposed.
6. **Consolidate learning.** Modify one part of the solution yourself, explain it in your own words, and record the AI assistance used. Review file changes and retain version-control checkpoints.

**Good requests include:** task + context + constraints + expected output + evidence of correctness + requested explanation. Avoid vague requests such as "do my project" or "use the best model".

**Keep project context concise:** Maintain a `README.md` stating the task, files, dependencies, and how to run the code. Optionally, add tool-specific project instructions ([`AGENTS.md` for Codex](https://developers.openai.com/codex/guides/agents-md/) or [`CLAUDE.md` for Claude Code](https://code.claude.com/docs/en/memory)) asking the agent to make minimal changes, explain decisions, and report tests. These instructions guide the agent; they do not ensure compliance or correctness.

## 3. Reusable prompts: from idea to working code

### A. Plan and learn before implementation

> I am an introductory Python student working on **[goal]**. My project has **[files/data structure]**; I want **[observable output]**, using **[libraries/constraints]**. Explain the key programming concepts I need. Propose a minimal implementation plan, identify assumptions, and compare it briefly with one simpler alternative. **Do not edit files yet.**

### B. Implement an agreed step

> Now **implement step [X]** in **[file/path]**. Write readable Python code with descriptive names, a short docstring for each function, and only necessary comments. Show how to run it, provide a small test using synthetic data, and state the expected output. Change no unrelated files, and ask before installing packages, accessing external services, or overwriting data. When finished, summarise exactly what you changed.

### C. Make the agent teach the code back to you

> Teach me the implementation you just created at an introductory level. Explain (1) the purpose of each function, (2) important lines and Python concepts, (3) the data flow from input to output, (4) why you chose this solution rather than a plausible alternative, and (5) two ways it could fail. Walk through a tiny example. Then ask **two short comprehension questions** and propose **one small change for me to implement without AI**. Do not claim the code is correct solely because you wrote it.

### D. Debug with evidence

> I ran **[command]** and obtained **[error/actual output]**, but expected **[expected output]**. Explain the likely cause, show how to check your hypothesis, make the *smallest justified correction*, and describe how we can test that it works. If you cannot execute the code, say so explicitly.

**First exercise:** Ask an assistant to create a Python script that reads a small CSV and reports its number of rows, missing values per column, and duplicate records. Run the script; explain each operation; then independently extend it to calculate one additional statistic. No text-mining knowledge is required.

## 4. Reading guide (freely accessible documentation first)

### Core readings: start here

1. **Genatowski, E. (2024). [*Introduction to Artificial Intelligence Prompt Engineering*](https://campus.dariah.eu/resources/hosted/introduction-to-ai). DARIAH-Campus.** An openly licensed introductory module particularly relevant to Social Sciences and Humanities. **Read for:** precise instructions, context, and critical evaluation.
2. **Gadesha, V. (2026). [*The 2026 Guide to Prompt Engineering*](https://www.ibm.com/think/prompt-engineering). IBM.** Broad, freely readable overview of prompting and contextual information. **Read critically:** claims that prompting replaces programming are oversimplified.
3. **Microsoft. (n.d.). [*Best practices for using AI in VS Code*](https://code.visualstudio.com/docs/agents/best-practices).** Practical guidance on choosing chat, planning, or agent workflows; giving context; requesting implementation; and checking changes. **Especially recommended.**
4. **GitHub. (n.d.). [*Prompt engineering for GitHub Copilot*](https://docs.github.com/en/copilot/concepts/prompting-and-context/prompt-engineering).** Concrete examples of scoped requests, examples, relevant files, progressive tasks, and iteration. Applies beyond Copilot.
5. **Choose one tool and read its official onboarding documentation:** [GitHub Copilot in VS Code](https://code.visualstudio.com/docs/setup/copilot), [OpenAI Codex IDE extension](https://developers.openai.com/codex/ide), or [Anthropic Claude Code in VS Code](https://code.claude.com/docs/en/vs-code). For more advanced guidance, consult [Anthropic's Claude Code best practices](https://code.claude.com/docs/en/best-practices). You do **not** need to install or pay for all three.

### Supplementary practical readings from the proposed bibliography

6. **Shamim, A. (2025). [*Prompt Engineering Guide for Data Scientists & ML Engineers*](https://adilshamim8.medium.com/prompt-engineering-guide-for-data-scientists-ml-engineers-00f2ebf69d8e). Medium.** Adapt its concrete prompts for data preparation, analysis, code development and debugging. **Access may vary on Medium.**
7. **Shivanandhan, M. (2026). [*Codex vs Claude Code: Which AI Coding Assistant to Choose*](https://www.freecodecamp.org/news/codex-vs-claude-code-which-ai-coding-assistant-to-choose/). freeCodeCamp.** A readable comparison of working styles, **not** an empirical demonstration that one tool is pedagogically superior.
8. **Cholassery, A. (2026). [*How to Use Claude Code in 2026: The Complete Developer Guide*](https://archisacademy.com/tr/blogs/how-to-use-claude-code-in-2026-the-complete-developer-guide). Archi's Academy.** Optional tutorial on practical agent workflows. Cross-check technical details against official documentation; this is also a commercial training website.
9. **TeamoRouter. (2026). [*Claude Code Setup for Beginners: Install & Configure in 2026*](https://teamorouter.com/blogs/claude-code-install-configure-beginners-2026).** Optional setup walkthrough. **Commercial content promoting an API gateway:** prefer the official Anthropic instructions for installation and account configuration.
10. **Nóbrega, S. (2025). [*Become a Better Data Scientist with These Prompt Engineering Tips and Tricks*](https://towardsdatascience.com/become-a-better-data-scientist-with-these-prompt-engineering-hacks/). Towards Data Science.** Optional prompts for planning and exploratory work. The title/link were corroborated through publisher-related posts, but the full article could not be independently inspected; access may be restricted.

*Availability note:* These are online learning resources, not necessarily open-source software or peer-reviewed research. Official documentation is freely readable; usage of coding agents may require an eligible account, a subscription, or credits. Interfaces and pricing change.

## 5. Academic expectations

**Be able to demonstrate:** the code runs; you understand the functions and outputs; choices and assumptions are justified; failures and limitations are discussed; and another student could reproduce the result. Record meaningful use of AI (tool, task, contribution, and independent checks) in your project documentation. Never upload sensitive, personal, copyrighted-restricted, or confidential datasets to external services without appropriate permission.

**Learning test:** *If the assistant were unavailable, could you explain the solution, change a small part of it, and identify a plausible error?* If not, request another explanation and practise before proceeding.
