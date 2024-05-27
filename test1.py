import streamlit as st

# Sample data
products = [
    {
        "name": "iPhone 15 Pro Max",
        "price": "35,990,000 VND",
        "image": "https://cdn.tgdd.vn/Products/Images/42/305658/iphone-15-pro-max-blue-thumbnew-600x600.jpg"
    },
    {
        "name": "Samsung Galaxy S23",
        "price": "29,990,000 VND",
        "image": "https://example.com/galaxys23.jpg"
    },
    {
        "name": "Xiaomi Mi 12",
        "price": "19,990,000 VND",
        "image": "https://example.com/mi12.jpg"
    }
]

st.title("The gioi di dong")

# Display products
for product in products:
    st.image(product["image"], width=200)
    st.subheader(product["name"])
    
    st.write(f"Price: {product['price']}")

