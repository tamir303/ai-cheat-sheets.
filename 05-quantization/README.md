# Same Model. Different Precision. Different Footprint.

**Topic:** LLM quantization formats  
**LinkedIn:** Tue Oct 13 2026, 09:00 (Israel time)

![Cheat sheet titled 'Same Model. Different Precision. Different Footprint.' comparing six LLM quantization formats: INT8 (LLM.int8), GPTQ, AWQ, GGUF, NF4 and FP8. Each has a worked-example diagram, pros and cons, and relative latency and memory, followed by a table of which format to use when.](05-quantization.png)

## LinkedIn post

```text
Same model, six quantization formats, six different memory and speed trade-offs.

Quantization is how a 7B model goes from about 14 GB (16-bit) to about 3.5 GB (4-bit). The format decides how much quality you keep and where it can run.

The short version:
→ Quick 8-bit load, no calibration: LLM.int8
→ 4-bit serving on GPUs: GPTQ or AWQ
→ Laptops, CPUs and Macs: GGUF with llama.cpp or Ollama
→ QLoRA fine-tuning: NF4
→ Max throughput on Hopper/Ada GPUs: FP8

Rule of thumb: do the memory math (params × bits ÷ 8), then check quality on your own eval set, not just perplexity.

Which format do you deploy with?

#Quantization #LLM #Inference #AIEngineering
```

## Alt text

Cheat sheet titled 'Same Model. Different Precision. Different Footprint.' comparing six LLM quantization formats: INT8 (LLM.int8), GPTQ, AWQ, GGUF, NF4 and FP8. Each has a worked-example diagram, pros and cons, and relative latency and memory, followed by a table of which format to use when.
