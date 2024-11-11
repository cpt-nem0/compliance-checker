from src.llm import LLMClient
from src.prompt import COMPLIANCE_PROMPT
from src.utils import extract_json


def analyse_compliance(
    webpage_text: str, policy_text: str, llm_client: LLMClient
) -> dict:

    prompt = COMPLIANCE_PROMPT.format(
        webpage_text=webpage_text, policy_text=policy_text
    )
    llm_response = llm_client.generate_answer(prompt)
    json_result = extract_json(llm_response)

    if (
        not isinstance(json_result, dict)
        or "violations" not in json_result
        or "summary" not in json_result
    ):
        raise ValueError("Invalid response structure")

    return json_result
