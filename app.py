import streamlit as st

st.title("🦠 AI Microbiology Visual Identifier")

st.write("Select a bacteria to learn about it")

bacteria = st.selectbox(
    "Choose bacteria:",
    [
        "Escherichia coli",
        "Staphylococcus aureus",
        "Bacillus subtilis",
        "Streptococcus pneumoniae"
    ]
)

if bacteria == "Escherichia coli":
    st.subheader("Escherichia coli")
    st.write("**Gram Type:** Gram-negative")
    st.write("**Shape:** Rod (Bacillus)")
    st.write("**Habitat:** Human intestine")
    st.write("**Medical Importance:** Some strains cause diarrhea and urinary tract infections")

    st.success(
        "AI Interpretation: E. coli is a Gram-negative rod-shaped bacterium commonly found in the human gut. While many strains are harmless, certain pathogenic strains can cause gastrointestinal disease and urinary tract infections."
    )

elif bacteria == "Staphylococcus aureus":
    st.subheader("Staphylococcus aureus")
    st.write("**Gram Type:** Gram-positive")
    st.write("**Shape:** Cocci in clusters")
    st.write("**Habitat:** Skin and nasal cavity")
    st.write("**Medical Importance:** Causes skin infections and food poisoning")

    st.success(
        "AI Interpretation: Staphylococcus aureus is a Gram-positive bacterium that forms clusters resembling grapes. It commonly inhabits the skin and nasal passages but can cause skin infections and food poisoning."
    )

elif bacteria == "Bacillus subtilis":
    st.subheader("Bacillus subtilis")
    st.write("**Gram Type:** Gram-positive")
    st.write("**Shape:** Rod")
    st.write("**Habitat:** Soil")
    st.write("**Medical Importance:** Common model organism in research")

    st.success(
        "AI Interpretation: Bacillus subtilis is a Gram-positive, spore-forming bacterium commonly found in soil. It is widely used as a model organism in microbiology research."
    )

elif bacteria == "Streptococcus pneumoniae":
    st.subheader("Streptococcus pneumoniae")
    st.write("**Gram Type:** Gram-positive")
    st.write("**Shape:** Cocci in chains")
    st.write("**Habitat:** Respiratory tract")
    st.write("**Medical Importance:** Causes pneumonia and meningitis")

    st.success(
        "AI Interpretation: Streptococcus pneumoniae is a Gram-positive bacterium frequently found in the respiratory tract. It is an important pathogen associated with pneumonia, meningitis, and other respiratory infections."
    )