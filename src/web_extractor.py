import requests
from bs4 import BeautifulSoup
from fastapi import HTTPException


class WebPageExtractor:
    def __init__(self) -> None:
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",
        }

    def extract_text_from_webpage(self, url: str) -> str:
        try:
            response = requests.get(url, headers=self.headers, timeout=10)
            response.raise_for_status()

            soup = BeautifulSoup(response.text, "html.parser")

            for element in soup(["script", "style", "footer", "nav", "header"]):
                element.decompose()

            main_body = soup.find("main") or soup.find("body")
            if not main_body:
                return ""

            text = main_body.get_text(separator="\n", strip=True)
            return text

        except requests.exceptions.HTTPError as e:
            raise HTTPException(
                status_code=400, detail=f"Error fetching webpage: {str(e)}"
            )
