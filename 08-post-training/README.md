# Same Raw Model. Different Feedback. Different Behavior.

**Topic:** LLM post-training and alignment methods  
**LinkedIn:** Thu Oct 22 2026, 09:00 (Israel time)

![Cheat sheet titled 'Same Raw Model. Different Feedback. Different Behavior.' comparing six LLM post-training methods: SFT, RLHF with PPO, DPO, ORPO, KTO and GRPO. Each has a worked-example diagram with the loss or advantage computed, pros and cons, and relative cost, followed by a table of which method to use when.](08-post-training.png)

## LinkedIn post

```text
Same raw model, six ways to teach it how to behave.

Pretraining gives a model knowledge, not manners. Post-training decides which feedback shapes its behavior.

The short version:
→ Teach format and tone from examples: SFT
→ Chosen vs rejected pairs: DPO
→ One stage, no reference model: ORPO
→ Only thumbs up/down: KTO
→ Math or code with checkable answers: GRPO
→ Maximum control, big budget: RLHF with PPO

Rule of thumb: start with clean SFT data, try DPO before full RLHF, and keep a KL leash so the model can't game the reward.

Which one is in your pipeline?

#LLM #MachineLearning #GenAI #AIEngineering
```

## Alt text

Cheat sheet titled 'Same Raw Model. Different Feedback. Different Behavior.' comparing six LLM post-training methods: SFT, RLHF with PPO, DPO, ORPO, KTO and GRPO. Each has a worked-example diagram with the loss or advantage computed, pros and cons, and relative cost, followed by a table of which method to use when.
