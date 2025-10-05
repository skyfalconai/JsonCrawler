import requests

class JsonCrawler:
    # Recursively crawl through a dictionary and return a string representation
    def crawl_dict(self, obj, **kwargs):
        try:
            required_keys = kwargs.get("require", None)
            string_to_return = ""
            
            for key, value in obj.items():
                if required_keys:
                    if key.lower() in required_keys:
                        string_to_return += f"{key}: {self.crawl(value, **kwargs)}\n"
                else:
                    string_to_return += f"{key}: {self.crawl(value, **kwargs)}\n"
            return string_to_return
        except Exception:
            return ""

    def crawl_list(self, lst, **kwargs):
        try:
            max_levels = kwargs.get('n_levels', len(lst))
            string_to_return = ""
            
            for item in lst[:max_levels]:
                string_to_return += self.crawl(item, **kwargs) + "\n"
            return string_to_return
        except Exception:
            return ""

    def crawl(self, obj, **kwargs):
        try:
            if isinstance(obj, list):
                return self.crawl_list(lst=obj, **kwargs)
            elif isinstance(obj, dict):
                return self.crawl_dict(obj=obj, **kwargs)
            else:
                return str(obj)
        except Exception:
            return ""

    def process(self, obj, **kwargs):
        try:
            if "require" in kwargs:
                kwargs["require"] = list(map(str.lower, kwargs["require"]))
            return self.crawl(obj, **kwargs)
        except Exception:
            return ""


# Example usage:
# crawler = JsonCrawler()
# try:
#     response = requests.get('https://dummyjson.com/products')
#     result = crawler.process(
#         response.json(),
#         n_levels=10,  # Limit number of items processed from lists
#         require=["products", "title", "id", "category"]  # Only include these keys
#     )
#     print(result)
# except Exception:
#     # If request fails or JSON is invalid, fallback to empty string
#     print("")
