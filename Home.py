import streamlit as st

st.set_page_config(page_title="Divvy", page_icon="icon.png")

def get_user_inputs():
    #Collects user inputs for bill splitting.
    st.image("headerimg.png")
    with st.container(border=True):
        st.header("Start Here")
        num_people = st.number_input("Divvied how many ways?", min_value=2, max_value = 15, value=2, step=1)
        num_subtotal = st.number_input("Subtotal:", min_value=0.01, value=0.01, step=0.01, format="%0.2f")
        num_tax = st.number_input("How much is tax?", min_value=0.00, max_value=num_subtotal, value=0.00, step=0.01, format="%0.2f")
        num_tip = st.number_input("How much is tip?", min_value=0.00, value=0.00, step=0.01, format="%0.2f")
        return num_people, num_subtotal, num_tax, num_tip

def display_summary(num_subtotal, num_tax, num_tip):
    #Displays a summary of the bill.
    percent_tax = (num_tax / num_subtotal) * 100
    num_total = num_subtotal + num_tax + num_tip

    with st.container(border=True):
        st.subheader("Receipt Summary:")
        st.write(f"Subtotal: ${num_subtotal:.2f}")
        st.write(f"Tax: ${num_tax:.2f} ({percent_tax:.2f}%)")
        st.write(f"Tip: ${num_tip:.2f}")
        st.write(f"Total: ${num_total:.2f}")
    return num_total

def collect_item_totals(num_people, num_subtotal):
    #Collects individual item totals from the user.
    with st.container(border=True):
        st.subheader("Enter each person's item total:")
        item_totals = [st.number_input(f"Person {i+1} Item Total:", min_value=0.00, value=0.00, step=0.01, format="%0.2f") for i in range(num_people)]
        # Validation check for subtotal match
        if sum(item_totals) == num_subtotal:
            st.success("All totals match the subtotal! ✅")
        elif sum(item_totals) > num_subtotal:
            st.error("The totals exceed the subtotal. Please review the inputs.")
        elif sum(item_totals) < num_subtotal:
            st.warning("The totals are less than the subtotal. Please review the inputs.")

        return item_totals

def calculate_shares(item_totals, num_subtotal, num_total):
    #Calculates and displays each person's share of the bill.
    with st.container(border=True):
        st.subheader("Each Person's Share:")
        for i, item_total in enumerate(item_totals):
            person_share = (item_total / num_subtotal) * num_total
            st.write(f"Person {i+1} owes: ${person_share:.2f}")
        

def main():
    num_people, num_subtotal, num_tax, num_tip = get_user_inputs()
    num_total = display_summary(num_subtotal, num_tax, num_tip)
    item_totals = collect_item_totals(num_people, num_subtotal)
    calculate_shares(item_totals, num_subtotal, num_total)

if __name__ == "__main__":
    main()
