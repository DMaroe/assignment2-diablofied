Name : Dylan Dahran Pribadi
NPM  : 2106720872

1. What does {% csrf_token %} do in the <form> element? What happens if there is no such "code snippet" in the <form> element?

For context, a CSRF Token is a secret, unique and unpredictable value a server-side application generates in order to protect CSRF vulnerable resources. 

If theres no such "code snippet" in te form element, it is very likely that the site is extremely vulnerable for cyberattacks.

2. Can we create the <form> element manually (without using a generator like {{ form.as_table }})? Explain generally how to create <form> manually.

It is possible.

For context, An HTML Form is a group of one or more fields/widgets on a web page, which can be used to collect information from users for submission to a server. Forms are a flexible mechanism for collecting user input because there are suitable widgets for entering many different types of data, including text boxes, checkboxes, radio buttons, date pickers and so on. Forms are also a relatively secure way of sharing data with the server, as they allow us to send data in POST requests with cross-site request forgery protection.

ref : https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Forms



3. Describe the data flow process from the submission made by the user through the HTML form, data storage in the database, until the appearance of the data that has been stored in the HTML template.

First of all, we click the "Create Task" button

4. Explain how you implement the checklist above.