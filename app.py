import streamlit as st
from solver.algebra import solve_equation
from solver.geometry import solve_geometry
from solver.trigonometry import solve_trigonometry
from solver.image_solver import extract_text_from_image
from PIL import Image

st.set_page_config(page_title="Mubashar AI Math Calculator", layout="centered")

st.title("📚 Mubashar's AI Math Calculator 🤖")
st.markdown("""
Welcome to the **AI Math Calculator by Mubashar Ul Hassan**.
This app can solve:
- Algebra equations
- Geometry problems
- Trigonometry questions
- Image-based math queries
""")

# Tabs for each type
tab1, tab2, tab3, tab4 = st.tabs(["🔢 Algebra", "📐 Geometry", "📈 Trigonometry", "🖼️ Image Solver"])

with tab1:
    st.subheader("🧮 Algebra Solver")
    question = st.text_input("Enter your algebraic equation (e.g., 2x + 3 = 7)")
    if st.button("Solve Algebra"):
        try:
            result = solve_equation(question)
            st.success(f"✅ Answer: {result}")
        except Exception as e:
            st.error("❌ Error: Couldn't solve the algebraic equation.")

with tab2:
    st.subheader("📏 Geometry Solver")
    geo_question = st.text_input("Enter a geometry problem (e.g., area of circle with radius 5)")
    if st.button("Solve Geometry"):
        result = solve_geometry(geo_question)
        st.success(f"✅ Answer: {result}")

with tab3:
    st.subheader("📐 Trigonometry Solver")
    trig_question = st.text_input("Enter a trigonometry expression (e.g., sin(30))")
    if st.button("Solve Trigonometry"):
        result = solve_trigonometry(trig_question)
        st.success(f"✅ Answer: {result}")

with tab4:
    st.subheader("🖼️ Upload Image of Math Problem")
    uploaded_image = st.file_uploader("Upload PNG/JPG image", type=["png", "jpg", "jpeg"])
    if uploaded_image:
        st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)

        if st.button("🧠 Extract & Solve"):
            extracted = extract_text_from_image(uploaded_image)
            st.info(f"📝 Extracted: {extracted}")

            try:
                result = solve_equation(extracted)
                st.success(f"✅ Answer: {result}")
            except:
                st.warning("⚠️ Could not solve extracted text.")
