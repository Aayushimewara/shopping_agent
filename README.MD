# 🛒 Shopping Agent

An agentic AI shopping assistant that uses an LLM and tool calling
to search products, check ratings, and place orders using a SQLite database.

## Features

- Natural-language product search
- Filter products by price and organic status
- Retrieve product ratings and review counts
- Place orders through an agent-selected checkout tool
- Analyze product images and extract searchable attributes
- SQLite database for products, reviews, and orders

## Tech Stack

- Python
- LangChain
- Groq
- SQLite
- Streamlit
- Sentence/vision-capable LLMs

## How It Works

User Query
    ↓
LangChain Agent
    ↓
LLM decides which tool to use
    ↓
┌──────────────────────────────┐
│ search_products              │
│ get_rating                   │
│ describe_product_image       │
│ checkout                     │
└──────────────────────────────┘
    ↓
SQLite Database
    ↓
Response to User