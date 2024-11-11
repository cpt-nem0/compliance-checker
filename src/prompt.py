COMPLIANCE_PROMPT = """\
    Act as a compliance checker. Analyze the following webpage content against the given compliance policy.
    Return your analysis in JSON format with two keys: 'violations' (a list of objects) and 'summary' (a string).

    For each violation, include:
        - "text": the specific text that violates the policy
        - "rule": the policy rule that was violated
        - "explanation": brief explanation of why it's a violation

    Compliance Policy:
        {policy_text}

        Webpage Content:
        {webpage_text}

        Provide your response in valid JSON format like this:
        {{
            "violations": [
                {{
                    "text": "found text",
                    "rule": "violated rule",
                    "explanation": "why this is a violation"
                }}
            ],
            "summary": "overall compliance summary"
        }}
    """
