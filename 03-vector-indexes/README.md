# Same Embeddings. Different Indexes. Different Trade-offs.

**Topic:** Vector index types  
**LinkedIn:** Tue Oct 6 2026, 09:00 (Israel time)

![Cheat sheet titled 'Same Embeddings. Different Indexes. Different Trade-offs.' comparing six vector index types: flat, IVF, HNSW, product quantization, LSH and DiskANN. Each has a diagram, pros and cons, and relative latency and cost, followed by a table of which index to use when.](03-vector-indexes.png)

## LinkedIn post

```text
Same embeddings, six index types, six different speed/recall/memory trade-offs.

Every vector database answers nearest-neighbour queries, but the index decides how much recall you give up for speed and memory.

The short version:
→ Small corpus that must be exact: flat
→ Low latency and high recall, RAM is fine: HNSW
→ Speed vs recall you can tune per query: IVF
→ Tight memory budget: product quantization
→ Bigger than RAM on one machine: DiskANN
→ Streaming data, no training step: LSH

Rule of thumb: benchmark recall@10 against a flat index before trusting any default.

Which index do you run in production?

#VectorSearch #RAG #LLM #AIEngineering
```

## Alt text

Cheat sheet titled 'Same Embeddings. Different Indexes. Different Trade-offs.' comparing six vector index types: flat, IVF, HNSW, product quantization, LSH and DiskANN. Each has a diagram, pros and cons, and relative latency and cost, followed by a table of which index to use when.
