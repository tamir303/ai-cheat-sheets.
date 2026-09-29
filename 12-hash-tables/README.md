# Same Keys. Different Tables. Different Speed.

**Topic:** Hash-table collision handling  
**LinkedIn:** Posted Tue Sep 29 2026

![Cheat sheet titled 'Same Keys. Different Tables. Different Speed.' comparing six hash-table collision strategies: separate chaining, linear probing, quadratic probing, double hashing, Robin Hood hashing and cuckoo hashing. Each has a worked-example diagram, pros and cons, and relative latency and cost, followed by a table of which strategy to use when.](12-hash-tables.png)

## LinkedIn post

```text
Same keys, six collision strategies, six different lookup speeds.

Every dict, set and map eventually hashes two keys to the same slot. What happens next decides memory use, cache hits and the worst-case lookup time.

The short version:
→ Frequent deletes, large values: separate chaining
→ Small keys, fastest average lookup: linear probing or Robin Hood
→ Flat array, less clustering: quadratic probing
→ Table must run nearly full: double hashing or cuckoo
→ Hard worst-case lookup bound: cuckoo hashing

Rule of thumb: watch the load factor before you swap the scheme.

Which one does your language's built-in map use?

#DataStructures #Algorithms #HashTables #ComputerScience
```

## Alt text

Cheat sheet titled 'Same Keys. Different Tables. Different Speed.' comparing six hash-table collision strategies: separate chaining, linear probing, quadratic probing, double hashing, Robin Hood hashing and cuckoo hashing. Each has a worked-example diagram, pros and cons, and relative latency and cost, followed by a table of which strategy to use when.
