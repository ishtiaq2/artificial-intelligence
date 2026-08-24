# Module 5: Creating

## Teacher Script
Around 2020, models like GPT-3 crossed a threshold: instead of predicting a single number or label
(Module 2) using a network (Module 3), they could **generate brand-new content** — paragraphs, poems,
code — by predicting *the next word*, over and over, extremely well. This is a **Large Language
Model (LLM)**, and the underlying mechanism is neural networks from Module 3, just vastly bigger.

## Kid-Friendly Analogy
"Imagine the world's best 'autocomplete' on your phone keyboard — but instead of suggesting one word,
it's read an enormous amount of text, and can write whole essays, one word at a time, each word
chosen because it's the most likely next word given everything before it."

## Key Vocabulary
- **LLM (Large Language Model)** — a neural network trained on huge amounts of text to predict/generate language
- **Token** — a chunk of text (roughly a word or part of a word) the model reads/writes at a time
- **Prompt** — the instruction or question you give the model
- **Generative** — creating something new, rather than just classifying or predicting a number

## Unplugged Activity: Next-Word Guessing Game (15 min)
1. Write a sentence on the board with the last word missing: "The dog ran across the ___."
2. Students shout guesses. Notice everyone predicts something *plausible* (park, road, field) — not
   random words like "purple."
3. Explain: an LLM does exactly this, one word at a time, thousands of times per second, trained on
   billions of sentences instead of just classroom guesses.

## Hands-On Tutorial: `tutorial.py`
Build a tiny text generator using a simple statistical technique (a Markov chain) — no API key
needed, works completely offline, and demystifies "predict the next word" with real, runnable code.

## No-Code Extension: Prompt Engineering Lab (25 min)
Using any supervised, school-appropriate chat AI interface:
1. Try a vague prompt: `"Write about a dog."`
2. Try a detailed prompt: `"Write a 3-sentence story about a nervous puppy's first day at school, in a funny tone."`
3. Compare outputs — the quality of the prompt strongly shapes the quality of the output.

## Data & Bias Checkpoint
Ask: **"If this model only ever read text from one country, one language, or one point of view, what
might it never learn to write well?"** Generative models can only remix patterns they've seen in
their training text.

## Discussion Questions
- Why might an LLM sometimes state something false confidently ("hallucination")? (It's predicting
  *plausible* text, not looking up *true* facts.)
- What's the difference between a search engine and an LLM?
