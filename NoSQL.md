Take MongoDB, for example. In MongoDB syntax, Users.find()
returns users that meet a certain criteria. For example, the following 
query returns users with the username vickie and the password password123:


Users.find({username: 'vickie', password: 'password123'});

If the application uses this functionality to log in users and populates 
the database query directly with user input, like this:

Users.find({username: $username, password: $password});

attackers can submit the password {$ne: ""} to log in as anyone. For example, 
let’s say that the attacker submits a username of admin and a password of 
{$ne: ""}. The database query would become as follows:

Users.find({username: 'admin', password: {$ne: ""}});

In MongoDB, $ne selects objects whose value is not equal to the specified value. Here, the query would return users whose username is admin
and password isn’t equal to an empty string, which is true unless the admin 
has a blank password! The attacker can thus bypass authentication and gain 
access to the admin account.


Injecting into MongoDB queries can also allow attackers to execute 
arbitrary JavaScript code on the server. In MongoDB, the $where, mapReduce, 
$accumulator, and $function operations allow developers to run arbitrary 
JavaScript. For example, you can define a function within the $where operator to find users named vickie:

Users.find( { $where: function() { return (this.username == 'vickie') } } );

Say the developer allows unvalidated user input in this function and 
uses that to fetch account data, like this:

Users.find( { $where: function() { return (this.username == $user_input) } } );

In that case, an attacker can execute arbitrary JavaScript code by 
injecting it into the $where operation. For example, the following piece of 
malicious code will launch a denial-of-service (DoS) attack by triggering a 
never-ending while loop:

Users.find( { $where: function() {
 return (this.username == 'vickie'; while(true){};) } } );


The process of looking for NoSQL injections is similar to detecting 
SQL injections. You can insert special characters such as quotes (' "), semicolons (;), and backslashes (\), as well as parentheses (()), brackets([]), and 
braces ({}) into user-input fields and look for errors or other anomalies. 
You can also automate the hunting process by using the tool NoSQLMap 
(https://github.com/codingo/NoSQLMap/).


Developers can prevent NoSQL injection attacks by validating user input 
and avoiding dangerous database functionalities. In MongoDB, you can disable the running of server-side JavaScript by using the --noscripting option 
in the command line or setting the security.javascriptEnabled flag in the 
configuration file to false. Find more information at https://docs.mongodb.com/
manual/faq/fundamentals/index.html. 
Additionally, you should follow the principle of least privilege when 
assigning rights to applications. This means that applications should run 
with only the privileges they require to operate.
