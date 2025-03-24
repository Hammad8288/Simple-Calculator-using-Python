import streamlit as st

def main():

    st.title("Simple Calculator")
    st.write("Enter the number you want to calculate")


    # Create two columns for number inputs
    col1, col2 = st.columns(2)

    # Get the input numbers from the columns
    with col1:
        num1 = st.number_input("Enter the first number")

    with col2:
        num2 = st.number_input("Enter the second number")


    # Create a dropdown menu for the operation
    operation = st.selectbox("Select the operation", ["Addition", "Subtraction", "Multiplication", "Division"])


    #calculate button
    if st.button("Calculate"):
        try:
            if operation == "Addition":
                result = num1 + num2
            
            elif operation == "Subtraction":
                result = num1 - num2

            elif operation == "Multiplication":
                result = num1 * num2

            elif operation == "Division":
                if num2!= 0:
                    result = num1 / num2
                else:
                    st.error("Cannot divide by zero!")

            st.success(f"The result of {num1} {operation} {num2} is: {result}")
        
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
                

# Run the main function if the script is executed directly
if __name__ == "__main__":
    main()
