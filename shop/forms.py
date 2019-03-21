from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Regexp, NumberRange
from shop.models import User


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired('Please enter your username'), Length(min=3, max=15)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(),Regexp('^.{6,8}$',
                              message='Your password should be between 6 and 8 characters long.')])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError('Username already exist. Please choose a different one.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('This email is already registered. Please choose a different one.')


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class SearchForm(FlaskForm):
    search = StringField('')

class CheckoutForm(FlaskForm):
    cardnumber = StringField('Card Number', validators = [DataRequired(), Regexp('^[0-9]{16}$', message='Your card number should be 16 characters long.')]) 
    cardname = StringField('Name on Card', validators = [DataRequired()])
    cardexp = IntegerField('Expiration month', validators = [DataRequired(), NumberRange(min=0,max=12, message ='Please enter a valid month between 01 and 12')])
    cardyearexp = IntegerField('Expiration year', validators = [DataRequired(), NumberRange(min=19, message ='Please enter a valid year')])  
    cardcvv = IntegerField('CVV', validators = [DataRequired(), Regexp('^[0-9]{3}$', message='Your CVV is the 3-digit number at the back of your card.')])
    address = StringField('Address', validators = [DataRequired()])
    city = StringField('City', validators = [DataRequired()])
    postcode = StringField('Postcode', validators = [DataRequired()])
    phonenumber = StringField('Phone Number', validators = [DataRequired(), Regexp('^[0-9]{11}$', message='Please input a valid phone number.')])
    submit = SubmitField('Confirm Purchase')


    