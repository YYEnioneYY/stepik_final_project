from flask import Flask, render_template
import random


def get_width_height():
    return 800, 500

app = Flask(__name__)

@app.route("/")
def ballons():
    i = random.randint(1,11)
    ballon_name = "ballon ("+str(i)+").jpg"
    width_b, height_b = get_width_height()
    return render_template('ballons.html', ballon_name = ballon_name, width = str(width_b), height = str(height_b))

if __name__ == "__main__":
    app.run(debug=True)

