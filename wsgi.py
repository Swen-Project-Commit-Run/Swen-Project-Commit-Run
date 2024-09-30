import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup


from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( view_applicants_for_job, view_applicants_for_employer, view_jobs, remove_listing, remove_user, create_listing, apply_for_job, create_user, create_admin, create_employer, create_applicant, get_all_users_json, get_all_users, initialize )


# This commands file allow you to create convenient CLI commands for testing controllers

app = create_app()
migrate = get_migrate(app)

# This command creates and initializes the database
@app.cli.command("init", help="Creates and initializes the database")
def init():
    initialize()
    print('database intialized')

'''
User Commands
'''

# Commands can be organized using groups

# create a group, it would be the first argument of the comand
# eg : flask user <command>
user_cli = AppGroup('user', help='User object commands') 

# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("firstName", default="rob")
@click.argument("lastName", default="man")
@click.argument("email", default="rob@email.com")
@click.argument("password", default="robpass")
def create_user_command(firstName, lastName, email, password):
    create_user(firstName, lastName, email, password)
    print(f'{firstName} created!')

# this command will be : flask user create bob bobpass

@user_cli.command("list", help="Lists users in the database")
@click.argument("format", default="string")
def list_user_command(format):
    if format == 'string':
        print(get_all_users())
    else:
        print(get_all_users_json())



app.cli.add_command(user_cli) # add the group to the cli

'''
applicant commands
'''
applicant_cli = AppGroup('applicant', help='Applicant object commands')
@applicant_cli.command("create", help="creates an applicant")
@click.argument("firstname", default="unemployed")
@click.argument("lastname", default="unemployed")
@click.argument("email", default="unemployed@email.com")
@click.argument("password", default="robpass")
def create_applicant_command(firstname, lastname, email, password):
    applicant = create_applicant(firstname, lastname, email, password)
    print(f'{firstname} created! With an ID of {applicant.id}')


@applicant_cli.command("apply", help="creates an job application")
@click.argument("applicantid", default="1")
@click.argument("joblistingid", default="1")
def apply_for_job_command(applicantid, joblistingid):
    apply_for_job(applicantid,joblistingid)

@applicant_cli.command("view_jobs", help="show all jobs listings")
def view_job_command():
    view_jobs()

app.cli.add_command(applicant_cli) # add the group to the cli

'''
admin commands
'''
admin_cli = AppGroup('admin', help='admin object commands')
@admin_cli.command("create", help="creates an admin")
@click.argument("firstname", default="bigboss")
@click.argument("lastname", default="unemployed")
@click.argument("email", default="bigboss@email.com")
@click.argument("password", default="robpass")
def create_admin_command(firstname, lastname, email, password):
    create_admin(firstname, lastname, email, password)
    print(f'{firstname} created!')

@admin_cli.command("remove_user", help="removes a user")
@click.argument("user_id", default="0")
def remove_user_command(user_id):
    remove_user(user_id)

@admin_cli.command("remove_listing", help="removes a listing")
@click.argument("listing_id", default="0")
def remove_listing_command(listing_id):
    remove_listing(listing_id)

app.cli.add_command(admin_cli) # add the group to the cli

'''
employer commands
'''
employer_cli = AppGroup('employer', help='admin object commands')
@employer_cli.command("create", help="creates an admin")
@click.argument("firstname", default="employer")
@click.argument("lastname", default="unemployed")
@click.argument("email", default="employer@email.com")
@click.argument("password", default="robpass")
def create_employer_command(firstname, lastname, email, password):
    employer=create_employer(firstname, lastname, email, password)
    print(f'{firstname} created! with an ID of {employer.id}')

@employer_cli.command("create_listing", help="creates an job listing")
@click.argument("title", default="internship")
@click.argument("description", default="basically slave labour")
@click.argument("employerid", default="1")
def create_job_listing_command(title, description, employerid):
    job_listing=create_listing(title, description, employerid)
    click.echo(f"Job listing '{title}' created by employer {employerid} with an ID of {job_listing.id}.")

@employer_cli.command("view_all_applicants", help="shows all applicants for all jobs")
@click.argument("employer_id", default="0")
def view_applicants_for_employer_command(employer_id):
    view_applicants_for_employer(employer_id)

@employer_cli.command("view_job_applicants", help="shows all applicants for a job")
@click.argument("job_id", default="0")
def view_job_applicants_command(job_id):
    view_applicants_for_job(job_id)


app.cli.add_command(employer_cli) # add the group to the cli

'''
Test Commands
'''

test = AppGroup('test', help='Testing commands') 

@test.command("user", help="Run User tests")
@click.argument("type", default="all")
def user_tests_command(type):
    if type == "unit":
        sys.exit(pytest.main(["-k", "UserUnitTests"]))
    elif type == "int":
        sys.exit(pytest.main(["-k", "UserIntegrationTests"]))
    else:
        sys.exit(pytest.main(["-k", "App"]))
    

app.cli.add_command(test)