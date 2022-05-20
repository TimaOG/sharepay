import datetime
import os
from flask import Flask, render_template, session, redirect, url_for, abort, request, flash
from flask_login import login_user, login_required, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash
from werkzeug.utils import secure_filename

from config import app, db
from models import Users, Fund


@app.route("/", endpoint='openMain')
def openMain():
	buttonText = ''
	isLoginUrl = False
	if current_user.is_authenticated:
		buttonText = 'Личный кабинет'
		isLoginUrl = True
	else:
		buttonText = 'Войти'
		isLoginUrl = False
	return render_template('startPage.html', buttonText=buttonText, isLoginUrl=isLoginUrl)


@app.route("/contacts")
def openContacts():
	return render_template('contactsPage.html')


@app.route("/funds")
def openFunds():
	funds = Fund.query.all()
	return render_template('fundsPage.html', funds=funds)


@app.route("/register", methods=["GET","POST"])
def register():
	name = request.form.get('name')
	email = request.form.get('email')
	password1 = request.form.get('password')
	password2 = request.form.get('password2')

	if request.method == 'POST':
		if not (email or password1 or password2):
			flash('Не все поля заполнены')
		elif password1 != password2:
			flash('Пароли не совпадают')
		else:
			hashP = generate_password_hash(password1)
			new_user = Users(name=name, email=email, password=hashP, isAdmin=False)
			db.session.add(new_user)
			db.session.commit()

			return redirect(url_for('login'))
	return render_template('registerPage.html')


@app.route("/login", methods=["GET","POST"])
def login():
	email = request.form.get('email')
	password = request.form.get('password')

	if email and password:
		user = Users.query.filter_by(email=email).first()

		if user and check_password_hash(user.password, password):
			login_user(user)

			return redirect(url_for('openMain'))
		else:
			flash('Неправильно введён пароль или логин')

	return render_template('login.html')


@app.route("/logout", methods=["GET","POST"])
@login_required #ТОЛЬКО ДЛЯ АВТОРИЗОВАННЫХ
def logout():
	logout_user()
	return redirect(url_for('openMain'))


@app.route("/admin", methods=["GET","POST"])
@login_required
def openAdmin():
	adminID = current_user.get_id()
	user = Users.query.filter_by(id=adminID).first()
	if user.isAdmin:
		funds = Fund.query.all()
		allUsers = Users.query.all()
		if request.method == 'POST':
			for fund in funds:
				cb = request.form.getlist(f'checkFundId_{fund.id}')
				if cb != []:
					i = db.session.query(Fund).filter(Fund.id == fund.id).one()
					db.session.delete(i)
					db.session.commit()
					os.remove(fund.fundImageLink)
					for cUser in allUsers:
						tmpFound = cUser.trustFunds
						tmpFound.remove(fund.id)
						cUser.trustFunds = tmpFound
						db.session.add(cUser)
						db.session.commit()
			funds = Fund.query.all()
			#сделать удаление для юзеров
		return render_template('adminPage.html', funds=funds)
	else:
		return redirect(url_for('openMain'))


@app.route("/account", methods=["GET","POST"])
@login_required
def openLC():
	userId = current_user.get_id()
	user = Users.query.filter_by(id=userId).first()
	fundsIds = user.trustFunds
	fundsIdsNow = []
	if not fundsIds:
		fundsIds = []
	funds = Fund.query.all()
	if request.method == 'POST':
		email = request.form.get('email')
		password1 = request.form.get('password1')
		password2 = request.form.get('password2')
		password3 = request.form.get('password3')
		if password1 != password2:
			flash('Пароли не совпадают')
		else:
			if password3:
				hashP = generate_password_hash(password3)
				user.password = hashP 
		for fund in funds:
			cb = request.form.getlist(f'checkFundId_{fund.id}')
			if cb != []:
				fundsIdsNow.append(fund.id)
		user.trustFunds = fundsIdsNow
		db.session.add(user)
		db.session.commit()
		fundsIds = user.trustFunds
	return render_template('accountPage.html', user=user, fundsIds=fundsIds, funds=funds)


@app.route("/admin/addfund", methods=["GET","POST"])
@login_required
def openAdminAddFund():
	adminID = current_user.get_id()
	user = Users.query.filter_by(id=adminID).first()
	if user.isAdmin:
		fundName = request.form.get('fundname')
		fundDiscrib = request.form.get('funddisk')
		fundLink = request.form.get('fundlink')
		if request.method == 'POST':
			fundImage = request.files['imagefile']
			if not fundImage:
				flash('файл не загружен')
			else:
				filename = secure_filename(fundImage.filename)
				fundImage.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
			if not (fundName or fundDiscrib or fundLink):
				flash('Не все поля заполнены')
			else:
				filename = secure_filename(fundImage.filename)
				fileImagePath = str(os.path.join(app.config['UPLOAD_FOLDER'], filename))
				new_fund = Fund(fundName=fundName, fundDiscrib=fundDiscrib, fundLink=fundLink, fundImageLink=fileImagePath)
				db.session.add(new_fund)
				db.session.commit()
				return redirect(url_for('openAdmin'))
		return render_template('addFundPage.html')
	else:
		return redirect(url_for('openMain'))
	return render_template('addFundPage.html')


if __name__ == "__main__":
	app.run(debug=True)