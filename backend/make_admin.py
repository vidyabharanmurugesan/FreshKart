from run import create_app
from app.models.user_model import User
app = create_app()
with app.app_context():
    users = User.get_all()
    for user_data in users:
        user = User.from_dict(user_data)
        if user:
            user.role = 'admin'
            user.save()
    print('Done')