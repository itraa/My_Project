import flask, flask.views
import os
import sys
import utils
from flask.ext.mail import Message
from flask_sqlalchemy import SQLAlchemy
from apscheduler.scheduler import Scheduler
from models import *
#import datetime
#from datetime import date
import login

def weaning_reminder():

    __table__ = pups_info
    first_output = __table__.query.with_entities(__table__.Pups_Breeding_Cage_Id).filter_by(First_Date_of_weaning=date.today()).all()
    final_output = __table__.query.with_entities(__table__.Pups_Breeding_Cage_Id).filter_by(Final_Date_of_weaning=date.today()).all()
    
    first_email_list = []
    final_email_list = []

# Identify username for hello message
    for key, value in login.users.iteritems():
        hello_msg_to = key

    if final_output:
        for final_each in final_output:
            for i in range(len(final_each)):
                final_email_list.append(str(final_each[i]))

        final_msg = Message('Final weaning reminder!',
                    sender='xx@gmail.com.com',
                    recipients=['xx@gmail.com'])
        final_msg.body = "Hello %s" % hello_msg_to + ", this is your final reminder for weaning pups from the breeding cage(s): %s" % final_email_list

        mail.send(final_msg)

    if first_output:
        for first_each in first_output:
            for i in range(len(first_each)):
                first_email_list.append(str(first_each[i]))

        first_msg = Message('First weaning reminder!',
                    sender='xx@gmail.com.com',
                    recipients=['xx@gmail.com'])
#        first_msg.body = 'This is the first reminder for weaning pups from the breeding cage(s): %s' % first_email_list
        first_msg.body = "Hello %s" % hello_msg_to + ", this is your first reminder for weaning pups from the breeding cage(s): %s" % first_email_list

        mail.send(first_msg)


weaning_reminder() 
#sched = Scheduler()
#sched.start()
#job = sched.add_cron_job(weaning_reminder, hour=0)
