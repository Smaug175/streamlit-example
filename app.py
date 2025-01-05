import streamlit as st
from menu import menu
from bin.utils.SQLite_control import UserControl


# Initialize st.session_state.role to None
if "role" not in st.session_state or "login" not in st.session_state or st.session_state.login == False or st.session_state.role == None:
    st.session_state.role = None
    st.session_state.login = False

@st.fragment
def login_wiget():
    # Widgets for login
    st.write("# ⌨️🔑登录")
    st.write("##### 请输入账号和密码：")
    st.session_state.id_number = st.text_input(label="账号：", value="")
    st.session_state.password = st.text_input(label="密码：", value="")

if not st.session_state.login:
    login_wiget()
    if st.button("登录", disabled=st.session_state.login, use_container_width=True, type="primary"):
        user_control = UserControl()
        input = {
            'id': st.session_state.id_number,
            'password': st.session_state.password
        }
        
        if input['id'] == '' or input['password'] == '':
            st.error("⚠️账号或密码不能为空！")
        else:
            result = user_control.query(input)
            if result[0]:
                st.session_state.login = True
                st.session_state.role = result[1]
                st.rerun()
            else:
                st.session_state.login = False
                message = result[1]
                st.error('⚠️'+message)
else:
    st.write("# 🎉登录成功！")
    st.write("账号是：", st.session_state.id_number)
    st.write("密码是：", st.session_state.password)
    st.write("角色是：", st.session_state.role)


menu() # Render the dynamic menu