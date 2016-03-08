from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db
from flask_mail import Mail

migrate = Migrate(app, db)

mail = Mail(app)
app.config.update(
	DEBUG=True,
	#EMAIL SETTINGS
	MAIL_SERVER='smtp.yandex.com.tr',
	MAIL_PORT=465,
	MAIL_USE_SSL=True,
	MAIL_USERNAME = 'kasim@ridvantuncel.com',
	MAIL_PASSWORD = 'Rido1225'
	)

mail = Mail(app)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
    manager.run()
