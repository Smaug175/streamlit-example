import streamlit as st


def authenticated_menu():
    # Show a navigation menu for authenticated users
    st.sidebar.page_link("app.py", label="Switch accounts")
    st.sidebar.page_link("pages/user.py", label="Your profile")
    st.sidebar.page_link("pages/normal_introduce.py", label="普通抽介绍")
    st.sidebar.page_link("pages/normal.py", label="普通抽计算")
    if st.session_state.role in ["admin", "super-admin"]:
        st.sidebar.page_link("pages/admin.py", label="Manage users")
        st.sidebar.page_link(
            "pages/super-admin.py",
            label="Manage admin access",
            disabled=st.session_state.role != "super-admin",
        )


def unauthenticated_menu():
    # Show a navigation menu for unauthenticated users
    st.sidebar.page_link("app.py", label="Log in")


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