import os
from flask import Flask
from flask import (flash, request, render_template, url_for)

# create and configure the app
app = Flask(__name__)


# start page where the user inputs sequence and preferences
@app.route('/', methods=('GET', 'POST'))
def start():
    if request.method == 'POST':
        exon1 = request.form['exon1']
        exon2 = request.form['exon2']
        error = None

        # form validation
        if not exon1:
            error = 'Exon 1 sequence is required.'
        elif not exon2:
            error = 'Exon 2 sequence is required.'

        flash(error)

    return render_template('start.html')
