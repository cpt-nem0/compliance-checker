from fastapi import FastAPI
from pydantic import BaseModel

from src.llm import OllamaCLient
from src.service import analyse_compliance
from src.web_extractor import WebPageExtractor

app = FastAPI()


class ComplianceResult(BaseModel):
    violations: list[dict[str, str]]
    summary: str


class WebpageRequest(BaseModel):
    webpage_url: str
    policy_url: str


@app.post("/check-compliance", response_model=ComplianceResult)
async def check_compliance(request: WebpageRequest):

    ollama_client = OllamaCLient()
    info_extractor = WebPageExtractor()

    webpage_text = info_extractor.extract_text_from_webpage(request.webpage_url)
    policy_text = info_extractor.extract_text_from_webpage(request.policy_url)

    analysis = analyse_compliance(webpage_text, policy_text, ollama_client)

    return analysis
