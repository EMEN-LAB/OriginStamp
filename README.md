# 🛡️ OriginStamp

**OriginStamp is the open-source payment layer for the C2PA standard.**

## The Problem

The C2PA (Adobe, Google, Microsoft) is building the "nutrition label" to solve AI content *trust*. This is critical.

But it's missing the "price tag."

There is no open, universal standard for embedding *payment* and *licensing* information into a file. This is the critical missing piece that ensures creators get paid for their work in the new AI economy.

## The Solution

`OriginStamp` is a simple, lightweight, open-source tool that reads and writes a new, custom C2PA "assertion" (a metadata block) called `com.originstamp.payment`.

This allows any creator, artist, or developer to embed their "price tag"—a wallet address, a Stripe link, a licensing URL—directly into the file itself. The proof of origin and the path to payment will travel together, wherever the file goes.

## The Journey (Build in Public)

I am the solo founder of OriginStamp, building this from $0 and 0 connections. I am building this entire project in public, with an AI as my co-founder, from a Samsung tablet.

This is Day 1. You can follow the progress, contribute, and watch this grow.

### Roadmap (Sprint 0 - The First 7 Days)

1.  [ ] **Day 1:** Project Init.
2.  [ ] **Day 2:** Setup cloud environment (Replit) & install `c2patool`.
3.  [ ] **Day 3:** Successfully *read* a C2PA manifest from a test image.
4.  [ ] **Day 4:** Define the `com.originstamp.payment` JSON assertion.
5.  [ ] **Day 5-6:** Successfully *write* and *embed* this new assertion into a file.
6.  [ ] **Day 7:** Publicly demo the "stamped" file.

---
