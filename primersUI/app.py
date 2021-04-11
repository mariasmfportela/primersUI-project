import os
from flask import Flask
from flask import (flash, request, render_template, url_for, redirect, session)

import script

# create and configure the app
app = Flask(__name__)
app.config.from_mapping(
    SECRET_KEY='dev',
)


# start page where the user inputs sequence and preferences
@app.route('/', methods=['GET', 'POST'])
def start():
    error = None
    if request.method == 'POST':
        exon1 = request.form['exon1']
        exon2 = request.form['exon2']
        gc_content = request.form['gc-content']
        primer_length = request.form['primer-length']

        # form validation
        try:
            int(gc_content)
        except:
            error = "Please insert valid number for GC content"

        try:
            int(primer_length)
        except:
            error = "Please insert valid number for primer length"

        if len(exon1) < len(primer_length) or len(exon2) < len(primer_length):
            error = "The number of nucleotides must be bigger than primer length"

        # No errors, process input and show results page
        if error is None:
            hits = script.hits_from_exons(exon1, exon2, int(gc_content), int(primer_length))
            session["hits"] = hits
            return redirect(url_for('results'))

        # Form has errors
        flash(error)

    return render_template('start.html')


# show results page with primer candidates
@app.route('/results')
def results():
    hits = session["hits"]
    return render_template('results.html', forward=str(hits["forward"]), reverse=str(hits["reverse"]))
