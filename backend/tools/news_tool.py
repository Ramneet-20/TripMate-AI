from ddgs import DDGS

def get_latest_news(destination):
    try:
        query = f"{destination} travel safety weather traffic latest news"

        results = []

        with DDGS() as ddgs:
            for item in ddgs.news(query, max_results=5):
                results.append({
                    "title": item.get("title", "No title"),
                    "source": item.get("source", "Unknown source"),
                    "url": item.get("url", ""),
                    "date": item.get("date", "")
                })

        return results

    except Exception:
        return []