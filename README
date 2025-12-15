# Policy-Aware Prompt Compression Gateway

A minimal control-plane service that enforces
policy constraints on LLM prompts before execution.

Built on top of LLMLingua.

## Motivation

As LLM systems scale, prompts become:
- longer
- more expensive
- harder to control

This project demonstrates how prompt execution
can be constrained before reaching a model.

## Features

- Prompt compression via LLMLingua
- Token-based policy enforcement
- Clear trust boundaries

## Non-Goals

- Model execution
- Prompt sanitization
- Agent orchestration

## Running

```bash
pip install -r requirements.txt
uvicorn gateway.main:app --reload
