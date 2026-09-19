# BCGX GenAI Simulation - Task 2: AI Financial Chatbot Prototype

## Overview
This prototype is a rule-based AI financial chatbot developed for Global Finance Corp (GFC). It converts static 10-K financial metrics (2023–2025) for Microsoft, Apple, and Tesla into an interactive command-line query engine.

## Predefined Queries Handled
1. **Total Revenue:** "What is the total revenue for Microsoft / Apple / Tesla?"
2. **Net Income / Profit:** "What is the net income for Microsoft / Apple / Tesla?"
3. **Year-over-Year Growth:** "Show me YoY revenue growth rates"
4. **Profit Margins:** "What are the net profit margins?"
5. **Debt Ratios:** "Show debt to asset ratios"

## Architecture & Logic
- **Data Integration:** Loads structured metrics from `processed_financial_data.csv`.
- **Natural Language Parsing:** Normalizes user inputs to lowercase and uses keyword extraction to route queries.
- **Error Handling:** Features a fallback mechanism for unrecognized or out-of-scope queries.

## Limitations
- Operates on deterministic, hardcoded keyword-matching rules (requires exact company name and metric keyword).
- Currently lacks deep LLM-synthesized context or full conversational memory across multiple turns.
