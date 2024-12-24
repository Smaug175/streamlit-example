import streamlit as st


def authenticated_menu():
    st.sidebar.header("普通抽")
    st.sidebar.page_link("pages/1_normal_introduce.py", label="📣普通抽介绍")
    st.sidebar.page_link("pages/2_normal_caculate.py", label="🧮普通抽计算")

    st.sidebar.divider()

    st.sidebar.header("账户管理")
    st.sidebar.page_link("pages/user.py", label="你的账户")

    if st.session_state.role in ["管理员", "超级管理员"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "超级管理员",
        )

    st.sidebar.divider()

    if st.sidebar.button("退出登录", use_container_width=True):
        st.session_state.role = None
        st.rerun()


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="登录")


def menu():
    # 确定用户是否已登录，然后显示正确的导航菜单
    if "role" not in st.session_state or st.session_state.role is None:
        unauthenticated_menu()
        return
    authenticated_menu()


def menu_with_redirect():
    # 如果未登录，则将用户重定向到主页面，否则继续渲染导航菜单
    if "role" not in st.session_state or st.session_state.role is None:
        st.switch_page("app.py")
    menu()