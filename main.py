import streamlit as st

from LLM_Calling import translate_clinical_notes


st.set_page_config(
    page_title="Clinical Notes Translator",
    page_icon="🩺",
    layout="wide",
)

st.title("🩺 Clinical Notes Translator")
st.caption(
    "Turn clinical notes into clear, patient-friendly language while "
    "preserving the information in the original note."
)

st.info(
    "This tool explains the wording of a clinical note. It does not provide "
    "a diagnosis, medical advice, or a substitute for a healthcare professional."
)

note = st.text_area(
    "Enter a clinical note",
    placeholder=(
        "Example: Patient presents with hypertension and reports "
        "mild dyspnea on exertion."
    ),
    height=220,
)

translate_clicked = st.button(
    "Translate note",
    type="primary",
    disabled=not note.strip(),
)

if translate_clicked:
    with st.spinner("Translating the clinical note..."):
        result = translate_clinical_notes(note.strip())

    if result.startswith("Error:"):
        st.error(result)
    elif result == "Irrelevant prompt":
        st.warning(result)
    else:
        st.subheader("Translation")
        original_col, translated_col = st.columns(2, gap="large")

        with original_col:
            st.markdown("**Original clinical note**")
            st.text_area(
                "Original note",
                value=note.strip(),
                height=260,
                disabled=True,
                label_visibility="collapsed",
            )

        with translated_col:
            st.markdown("**Patient-friendly explanation**")
            st.markdown(result)

        st.caption(
            "Please review the explanation against the original clinical note. "
            "AI-generated translations may contain errors."
        )
