import sys

from streamlit.web import cli as strcli

if __name__ == "__main__":
    app_path = "demo_app/demo_app.py"
    sys.argv = ["streamlit", "run", app_path]
    sys.exit(strcli.main())
