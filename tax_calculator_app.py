import streamlit as st

def calculate_tax(sal):
    taxableSal = sal - 75000
    if taxableSal <= 0:
        return "Enter a valid amount."
    else:
        tax = 0
        if 0 < taxableSal <= 300000:
            tax = 0
        elif 300000 < taxableSal <= 700000:
            tax = (taxableSal - 300000) * 0.05
        elif 700000 < taxableSal <= 1000000:
            tax = (400000) * 0.05 + (taxableSal - 700000) * 0.1
        elif 1000000 < taxableSal <= 1200000:
            tax = (400000) * 0.05 + (300000) * 0.1 + (taxableSal - 1000000) * 0.15
        elif 1200000 < taxableSal <= 1500000:
            tax = (400000) * 0.05 + (300000) * 0.1 + (200000) * 0.15 + (taxableSal - 1200000) * 0.2
        elif taxableSal > 1500000:
            tax = (400000) * 0.05 + (300000) * 0.1 + (200000) * 0.15 + (300000) * 0.2 + (taxableSal - 1500000) * 0.3
        
        cess = (4 / 100) * tax
        inTax = tax + cess
        return f"Income Tax to be paid: ₹{inTax:.2f}"

# Streamlit UI
st.title("Income Tax Calculator")
salary = st.number_input("Enter your annual salary (₹):", min_value=0, step=1000)

if st.button("Calculate Tax"):
    result = calculate_tax(salary)
    st.success(result)
