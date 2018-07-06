from functools import wraps
from flask import g, request, redirect, url_for


def login_required(f):
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if g.user is None:
            return redirect(url_for('login', next=request.url))
        return f(*args, **kwargs)
    return decorated_function


@app.route('/secret')
@login_required
def secret():
    pass



@app.route('/grade', methods=['POST'])
def update_grade():
    json_data = request.get_json()
    if 'student_id' not in json_data:
        abort(400)
    # update database
    return "success!"
