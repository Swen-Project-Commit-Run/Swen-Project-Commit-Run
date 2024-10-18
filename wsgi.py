import click, pytest, sys
from flask import Flask
from flask.cli import with_appcontext, AppGroup


from App.database import db, get_migrate
from App.models import User
from App.main import create_app
from App.controllers import ( create_Company, view_applicants_for_jobListing,CreateJobListing, create_employer, CreateJobListing, remove_listing,remove_user, create_admin, get_job_listings,apply_job,create_job_applicant, get_all_users_json, get_all_users,create_user, initialize )


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
user_cli = AppGroup('user', help='Testing commands') 
# Then define the command and any parameters and annotate it with the group (@)
@user_cli.command("create", help="Creates a user")
@click.argument("firstname", default="rob")
@click.argument("lastname", default="man")
@click.argument("email", default="rob@email.com")
@click.argument("username", default="bobuser")
@click.argument("password", default="robpass")
def create_user_command(firstname, lastname, email, username, password):
    create_user(firstname, lastname, email, username, password)
    print(f'{firstname} {lastname} created!')


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
@click.argument("username", default="unemployeduser")
@click.argument("password", default="robpass")
def create_applicant_command(firstname, lastname, email, username, password):
    applicant = create_job_applicant(firstname, lastname, email, username, password)
    print(f'{firstname} created! With an ID of {applicant.id}')


@applicant_cli.command("apply", help="creates an job application")
@click.argument("applicantid", default="1")
@click.argument("joblistingid", default="1")
def apply_for_job_command(applicantid, joblistingid):
    apply_job(applicantid,joblistingid)

@applicant_cli.command("view_jobs", help="show all jobs listings")
def view_job_command():
    job_listings = get_job_listings()
    if not job_listings:
        print("No job listings found.")
    else:
        for job in job_listings:
            
            print(
                f"Job ID: {job.id}, Employer ID: {job.employer_id}, Title: {job.title}, "
                f"Description: {job.description}")

app.cli.add_command(applicant_cli) # add the group to the cli


'''
admin commands
'''
admin_cli = AppGroup('admin', help='admin object commands')
@admin_cli.command("create", help="creates an admin")
@click.argument("firstname", default="bigboss")
@click.argument("lastname", default="unemployed")
@click.argument("email", default="bigboss@email.com")
@click.argument("username", default="admin1")
@click.argument("password", default="robpass")
def create_admin_command(firstname, lastname, email, username, password):
    create_admin(firstname, lastname, email, username, password)
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
@click.argument("username", default="employer1")
@click.argument("password", default="robpass")
def create_employer_command(firstname, lastname, email, username, password):
    employer=create_employer(firstname, lastname, email, username, password)
    print(f'{firstname} created! with an ID of {employer.id}')


@employer_cli.command("create_listing", help="creates an job listing")
@click.argument("title", default="internship")
@click.argument("description", default="basically slave labour")
@click.argument("employerid", default="1")
def create_job_listing_command(employerid, title, description):
    job_listing=CreateJobListing(employerid, title, description)
    click.echo(f"Job listing '{title}' created by employer {employerid} with an ID of {job_listing.id}.")


@employer_cli.command("view_job_applicants", help="shows all applicants for a job")
@click.argument("job_id", default="0")
def view_job_applicants_command(job_id):
    view_applicants_for_jobListing(job_id)

@employer_cli.command("add_company", help="adds a company")
@click.argument("name", default="boring company")
@click.argument("employer_id", default="0")
def add_company_command(name, employer_id):
    create_Company(name, employer_id)
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