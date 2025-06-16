import streamlit as st
from solver.algebra import solve_equation
from solver.geometry import solve_geometry
from solver.trigonometry import solve_trigonometry
from solver.image_solver import extract_text_from_image

st.set_page_config(page_title="AI Math Calculator by Mubashar", layout="centered")

st.markdown(
    """
    <h1 style='text-align: center; color: #2E86C1;'>🧮 AI Math Calculator by Mubashar</h1>
    <h4 style='text-align: center; color: #555;'>Solve Algebra, Geometry, Trigonometry & MCQs — Text & Image Based</h4>
    <hr style='border: 1px solid #2E86C1;'/>
    """,
    unsafe_allow_html=True
)

# User Input Method
method = st.radio("Select Input Method:", ["📝 Type Question", "🖼️ Upload Image"])

if method == "📝 Type Question":
    question = st.text_area("Enter your math question:", height=150)

    if st.button("🔍 Solve"):
        if "sin" in question or "cos" in question or "tan" in question:
            result = solve_trigonometry(question)
        elif any(shape in question.lower() for shape in ["area", "perimeter", "circle", "rectangle", "triangle"]):
            result = solve_geometry(question)
        else:
            result = solve_equation(question)

        st.markdown("### 🧠 Answer:")
        st.success(result)

elif method == "🖼️ Upload Image":
    uploaded_file = st.file_uploader("Upload Image Containing Math Question", type=["jpg", "png", "jpeg"])

    if uploaded_file is not None:
        st.image(uploaded_file, caption="Uploaded Question", use_column_width=True)
        question = extract_text_from_image(uploaded_file)

        st.markdown("### 📝 Extracted Question:")
        st.info(question)

        if st.button("🔍 Solve"):
            if "sin" in question or "cos" in question or "tan" in question:
                result = solve_trigonometry(question)
            elif any(shape in question.lower() for shape in ["area", "perimeter", "circle", "rectangle", "triangle"]):
                result = solve_geometry(question)
            else:
                result = solve_equation(question)

            st.markdown("### 🧠 Answer:")
            st.success(result)

st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Made with ❤️ by Mubashar Ul Hassan</p>",
    unsafe_allow_html=True
)
