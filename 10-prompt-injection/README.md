# Same Injection. Different Defenses. Different Risk.

**Topic:** Prompt-injection defenses  
**LinkedIn:** Sun Oct 4 2026, 12:00 (Israel time)

![Cheat sheet titled 'Same Injection. Different Defenses. Different Risk.' comparing six prompt-injection defenses: injection classifiers, spotlighting, output filtering, least-privilege tools, dual-LLM isolation and human approval. Each has a worked-example diagram, pros and cons, and relative latency and cost, followed by a table of which defense to use when.](10-prompt-injection.png)

## LinkedIn post

```text
Same injection, six defenses, six different levels of risk.

Prompt injection hides instructions in text your model reads: a web page, an email, a PDF. No single defense stops it, so you layer them.

The short version:
→ Scan inputs and retrieved docs: injection classifier
→ Mark outside text as data: spotlighting
→ Stop leaks through links: output filtering
→ Agents that can act: least-privilege tools
→ Agents reading untrusted inboxes: dual-LLM isolation
→ Payments or deletes: human approval

Rule of thumb: assume the model will be fooled, and design so a hijacked agent can't reach anything that matters.

Which layer are you missing?

#AISecurity #LLM #PromptInjection #AIAgents
```

## Alt text

Cheat sheet titled 'Same Injection. Different Defenses. Different Risk.' comparing six prompt-injection defenses: injection classifiers, spotlighting, output filtering, least-privilege tools, dual-LLM isolation and human approval. Each has a worked-example diagram, pros and cons, and relative latency and cost, followed by a table of which defense to use when.
