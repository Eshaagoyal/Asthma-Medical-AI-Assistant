import re


class Guardrails:

    def __init__(self):

        # Prompt injection patterns
        self.jailbreak_patterns = [
            r"ignore previous instructions",
            r"disregard previous instructions",
            r"forget your instructions",
            r"reveal your system prompt",
            r"show your prompt",
            r"developer mode",
            r"bypass safety",
            r"jailbreak",
            r"pretend to be",
            r"act as",
            r"override rules",
            r"disable safety",
            r"system prompt",
            r"confidential instructions",
        ]

        # Medical safety phrases
        self.medical_warning_patterns = [
            r"prescribe medication",
            r"diagnose me",
            r"give me medical prescription",
            r"tell exact dosage",
            r"should i stop medication",
        ]

    # Detect prompt injection
    def detect_jailbreak(self, query):

        q = query.lower()

        for pattern in self.jailbreak_patterns:
            if re.search(pattern, q):
                return True

        return False


    # Detect unsafe medical advice requests
    def detect_medical_risk(self, query):

        q = query.lower()

        for pattern in self.medical_warning_patterns:
            if re.search(pattern, q):
                return True

        return False


    # Check if query is related to asthma
    def is_asthma_related(self, query):

        asthma_keywords = [
            "asthma",
            "lungs",
            "breathing",
            "wheezing",
            "inhaler",
            "airway",
            "bronchial",
            "respiratory",
            "allergy",
            "attack",
            "cough",
        ]

        q = query.lower()

        for word in asthma_keywords:
            if word in q:
                return True

        return False


    # Main safety filter
    def filter_query(self, query):

        # Jailbreak detection
        if self.detect_jailbreak(query):
            return False, (
                "⚠️ Security Alert: This query appears to attempt bypassing "
                "the system's safety rules. I can only answer questions "
                "related to asthma and respiratory health."
            )

        # Unsafe medical advice
        if self.detect_medical_risk(query):
            return False, (
                "⚠️ I cannot provide personalized medical prescriptions. "
                "Please consult a qualified healthcare professional."
            )

        return True, query