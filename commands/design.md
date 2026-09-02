---
description: Design one slice together, by question and answer.
---

We are designing slice $ARGUMENTS together. I am the designer. You ask, I decide.

Ask me ONE question at a time. Wait for my answer before the next. Never ask two
questions in one message. Never propose a full design.

Work through these in order, skipping any I have already answered:

1. What goes in? Exact fields.
2. What comes out? Exact fields.
3. What happens when the input is malformed or empty?
4. What happens when the system is uncertain?
5. What must never happen, no matter what?
6. What is explicitly out of scope for this slice?

Each question: one line. Offer at most two options if it helps me decide, marked as
suggestions I can reject.

When all six are answered, write DESIGN-slice$ARGUMENTS.md containing exactly my answers
under those six headings. Add nothing I did not say. Then print the file and stop.

Do not write tests. Do not write code.
