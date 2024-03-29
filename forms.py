from wtforms import Form, TextField, validators, SubmitField
from flask import Flask, render_template, request
from utils import eval_from_input

#create app
app = Flask(__name__)

class WebForm(Form):
    eval_text = TextField("Please enter some text to be evaluated",
                          validators=[validators.InputRequired()])
    submit = SubmitField("Enter")

@app.route("/", methods=['GET', 'POST'])
def home():
    "home page with form"
    form = WebForm(request.form)

    if request.method == 'POST' and form.validate():
        link = request.form['eval_text']
        return render_template('eval_text.html',
                               input=eval_from_input(link=link))

    return render_template('index.html', form=form)

if __name__ == "__main__":
    print(("* Loading model and Flask starting server..."
           "please wait until server has fully started"))
    # Run app
    app.run(host="0.0.0.0")