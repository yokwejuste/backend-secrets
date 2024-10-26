from flask import Flask
from flask_principal import Principal, Permission, RoleNeed

app = Flask(__name__)
principals = Principal(app)

admin_permission = Permission(RoleNeed('admin'))


@app.route('/admin')
@admin_permission.require(http_exception=403)
def admin_page():
    return "Welcome Admin!"


if __name__ == "__main__":
    app.run()
