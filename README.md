# AI Cheat Sheets

Sixteen visual cheat sheets on AI engineering, machine learning, the math behind it, computer science and software engineering. Most compare six approaches with worked-example diagrams, trade-offs and a which-one-to-use table; the rest use one of the other formats below.

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
| 12 | [Hash-table collision handling](12-hash-tables/) | Same Keys. Different Tables. Different Speed. | Tue Sep 29 |
| 13 | [BatchNorm vs LayerNorm](13-batchnorm-layernorm/) | BatchNorm vs LayerNorm: Same Formula. Different Axis. | Sun Oct 11 |
| 14 | [Deployment strategies](14-deployment/) | Same Release. Different Rollouts. Different Risk. | Mon Oct 12 |
| 15 | [From RNNs to Transformers](15-rnns-transformers/) | How Models Learned to Read. 1997 → 2020 | Tue Oct 13 |
| 16 | [Sigmoid activation](16-sigmoid/) | Sigmoid: Squash Any Number to (0, 1) | Wed Oct 14 |

Each folder holds the full-size image (1800 px wide), the LinkedIn post and the image alt text.

## Formats

- **Comparison:** six (or nine) approaches to one job, each with a worked-example diagram, pros and cons, and a which-one-to-use table.
- **Deep dive:** one concept: the idea, its formula, a worked example, two diagrams, where it's used, and its strengths and limits.
- **Face-off:** two alternatives side by side, with a chart that puts numbers on the difference, a table of key differences and when to use each.
- **Gallery:** six to ten variants of one thing, each with its own small flow diagram, one strength and one watch-out.
- **Timeline:** dated milestones, each with a small diagram, what it introduced and why it mattered.

Any sheet can also be one part of a series: the series list sits at the top and the next part is named at the bottom.

## How the images are made

Each sheet is stored as data in `src/sheets/`. A GitHub Action (`.github/workflows/render.yml`) renders it with `src/render_sheet.py` and headless Chromium, and commits the PNG into the sheet's folder. The `layout` field in the data picks the format. Edit a JSON file and push to re-render.
