import streamlit as st
from app import initialize_system
from safety.guardrails import Guardrails

st.title("🩺 Asthma Scenario Advisor")

st.write(
"""
Describe a breathing-related situation or asthma symptoms.
The AI will analyze it.
"""
)

# Load AI system once
@st.cache_resource
def load_rag():
    return initialize_system()

rag = load_rag()
guard = Guardrails()

scenario = st.text_area(
    "Describe the situation",
    placeholder="Example: My child coughs and wheezes at night when the weather is cold."
)

if st.button("Analyze Situation"):

    # Edge Case 1: Empty input
    if scenario.strip() == "":
        st.warning("Please describe the situation.")
        st.stop()

    with st.spinner("Analyzing..."):

        # Guardrails check
        safe, response = guard.filter_query(scenario)

        if not safe:
            st.error(response)
            st.stop()

        # ----------------------------
        # Scenario Advisor Prompt
        # ----------------------------

        scenario_prompt = f"""

You are MediBot, an AI assistant specialized in asthma and respiratory health.

You must analyze the user's situation using ONLY the retrieved medical context.

You are NOT allowed to diagnose diseases.
You must only explain possible interpretations of the symptoms.

--------------------------------
USER SITUATION
--------------------------------
{scenario}

--------------------------------
ANALYSIS INSTRUCTIONS
--------------------------------

Step 1: Identify symptoms mentioned by the user.

Step 2: Identify important context clues such as:
• worsening symptoms
• medication use
• triggers
• frequency or timing of symptoms

Step 3: Explain what might be happening in the airways based on the medical context.

Step 4: Provide helpful guidance based on the situation.

Step 5: Always remind the user that this is not a diagnosis.

--------------------------------
OUTPUT FORMAT
--------------------------------

Situation Understanding
Explain what the user described in simple words.

Possible Explanation
Explain what may be happening in the lungs or airways.

Important Symptoms
List symptoms detected in the description.

Important Concern
Mention if symptoms appear to be worsening or concerning.

Suggested Actions
Provide general safe advice based on medical context.

Medical Advice
Remind the user to consult a healthcare professional.

--------------------------------
IMPORTANT RULES
--------------------------------

• Do NOT invent triggers that are not mentioned.
• Do NOT diagnose asthma.
• Do NOT hallucinate.
• Use cautious language like:
  "may indicate"
  "could be related to"
  "may suggest"

• Use simple language suitable for patients.
"""

        result = rag.run(scenario_prompt)

        st.success("Analysis")

        st.write(result)