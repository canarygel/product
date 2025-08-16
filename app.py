import streamlit as st
import pandas as pd
import os

# Safer path
data_path = os.path.join("data", "products.csv")

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
else:
    st.error(f"❌ Could not find dataset at: {data_path}")
    st.stop()

st.title("🛠️ Canary Products Workflow Tracker")

# Select a product
product = st.selectbox("Select a product", df["Product Name"].unique())

# Show product details
st.subheader("📋 Product Details")
st.write(df[df["Product Name"] == product])

# Example workflow stages & tasks
workflow = {
    "Design": ["Finalize design", "Review specifications", "Get approvals"],
    "Manufacturing": ["Source materials", "Set up production line", "Run initial batch"],
    "Testing": ["QA testing", "Safety compliance", "User feedback"],
    "Launch": ["Marketing prep", "Distribute units", "Post-launch support"]
}

st.subheader("✅ Workflow Checklist")

# Checklist with session_state
for stage, tasks in workflow.items():
    st.markdown(f"### {stage}")
    for task in tasks:
        key = f"{product}_{stage}_{task}"
        st.checkbox(task, key=key)
import os
import streamlit as st
import pandas as pd

st.write("📂 Current working directory:", os.getcwd())
st.write("📂 Files here:", os.listdir())
if os.path.exists("data"):
    st.write("📂 Files in /data:", os.listdir("data"))
else:
    st.write("❌ No /data folder found!")

data_path = os.path.join("data", "products.csv")

if os.path.exists(data_path):
    df = pd.read_csv(data_path)
    st.success("✅ Dataset loaded successfully!")
else:
    st.error(f"❌ Could not find dataset at: {data_path}")
    st.stop()
