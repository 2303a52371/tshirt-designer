import streamlit as st
import copy

# Prototype base
class Prototype:
    def clone(self):
        return copy.deepcopy(self)

# Tshirt class
class Tshirt(Prototype):
    def __init__(self, size, color, print_design):
        self.size = size
        self.color = color
        self.print_design = print_design

    def __str__(self):
        return f"Tshirt(Size={self.size}, Color={self.color}, Print={self.print_design})"

# -----------------------
# Streamlit UI
# -----------------------

st.title("👕 Custom T-shirt Designer (Prototype Pattern)")

st.sidebar.header("🎨 Create Original T-shirt")
size = st.sidebar.selectbox("Choose Size", ["S", "M", "L", "XL"])
color = st.sidebar.color_picker("Pick Color", "#000000")
design = st.sidebar.text_input("Print Design", "No Print")

# Create original
original_tshirt = Tshirt(size, color, design)

st.subheader("🟢 Original T-shirt")
st.write(original_tshirt.__str__())

# Clone Section
st.sidebar.header("🌀 Clone Settings")
clone_option = st.sidebar.radio("Modify while cloning", ["Size", "Color", "Print Design"])

if clone_option == "Size":
    new_size = st.sidebar.selectbox("New Size", ["S", "M", "L", "XL"])
    cloned_tshirt = original_tshirt.clone()
    cloned_tshirt.size = new_size

elif clone_option == "Color":
    new_color = st.sidebar.color_picker("New Color", "#FF0000")
    cloned_tshirt = original_tshirt.clone()
    cloned_tshirt.color = new_color

elif clone_option == "Print Design":
    new_design = st.sidebar.text_input("New Print", "Dragon Logo")
    cloned_tshirt = original_tshirt.clone()
    cloned_tshirt.print_design = new_design

# Display cloned T-shirt
st.subheader("🔵 Cloned T-shirt")
st.write(cloned_tshirt.__str__())

# Note
st.info("✅ The cloned T-shirt starts with original properties but is independent after modification.")
