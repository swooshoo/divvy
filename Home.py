import streamlit as st
import os

st.set_page_config(
    page_title="Divvy",
    page_icon="icon.png",
)

def main():
    st.image("headerimg.png")
    with st.container(border=True):
        st.header("Start Here")
        num_people = st.number_input("Divvied how many ways?", min_value=2, value=2, step=1,) #INPUT: NUM OF PEOPLE
        #st.write("Bill will be split by:", num_people)
        num_subtotal = st.number_input("Subtotal:", min_value=0.01, value=0.02, step = 0.01, format="%0.2f")  #INPUT: RECEIPT SUBTOTAL
        #st.write("Subtotal: $", f"{num_subtotal:.2f}")
        num_tax = st.number_input("How much is tax?", min_value = 0.00, max_value=num_subtotal, value=0.00, step = 0.01, format="%0.2f")  #INPUT: SALES TAX
        #st.write("Tax: $", f"{num_tax:.2f}")
        percent_tax = (num_tax/num_subtotal) * 100
        #st.write(f"Your tax is {percent:.2f}%.")  #OUTPUT: CLARIFYING IF THE STATE TAX PERCENT LINES UP FOR THE USER
        num_tip =  st.number_input("How much is tip?", min_value = 0.00, value=0.00, step = 0.01, format="%0.2f") #INPUT: RECEIPT TIP
        st.write("Tip: $", f"{num_tip:.2f}")
    with st.container(border=True):
        st.subheader("Receipt Summary:")
        st.write("Subtotal -  $", f"{num_subtotal:.2f}")
        st.write(f"Tax -  $", f"{num_tax:.2f}", " at a ", f"{percent_tax:.2f}%")
        st.write("Tip -  $", f"{num_tip:.2f}")
        num_total = num_subtotal + num_tax + num_tip
        st.write("Total -  $", f"{num_total:.2f}")
    with st.container(border=True):
        st.subheader("Enter each person's item total:")
        item_totals = []
        for i in range(num_people):
            item_total = st.number_input(f"Person {i+1} Item Total:", min_value=0.00, value=0.00, step=0.01, format="%0.2f")
            item_totals.append(item_total)
        
        num_total = num_subtotal + num_tax + num_tip
        st.subheader("Double Check")
        st.write(f"Subtotal: ${num_subtotal:.2f}")
        st.write(f"Tax: ${num_tax:.2f}")
        st.write(f"Tip: ${num_tip:.2f}")
        st.write(f"Total: ${num_total:.2f}")

        # Calculating each person's share
        st.subheader("Each Person's Share:")
        for i, item_total in enumerate(item_totals):
            person_share = (item_total / num_subtotal) * num_total
            st.write(f"Person {i+1} owes: ${person_share:.2f}")


if __name__ == "__main__":
    main()