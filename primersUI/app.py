import os
from flask import Flask
from flask import (flash, request, render_template, url_for, redirect)

import script

# create and configure the app
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
)


# start page where the user inputs sequence and preferences
@app.route('/', methods=['GET', 'POST'])
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

        if error is None:
            hits = script.hits_from_exons(exon1, exon2)
            return redirect(url_for('results', forward=str(hits["forward"]), reverse=str(hits["reverse"])))

        flash(error)

    return render_template('start.html')

# show results page with primer candidates
@app.route('/results')
def results():
    forward = request.args['forward']
    reverse = request.args['reverse']
    return render_template('results.html', forward=forward, reverse=reverse)
