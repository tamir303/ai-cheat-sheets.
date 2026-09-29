# AI Cheat Sheets

Eleven visual cheat sheets on AI engineering, machine learning, the math behind it, computer science and software engineering. Each compares six approaches with worked-example diagrams, trade-offs and a which-one-to-use table.

| # | Topic | Sheet title | LinkedIn |
|---|---|---|---|
| 01 | [RAG chunking strategies](01-rag-chunking/) | Same Document. Different Chunkers. Different Recall. | Sat Sep 26 |
| 02 | [Parameter-efficient fine-tuning](02-peft/) | Same Base Model. Different Methods. Different Trade-offs. | Sun Sep 27 |
| 03 | [Vector index types](03-vector-indexes/) | Same Embeddings. Different Indexes. Different Trade-offs. | Mon Sep 28 |
| 04 | [LLM output evaluation](04-llm-evaluation/) | Same Output. Different Evaluators. Different Verdicts. | Tue Sep 29 |
| 05 | [LLM quantization formats](05-quantization/) | Same Model. Different Precision. Different Footprint. | Wed Sep 30 |
| 06 | [Prompting techniques](06-prompting/) | Same Question. Different Prompts. Different Accuracy. | Sat Oct 17 |
| 07 | [LLM caching strategies](07-caching/) | Same Request. Different Caches. Different Savings. | Mon Oct 5 |
| 08 | [LLM post-training and alignment methods](08-post-training/) | Same Raw Model. Different Feedback. Different Behavior. | Tue Oct 6 |
| 09 | [LLM tokenization algorithms](09-tokenization/) | Same Sentence. Different Tokenizers. Different Tokens. | Wed Oct 7 |
| 10 | [Prompt-injection defenses](10-prompt-injection/) | Same Injection. Different Defenses. Different Risk. | Thu Oct 8 |
| 11 | [LLM response caching](11-response-caching/) | Same Prompt. Different Caching. Different Latency. | Sun Oct 4 |

Each folder holds the full-size image (1800 px wide), the LinkedIn post and the image alt text.

## How the images are made

Each sheet is stored as data in `src/sheets/`. A GitHub Action (`.github/workflows/render.yml`) renders it with `src/render_sheet.py` and headless Chromium, and commits the PNG into the sheet's folder. Edit a JSON file and push to re-render.