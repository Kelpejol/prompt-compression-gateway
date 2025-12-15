# Architecture

This service acts as a control plane for prompt execution.

## Flow

Client
  → Policy Gateway
      → Token / Cost Policies
      → Compression (LLMLingua)
  → Constrained Prompt Output

## Design Principles

- Policies execute before model interaction
- Compression reduces cost without truncation
- Clear rejection paths for unsafe prompts
