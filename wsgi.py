import os, sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from todoit import create_app
app = create_app("Production")

if __name__ == "__main__":
    app.run()