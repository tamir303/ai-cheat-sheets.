# Sigmoid: Squash Any Number to (0, 1)

**Topic:** Sigmoid activation  
**Format:** deep dive · Activation functions 1/6  
**LinkedIn:** Wed Oct 7 2026, 12:00 (Israel time)

![Cheat sheet titled 'Sigmoid: Squash Any Number to (0, 1)' explaining the sigmoid activation: the idea, the formula, a worked example, two diagrams (the S-curve and why gradients vanish), where it is used, and its strengths and limits. Part 1 of 6 in the Activation functions series.](16-sigmoid.png)

## LinkedIn post

```text
Sigmoid in one page: any number in, a probability out.

It's the classic output for yes/no predictions and the gate inside LSTMs, and its shape explains why hidden layers moved on to other activations.

What's on the sheet:
→ The formula: σ(x) = 1 / (1 + e^−x), with slope σ(x)(1 − σ(x))
→ A worked example: σ(2) ≈ 0.88, with slope 0.105
→ Why gradients vanish: the slope is at most 0.25
→ Where it's used: classifier heads, multi-label outputs, LSTM gates, SiLU

Rule of thumb: use it at the output, not in hidden layers, and give your loss logits, not probabilities.

Where do you still reach for sigmoid?

Part 1 of 6 in my Activation functions series. Next up: Tanh.

#DeepLearning #NeuralNetworks #MathForML #MachineLearning
```

## Alt text

Cheat sheet titled 'Sigmoid: Squash Any Number to (0, 1)' explaining the sigmoid activation: the idea, the formula, a worked example, two diagrams (the S-curve and why gradients vanish), where it is used, and its strengths and limits. Part 1 of 6 in the Activation functions series.
