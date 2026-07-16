from flask import Flask, render_template, request, redirect, url_for
from testapp import mainapp



@mainapp.route('/', methods=['GET', 'POST'])

@mainapp.route('/home', methods=['GET', 'POST'])
def home():
    return render_template('home.html', title='Home')


@mainapp.route('/themaster', methods=['GET', 'POST'])
def themaster():
    return render_template('themaster.html', title='The Master')

@mainapp.route('/rlt', methods=['GET', 'POST'])
def rlt():
    return render_template('rlt.html', title='Road Less Traveled')

@mainapp.route('/pursuit', methods=['GET', 'POST'])
def pursuit():
    return render_template('pursuit.html', title='Pursuit For Practicality')

@mainapp.route('/plasticshorts', methods=['GET', 'POST'])
def plasticshorts():
    return render_template('plasticshorts.html', title='Plastic Shorts')

@mainapp.route('/tuxedo', methods=['GET', 'POST'])
def tuxedo():
    return render_template('tuxedo.html', title='Tuxedo')

@mainapp.route('/senses', methods=['GET', 'POST'])
def senses():
    return render_template('senses.html', title='In The Senses')

@mainapp.route('/meta', methods=['GET', 'POST'])
def meta():
    return render_template('meta.html', title='Metamorphosis')

@mainapp.route('/spacebar', methods=['GET', 'POST'])
def spacebar():
    return render_template('spacebar.html', title='Welcome To The Spacebar')

@mainapp.route('/crimson', methods=['GET', 'POST'])
def crimson():
    return render_template('crimson.html', title='Crimson Eyes')

@mainapp.route('/hslm', methods=['GET', 'POST'])
def hslm():
    return render_template('hslm.html', title='Hot Stick Line Mechanic')

@mainapp.route('/clouds', methods=['GET', 'POST'])
def clouds():
    return render_template('clouds.html', title='Clouds On A Windy Day')

@mainapp.route('/spiritual', methods=['GET', 'POST'])
def spiritual():
    return render_template('spiritual.html', title='Spiritual Practices')