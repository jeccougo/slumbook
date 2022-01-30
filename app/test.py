from app.sendmail import send_mails
from app import mongo, api
from flask_restful import Resource,reqparse



#Change password
class SEndEmail(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument('email_address', 
                        type=str,
                        required=True,
                        help="Enter Email Address in comma separated. Field cannot be left blank")
    parser.add_argument('subject', 
                        type=str,
                        required=True,
                        help="Enter Email subject. Field cannot be left blank")
    parser.add_argument('message', 
                        type=str,
                        required=True,
                        help="Enter Email message. Field cannot be left blank")
                    

    def post(self):
        data = SEndEmail.parser.parse_args()
        _email = data["email_address"]
        emails = _email.split(",") #list of email addresses
        subject = data["subject"]
        message = data["message"]

        #send emails.
        name=""
        msg = message
        # msg="Thank you for contacting Tolemsoft Technologies. We will get back to you shortly."
        
        for email in emails:
            mail = send_mails(sender='Tolemsoft Technologies', receiver=email, subject=subject, name=name, token="#", token_name="Thank you!", message=msg)
        print("Emails sent successfully")
        return {"status":True, "message":"Emails sent successfully", "data": ""}, 200

api.add_resource(SEndEmail, '/api/v1/sendmail')
