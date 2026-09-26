# Same Document. Different Chunkers. Different Recall.

**Topic:** RAG chunking strategies  
**LinkedIn:** Tue Sep 29 2026, 09:00 (Israel time)

![Cheat sheet titled 'Same Document. Different Chunkers. Different Recall.' comparing six RAG chunking strategies: fixed-size with overlap, recursive split, structure-aware, semantic, late chunking and proposition chunking. Each has a diagram, pros and cons, and relative indexing time and cost, followed by a table of which chunker to use when.](01-rag-chunking.png)

## LinkedIn post

```text
Same document, six ways to split it, six different retrieval results.

Most RAG quality problems start before the embedding model: a retriever can only return the chunks you gave it.

The short version:
→ Quick baseline: fixed-size chunks with overlap
→ Mixed prose: recursive splitting
→ Docs with headings: structure-aware splitting
→ Long docs that drift across topics: semantic chunking
→ Pronouns that need wider context: late chunking
→ Fact lookup: proposition chunking

Rule of thumb: start with recursive splitting, then measure recall@k before paying for smarter chunkers.

Which chunking strategy works best on your documents?

#RAG #LLM #GenAI #AIEngineering
```

## Alt text

Cheat sheet titled 'Same Document. Different Chunkers. Different Recall.' comparing six RAG chunking strategies: fixed-size with overlap, recursive split, structure-aware, semantic, late chunking and proposition chunking. Each has a diagram, pros and cons, and relative indexing time and cost, followed by a table of which chunker to use when.
