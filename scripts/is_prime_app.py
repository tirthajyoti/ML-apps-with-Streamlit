import streamlit as st

st.title("My first app with Streamlit")
st.header("Is it prime?")

st.markdown("We determine primality using a simple code as follows")
st.code('''def is_prime(number):
    """
    Determines primality
    """
    from math import ceil,sqrt
    flag = True
    if number%2==0:
        flag=False
        return flag,0
    sqrt_num = ceil(sqrt(number))
    st.write(f"Checking divisibility up to **{sqrt_num}**")
    for i in range(2,sqrt_num):
        if number%i == 0:
            flag = False
            return flag,i
    return flag,i''',language='python')

number = st.number_input('Insert a number')
st.write('The current number is ', number)

def is_prime(number):
    """
    Determines primality
    """
    from math import ceil,sqrt
    flag = True
    if number%2==0:
        flag=False
        return flag,2
    sqrt_num = ceil(sqrt(number))
    st.write(f"Checking divisibility up to **{sqrt_num}**")
    for i in range(2,sqrt_num):
        if number%i == 0:
            flag = False
            return flag,i
    return flag,i

decision,divisor = is_prime(number)

if decision:
    st.write("Yes, the given number is prime")
else:
    st.write(f"No, the given number is not a prime.\nIt is divisible by **{divisor}**")
