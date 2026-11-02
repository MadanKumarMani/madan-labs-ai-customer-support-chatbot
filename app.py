import streamlit as st
from agents.customer_ai_agent import customer_ai_chat


st.set_page_config(
    page_title="Madan labs AI Assistant"
)


# ---------- SESSION STATE ----------

if "logged_in" not in st.session_state:
    st.session_state.logged_in = False


if "employee_messages" not in st.session_state:
    st.session_state.employee_messages = []


if "customer_messages" not in st.session_state:
    st.session_state.customer_messages = []



# ---------- HEADER ----------

col1, col2 = st.columns([5,1])


with col1:
    st.title("Madanlabs AI Intelligent Assistant")


with col2:

    if st.session_state.logged_in:

        if st.button("Logout"):

            st.session_state.logged_in = False

            st.session_state.employee_messages = []

            st.rerun()



role = st.radio(
    "Continue as:",
    [
        "Customer",
        "Employee"
    ]
)





# ================= CUSTOMER =================


if role == "Customer":


    st.subheader(
        "Customer Assistant"
    )


    # show old messages

    for msg in st.session_state.customer_messages:


        with st.chat_message(
            msg["role"]
        ):

            st.write(
                msg["content"]
            )



    question = st.chat_input(
        "Have an enquiry ? ask here"
    )



    if question:

    # save customer message
        st.session_state.customer_messages.append(
            {
                "role": "user",
                "content": question
            }
        )

        # LangChain Agent response
        with st.spinner("AI Agent thinking..."):

            answer = customer_ai_chat(question)

        # save AI response
        st.session_state.customer_messages.append(
            {
                "role": "assistant",
                "content": answer
            }
        )

        st.rerun()



# ================= EMPLOYEE =================


else:


    st.subheader(
        "Employee Assistant"
    )


    if st.session_state.logged_in == False:


        email = st.text_input(
            "Email"
        )


        password = st.text_input(
            "Password",
            type="password"
        )


        if st.button(
            "Login"
        ):


            if (
                email=="admin@gmail.com"
                and password=="123"
            ):


                st.session_state.logged_in = True


                st.rerun()


            else:


                st.error(
                    "Invalid Login"
                )



    else:


        st.success(
            "Employee Logged In"
        )


        # display chat history


        for msg in st.session_state.employee_messages:


            with st.chat_message(
                msg["role"]
            ):


                st.write(
                    msg["content"]
                )



        q = st.chat_input(
            "Ask CRM Assistant"
        )



        if q:


            st.session_state.employee_messages.append(
                {
                    "role":"user",
                    "content":q
                }
            )



            # temporary AI response

            st.session_state.employee_messages.append(
                {
                    "role":"assistant",
                    "content":
                    "CRM AI response will appear here"
                }
            )


            st.rerun()