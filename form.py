import streamlit as st
import re
from data import job_data, tech_suggestions

def show_form():
    if st.session_state.get("page") != "form":
        return

    st.set_page_config(page_title="TalentScout Hiring Assistant", layout="centered")

    st.title("🤖 TalentScout Hiring Assistant")

    # ---------------- SESSION ---------------- #
    if "step" not in st.session_state:
        st.session_state.step = 1

    if "edit_mode" not in st.session_state:
        st.session_state.edit_mode = None

    if "start_interview" not in st.session_state:
        st.session_state.start_interview = False

    if "previous_step" not in st.session_state:
        st.session_state.previous_step = 1

    fields = ["first_name", "middle_name", "last_name", "email", "country_code", "phone", "experience", "location"]
    if "tech_stack" not in st.session_state:
        st.session_state.tech_stack = []
    for f in fields:
        if f not in st.session_state:
            st.session_state[f] = [] if f == "tech_stack" else ""

    # ---------------- VALIDATIONS ---------------- #
    
    def is_valid_first_name(name):
        return re.fullmatch(r'^[A-Za-z]{2,30}$', name)

    def is_valid_middle_name(name):
        return name == "" or re.fullmatch(r'^[A-Za-z]{1,30}$', name)

    def is_valid_last_name(name):
        return re.fullmatch(r'^[A-Za-z]{1,30}$', name)

    def is_valid_email(email):
        return re.fullmatch(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-z]{2,}$', email)

    def is_valid_country_code(code):
        return re.fullmatch(r'^\+[0-9]{1,3}$', code)

    def is_valid_phone(phone):
        return re.fullmatch(r'^[0-9]{10}$', phone)

    def is_valid_experience(exp):
        return re.fullmatch(r'^(?:[0-9]|[1-3][0-9]|40)(\.\d{1})?$', exp)

    def is_valid_location(loc):
        return re.fullmatch(r'^[A-Za-z ]{2,50}$', loc)
    
    # ---------------- PROGRESS ---------------- #
    if st.session_state.page == "form":
        st.progress(min((st.session_state.step - 1) / 12, 1.0))

    # ---------------- SHOW DATA ---------------- #
        def show_user_data():

            if st.session_state.first_name:
                col1, col2 = st.columns([4,1])
                with col1:
                    st.info(f"👤 Full Name: {st.session_state.first_name} {st.session_state.middle_name} {st.session_state.last_name}")
                with col2:
                    if st.button("Edit", key="edit_name"):
                        st.session_state.edit_mode = "name"
                        st.session_state.previous_step = st.session_state.step
                        st.session_state.step = 1
                        st.rerun()

            if st.session_state.email:
                col1, col2 = st.columns([4,1])
                with col1:
                    st.info(f"📧 Email: {st.session_state.email}")
                with col2:
                    if st.button("Edit", key="edit_email"):
                        st.session_state.edit_mode = "email"
                        st.session_state.previous_step = st.session_state.step
                        st.session_state.step = 4
                        st.rerun()

            if st.session_state.phone:
                col1, col2 = st.columns([4,1])
                with col1:
                    st.info(f"📱 Phone: {st.session_state.country_code}{st.session_state.phone}")
                with col2:
                    if st.button("Edit", key="edit_phone"):
                        st.session_state.edit_mode = "phone"
                        st.session_state.previous_step = st.session_state.step
                        st.session_state.step = 5
                        st.rerun()

            if st.session_state.experience:
                col1, col2 = st.columns([4,1])
                with col1:
                    st.info(f"💼 Experience: {st.session_state.experience} years")
                with col2:
                    if st.button("Edit", key="edit_exp"):
                        st.session_state.edit_mode = "experience"
                        st.session_state.previous_step = st.session_state.step
                        st.session_state.step = 7
                        st.rerun()

            if st.session_state.location:
                col1, col2 = st.columns([4,1])
                with col1:
                    st.info(f"📍 Location: {st.session_state.location}")
                with col2:
                    if st.button("Edit", key="edit_location"):
                        st.session_state.edit_mode = "location"
                        st.session_state.previous_step = st.session_state.step
                        st.session_state.step = 8
                        st.rerun()

            # ✅ Desired Job + Edit
            if st.session_state.get("role"):
                col1, col2 = st.columns([4,1])

                with col1:
                    st.markdown(f"""
                    <div style="padding:12px; border-radius:10px; background-color:#1e293b; color:#38bdf8;">
                    <b>🎯 Desired Job:</b> {st.session_state.department} → {st.session_state.domain} → {st.session_state.role}
                    </div>
                    """, unsafe_allow_html=True)

                with col2:
                    if st.button("Edit", key="edit_role"):
                        st.session_state.edit_mode = "role"

                        # 🔥 CLEAR OLD DATA
                        st.session_state.domain = ""
                        st.session_state.role = ""
                        st.session_state.tech_stack = []
                        st.session_state.previous_step = st.session_state.step
                        st.session_state.step = 9
                        st.rerun()

            st.markdown("<div style='margin-top:15px'></div>", unsafe_allow_html=True)
            if st.session_state.tech_stack:
                col1, col2 = st.columns([4,1])
                with col1:
                    st.info(f"💻 Tech Stack: {', '.join(st.session_state.tech_stack)}")
                with col2:
                    if st.button("Edit", key="edit_stack"):
                        st.session_state.edit_mode = "tech"
                        st.session_state.previous_step = st.session_state.step
                        st.session_state.step = 12
                        st.rerun()
            
        # ---------------- STEPS ---------------- #

        if not st.session_state.start_interview:

            # NAME
            if st.session_state.step == 1:
                show_user_data()
                first = st.text_input("First Name", value=st.session_state.first_name)

                if st.button("Next"):
                    if not is_valid_first_name(first):
                        st.error("❌ First name must be 2–30 alphabets only (no spaces/numbers)")
                    else:
                        st.session_state.first_name = first
                        st.session_state.step = 2
                        st.rerun()

            elif st.session_state.step == 2:
                show_user_data()
                middle = st.text_input("Middle Name", value=st.session_state.middle_name)

                if st.button("Next"):
                    if not is_valid_middle_name(middle):
                        st.error("❌ Middle name must be alphabets only (1–30 chars)")
                    else:
                        st.session_state.middle_name = middle
                        st.session_state.step = 3
                        st.rerun()

            elif st.session_state.step == 3:
                show_user_data()
                last = st.text_input("Last Name", value=st.session_state.last_name)

                if st.button("Save" if st.session_state.edit_mode == "name" else "Next"):
                    if not is_valid_last_name(last):
                        st.error("❌ Last name must be alphabets only (1–30 chars)")
                    else:
                        st.session_state.last_name = last
                        if st.session_state.edit_mode == "name":
                            st.session_state.step = st.session_state.previous_step
                            st.session_state.edit_mode = None
                        else:
                            st.session_state.step = 4
                        st.rerun()

            # EMAIL
            elif st.session_state.step == 4:
                show_user_data()
                email = st.text_input("Email", value=st.session_state.email)

                if st.button("Save" if st.session_state.edit_mode == "email" else "Next"):
                    if not is_valid_email(email):
                        st.error("❌ Enter valid email (example@gmail.com)")
                    else:
                        st.session_state.email = email
                        if st.session_state.edit_mode:
                            st.session_state.step = st.session_state.previous_step   # 🔥 GO BACK
                            st.session_state.edit_mode = None
                        else:
                            st.session_state.step = 5
                        st.rerun()

            # PHONE
            elif st.session_state.step == 5:
                show_user_data()
                code = st.text_input("Country Code", value=st.session_state.country_code)

                if st.button("Next"):
                    if not is_valid_country_code(code):
                        st.error("❌ Invalid country code (example: +91)")
                    else:
                        st.session_state.country_code = code
                        st.session_state.step = 6
                        st.rerun()

            elif st.session_state.step == 6:
                show_user_data()
                phone = st.text_input("Phone Number", value=st.session_state.phone)

                if st.button("Save" if st.session_state.edit_mode == "phone" else "Next"):
                    if not is_valid_phone(phone):
                        st.error("❌ Phone must be exactly 10 digits (no country code)")
                    else:
                        st.session_state.phone = phone
                        if st.session_state.edit_mode:
                            st.session_state.step = st.session_state.previous_step   # 🔥 GO BACK
                            st.session_state.edit_mode = None
                        else:
                            st.session_state.step = 7
                        st.session_state.edit_mode = None
                        st.rerun()

            # EXPERIENCE
            elif st.session_state.step == 7:
                show_user_data()
                exp = st.text_input("Experience", value=st.session_state.experience)

                if st.button("Save" if st.session_state.edit_mode == "experience" else "Next"):
                    if not is_valid_experience(exp):
                        st.error("❌ Experience must be between 0–40 (e.g., 2 or 2.5)")
                    else:
                        st.session_state.experience = exp
                        if st.session_state.edit_mode:
                            st.session_state.step = st.session_state.previous_step   # 🔥 GO BACK
                            st.session_state.edit_mode = None
                        else:
                            st.session_state.step = 8
                        st.session_state.edit_mode = None
                        st.rerun()

            # LOCATION
            elif st.session_state.step == 8:
                show_user_data()
                location = st.text_input("Current Location", value=st.session_state.location)

                if st.button("Save" if st.session_state.edit_mode == "location" else "Next"):
                    if not is_valid_location(location):
                        st.error("❌ Location must be 2–50 alphabets only")
                    else:
                        st.session_state.location = location

                        if st.session_state.edit_mode == "location":
                            st.session_state.step = st.session_state.previous_step
                            st.session_state.edit_mode = None
                        else:
                            st.session_state.step = 9

                        st.rerun()

            # DEPARTMENT
            elif st.session_state.step == 9:
                show_user_data()
                dept = st.selectbox("Department", list(job_data.keys()))

                if st.button("Save" if st.session_state.edit_mode == "role" else "Next"):
                    st.session_state.department = dept

                    if st.session_state.edit_mode == "role":
                        st.session_state.step = 10
                    else:
                        st.session_state.step = 10

                    st.rerun()

            # DOMAIN
            elif st.session_state.step == 10:
                show_user_data()
                domain = st.selectbox("Domain", list(job_data[st.session_state.department].keys()))

                if st.button("Save" if st.session_state.edit_mode == "role" else "Next"):
                    st.session_state.domain = domain
                    st.session_state.step = 11
                    st.rerun()

            # ROLE
            elif st.session_state.step == 11:
                show_user_data()
                role = st.selectbox("Role", job_data[st.session_state.department][st.session_state.domain])

                if st.button("Save" if st.session_state.edit_mode == "role" else "Confirm"):
                    st.session_state.role = role
                    st.session_state.step = 12
                    st.session_state.edit_mode = None
                    st.rerun()

            # TECH STACK
            elif st.session_state.step == 12:
                show_user_data()

                role = st.session_state.role
                suggestions = tech_suggestions.get(role, [])

                selected = st.multiselect(
                    "Select your Tech Stack",
                    suggestions,
                    default=st.session_state.tech_stack
                )
                custom = st.text_input("Add more skills (comma separated)")

                if st.button("Save" if st.session_state.edit_mode == "tech" else "Next"):
                    custom_list = [x.strip() for x in custom.split(",") if x.strip()]
                    final_stack = list(set(selected + custom_list))

                    if not final_stack:
                        st.error("Enter at least one skill")
                    else:
                        st.session_state.tech_stack = final_stack

                        if st.session_state.edit_mode == "tech":
                            st.session_state.step = st.session_state.previous_step   # 🔥 FIX
                            st.session_state.edit_mode = None
                        else:
                            st.session_state.step = 13

                        st.rerun()

            # FINAL
            elif st.session_state.step == 13:
                show_user_data()
                st.markdown("<div style='margin-top:30px'></div>", unsafe_allow_html=True)
                st.success("🎉 All details captured successfully!")
                st.markdown("<br>", unsafe_allow_html=True)

                if st.button("🚀 Start Interview"):
                    st.session_state.page = 'loading'
                    st.rerun()

if __name__ == "__main__":
    show_form()