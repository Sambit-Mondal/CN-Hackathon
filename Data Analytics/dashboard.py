# dashboard.py
import streamlit as st
import plotly.express as px

import inventory

def main():
    st.title("Smart Inventory Management Dashboard")
    
    # Sidebar for threshold settings and email for notifications (moved to top)
    st.sidebar.header("Settings")
    low_stock_threshold = st.sidebar.number_input("Low Stock Threshold", value=50)
    excess_stock_threshold = st.sidebar.number_input("Excess Stock Threshold", value=500) 
    user_email = st.sidebar.text_input("Your Email for Notifications")
    
    # Load inventory data from MongoDB Atlas
    df = inventory.load_inventory_data()
    
    st.subheader("Current Inventory")
    if not df.empty:
        st.dataframe(df)
    else:
        st.info("No inventory data found.")
    
    # Visualize inventory using a bar chart with dynamic marker lines
    if not df.empty:
        fig = px.bar(df, x='title', y='quantity', title="Item Quantities")
        # Marker line for low stock threshold
        fig.add_shape(
            type="line",
            xref="paper", yref="y",
            x0=0, x1=1,
            y0=low_stock_threshold, y1=low_stock_threshold,
            line=dict(color="red", width=2, dash="dash")
        )
        # Marker line for excess stock threshold
        fig.add_shape(
            type="line",
            xref="paper", yref="y",
            x0=0, x1=1,
            y0=excess_stock_threshold, y1=excess_stock_threshold,
            line=dict(color="blue", width=2, dash="dash")
        )
        st.plotly_chart(fig)
        st.markdown("**Marker Lines:**\n- Red line = Low Stock Threshold\n- Blue line = Excess Stock Threshold")
        
        # Add line graph visualization
        fig_line = px.line(df, x='title', y='quantity', title="Item Quantities - Line Graph")
        st.plotly_chart(fig_line)
        
        # Add pie chart visualization
        fig_pie = px.pie(df, names='title', values='quantity', title="Inventory Distribution")
        st.plotly_chart(fig_pie)
    
    # Display low and excess stock items using sidebar thresholds
    if not df.empty:
        low_stock_items = df[df['quantity'] < low_stock_threshold]
        excess_stock_items = df[df['quantity'] > excess_stock_threshold]
        
        st.subheader("Low Stock Items")
        if not low_stock_items.empty:
            st.dataframe(low_stock_items)
        else:
            st.info("No items below threshold.")
        
        st.subheader("Excess Stock Items")
        if not excess_stock_items.empty:
            st.dataframe(excess_stock_items)
        else:
            st.info("No items above threshold.")
            

    
if __name__ == "__main__":
    main()
