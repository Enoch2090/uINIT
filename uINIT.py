import streamlit as st
import os
import base64


# ----------------Data----------------
enviro_list = []
if not os.path.exists("sh/packages"):
    "Package file not found."
    raise FileNotFoundError
else:
    dir_list = os.listdir("sh/packages")
    for item in dir_list:
        if os.path.isfile(os.path.join("sh/packages/", item)) and item != '.DS_Store':
            package_name = item.split(".")[0]
            enviro_list.append(package_name)


class sh_file(object):
    def __init__(self):
        self.code = ""
        self.gen_code()
        self.packages = []

    def __str__(self):
        return self.code

    def gen_code(self):
        self.code = ""
        with open('sh/header.sh', 'r') as f:
            header_str = f.readlines()
        for line in header_str:
            self.code += line
        return

    def add_package(self, packages):
        self.gen_code()
        for package in packages:
            if not(package in self.packages) and (package != "zsh"):
                package_fname = "sh/packages/%s.sh" % package
                self.code += get_code_from_file(package_fname)
                self.code += "\n"
        if "zsh" in packages:
            package_fname = "sh/packages/%s.sh" % "zsh"
            self.code += get_code_from_file(package_fname)


def get_code_from_file(package_fname):
    code = ""
    with open(package_fname, 'r') as f:
        package_code = f.readlines()
        for line in package_code:
            code += line
    return code


def get_file_download_link(code):
    fname = "uINIT"
    b64 = base64.b64encode(code.encode()).decode()
    href = f'<a href="data:file/sh;base64,{b64}" download="%s.sh">Download shell script</a>' % fname
    return href


# ----------------Menu----------------
st.sidebar.title('uINIT')
option = st.sidebar.selectbox(
    'Menu',
    ['Generate', 'Help', 'About'])


# ----------------Functionalities----------------
if option == 'Generate':
    enviro_checked = st.multiselect(label="ENVIRON", options=enviro_list)
    if len(enviro_checked) > 0:
        if len(enviro_checked) == 1:
            "1 package chosen."
        else:
            "%s packages chosen." % len(enviro_checked)
        sh_code = sh_file()
        sh_code.add_package(enviro_checked)
        st.markdown(get_file_download_link(
            sh_code.__str__()), unsafe_allow_html=True)
        st.code(body=sh_code, language='shell')

    else:
        "No packages chosen."
elif option == 'Help':
    f = open('README.md', 'r')
    lines = f.readlines()
    f.close()
    README = ''
    for line in lines:
        README += line
    st.markdown(README)

elif option == 'About':
    st.title('About')
    '''
    [WhiteGivers](https://whitegivers.com).
    [Enoch2090](https://enoch2090.me).
    '''
# ----------------Hide Development Menu----------------
hide_menu_style = """
        <style>
        #MainMenu {visibility: hidden;}
        </style>
        """
st.markdown(hide_menu_style, unsafe_allow_html=True)
