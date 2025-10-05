# 🧠 JSONCrawler – Automated Data Extractor for Agents

The **JSONCrawler** is a lightweight Python utility designed to **automatically extract and format structured data (like JSON responses from APIs)** into **clean, human-readable strings** — ready to be used as **context for LLM prompts, agent system messages, or downstream processing**.

This is especially useful when integrating external APIs (e.g., weather, news, finance) into intelligent systems, where the raw JSON needs to be **summarized into a natural-language context** without manual parsing.

---

## 🚀 Features

* ✅ **Automatic traversal** of nested JSON objects and lists
* ✅ Extracts **keys and values recursively**
* ✅ Customizable output (limit items, choose keys, etc.)
* ✅ Returns **plain text strings**, perfect for LLM prompts or system messages
* ✅ Easily embeddable into agents, IoT projects.

---

## 📦 Installation

Just drop the `JsonCrawler` class into your project — no external dependencies required.
or simply copy the class into your project file.

---

## 🧰 Usage Example

```python

crawler = JsonCrawler()

# Sample JSON from a weather API
data = {
    "location": "Ludhiana",
    "temperature": "31°C",
    "condition": "Cloudy",
    "forecast": [
        {"day": "Monday", "high": "33°C", "low": "25°C"},
        {"day": "Tuesday", "high": "32°C", "low": "24°C"}
    ]
}

result = crawler.process(data)
print(result)
```

This result can be directly appended to a system prompt for an LLM or used as context by an intelligent agent.

---

## ⚙️ API Reference

### `crawl_object(obj: dict, **kwargs) -> str`

Crawls a JSON/dict object and returns a flattened string.

| Parameter | Type                   | Description                     |
| --------- | ---------------------- | ------------------------------- |
| `obj`     | `dict`                 | JSON or dictionary to parse     |
| `extract` | `list[str]` (optional) | Keys to extract specifically    |
| `n_items` | `int` (optional)       | Limit number of items processed |

---

### `crawl_list(lst: list, **kwargs) -> str`

Iterates through a list of objects and concatenates their crawled strings.

| Parameter | Type             | Description                              |
| --------- | ---------------- | ---------------------------------------- |
| `lst`     | `list`           | List of JSON objects                     |
| `n_items` | `int` (optional) | Limit number of list elements to process |

---

## 🧠 Real-World Use Cases

* 🤖 **Agent Systems** – Convert structured API responses into natural language context.
* 🌦️ **Weather/News Assistants** – Fetch live data and pass it directly into prompts.
* 🛰️ **Wearable Devices (e.g., Arc Reactor)** – Automate sensor data parsing without custom logic.
* 📊 **Dashboards or Reports** – Generate readable summaries from complex JSON payloads.

---

## 🧪 Future Improvements

* 🔁 Stream parsing for very large JSON payloads
* ⚡ Async support for API-heavy workflows
* 🧹 Intelligent key filtering and summarization
* 🧠 Integration with vector databases for semantic retrieval

---

## 📜 License

MIT License © 2025 – Built for intelligent agents and real-time assistants.
