from flask import (
    Blueprint, render_template
)

from homework4.db import get_db

bp = Blueprint('secondpart', __name__, url_prefix='/secondpart')


@bp.route('/names/')
def unique_artist():
    '''this function returned view with unique artist of db'''
    artists = get_db().execute('SELECT COUNT (DISTINCT artist) FROM tracks').fetchone()[0]
    return render_template('secondpart/artist.html', artists=artists)


@bp.route('/tracks/')
def quantity_tracks():
    '''this function returned view with quantity tracks of db'''
    track = get_db().execute('SELECT COUNT (*) FROM tracks').fetchone()[0]
    return render_template('secondpart/quantity-tracks.html', track=track)


@bp.route('/tracks/<genre>')
def tracks_by_genre(genre):
    '''this function returned view with number of tracks for view of db'''
    track_genre = get_db().execute('SELECT COUNT(*) FROM tracks WHERE genre = ?', (genre,)).fetchone()[0]
    return render_template('secondpart/quantity-tracks-genre.html', track_genre=track_genre)


@bp.route('/tracks-sec/')
def tracks_sec():
    '''this function returned view with title of song and length of song of db'''
    track_sec = get_db().execute('SELECT title, lenght FROM tracks').fetchall()
    return render_template('secondpart/track-sec.html', track_sec=track_sec)


@bp.route('/tracks-sec/statistics/')
def tracks_statis():
    '''this function returned view with mean of length and sum of all length of db'''
    statis = get_db().execute('SELECT AVG(lenght), sum(lenght) FROM tracks').fetchall()
    return render_template('secondpart/statis.html', statis=statis)
