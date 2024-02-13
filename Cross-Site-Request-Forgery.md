# How CSRF Attacks Work:

Authentication Exploitation: The attacker crafts a malicious link or script that, when executed by the victim, performs actions on the target application where the victim is authenticated.

Victim Interaction: The victim interacts with the malicious link, often through social engineering tactics such as enticing offers or disguised content.

Unintended Actions: As a result of the victim's interaction, actions are triggered on the target application. These actions are executed with the victim's authentication credentials, giving the
attacker control.

# Impact of CSRF Attacks:

Unauthorized Actions: Attackers can perform actions on behalf of victims without their consent, leading to unauthorized transactions, data modification, or account compromise.

Data Manipulation: Attackers can manipulate data within the victim's account, leading to data corruption or loss.

Account Takeover: CSRF attacks can lead to unauthorized account actions, including changing passwords, adding new accounts, or performing other sensitive operations.

# Preventing CSRF Attacks:

Anti-CSRF Tokens: Implement anti-CSRF tokens that are unique to each user session. These tokens are included in requests and validated by the server to prevent unauthorized actions.

SameSite Cookie Attribute: Configure cookies with the SameSite attribute to restrict their usage to the same origin, reducing the risk of CSRF attacks.

Referrer Policy: Implement strict referer policies to ensure that requests are only accepted from trusted origins.

HTTP Methods: Use appropriate HTTP methods for different types of requests (GET, POST, PUT, DELETE), and avoid using GET for actions that modify data.

Double Submit Cookie: Create a cookie containing a value that matches the value of a form field. The server compares these values to validate the request's authenticity.
