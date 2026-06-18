import os
import pandas as pd
import streamlit as st

# Page settings with a traditional vibe
st.set_page_config(page_title="Mithila Art Tracker", page_icon="🦚")

# Party  balloons!
st.balloons()

# Main Title and Subtitle
st.title("🦚 Welcome to My Mithila Art Gallery 🌺")
st.subheader("Ghar ki traditional kala, ab sidha Internet par!")

# Description
st.write("Yeh app bohot special hai kyunki isme hamari apni Mithila (Madhubani) painting ka touch hai. 🎨✨")
st.write("Ab hum yahan apne saare art projects aur sketches track karenge.")

if st.button("App Check Karo (Click Me)"):
    st.success("PERFECT!!!")

def calculate_business_stats():
    print("=============================================")
    print("🎨 MITHILA ART BUSINESS TRACKER & ANALYTICS 🎨")
    print("=============================================\n")

    item_name = input("Enter Item/Motif Name (e.g., Fish Keyring, Surya): ")
    raw_material_cost = float(input("Enter Raw Material Cost (in ₹): "))
    selling_price = float(input("Enter Selling Price (in ₹): "))
    quantity = int(input("Enter Quantity Sold: "))

    total_cost = raw_material_cost * quantity
    total_revenue = selling_price * quantity
    net_profit = total_revenue - total_cost

    profit_percentage = (net_profit / total_cost) * 100

    print("\n" + "-" * 40)
    print("📊 REAL-TIME ORDER ANALYTICS:")
    print(f"💰 Total Investment: ₹{total_cost:.2f}")
    print(f"📈 Total Revenue: ₹{total_revenue:.2f}")
    print(f"🎉 Net Profit: ₹{net_profit:.2f}")
    print(f"🚀 Profit Margin: {profit_percentage:.2f}%")
    print("-" * 40 + "\n")

    new_data = {
        "Item Name": [item_name],
        "Material Cost (₹)": [raw_material_cost],
        "Selling Price (₹)": [selling_price],
        "Quantity": [quantity],
        "Total Cost (₹)": [total_cost],
        "Total Revenue (₹)": [total_revenue],
        "Net Profit (₹)": [net_profit],
        "Profit Margin (%)": [round(profit_percentage, 2)],
    }

    df_new = pd.DataFrame(new_data)
    file_name = "mithila_art_sales.csv"

    if os.path.exists(file_name):
        df_existing = pd.read_csv(file_name)
        df_final = pd.concat([df_existing, df_new], ignore_index=True)
    else:
        df_final = df_new

    df_final.to_csv(file_name, index=False)
    print(f"✅ Data successfully saved in '{file_name}'!")

    print("\n📦 CURRENT INVENTORY SUMMARY:")
    print(f"Total Items Sold till date: {df_final['Quantity'].sum()}")
    print(f"Total Lifetime Profit: ₹{df_final['Net Profit (₹)'].sum():.2f}")

calculate_business_stats()

