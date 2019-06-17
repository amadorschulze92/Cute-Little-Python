import string

email = ["mschulze@oxy.edu"]

def email_dom(email):   
    for x in email:
        if not email:
            return None
        return x.split('@')[-1]
	
print email_dom(email)