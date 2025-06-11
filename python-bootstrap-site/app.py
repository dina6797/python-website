from app import create_app, db
from app.models import User

app = create_app()

@app.before_first_request
def create_tables():
    db.create_all()
    if not User.query.first():
        db.session.add_all([User(name='Alice'), User(name='Bob')])
        db.session.commit()

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)