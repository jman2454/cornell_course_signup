# cornell_course_signup
A bot to fill out your Cornell student center shopping cart

# Requirements
 - Selenium:
   - `pip install selenium`
 - Chrome webdriver (look it up)

# Usage
This script will sign in to student center, and will send your Duo 2-step verification mobile app a request that you 
will have to approve. Before running the script, fill your enrollment shopping cart with all of the classes
that you'd like to sign up for. Note that this script will always navigate to the latest semester with 
enrollment data available (possible change for the future). 
 
 - `python signup.py [netid] [password]`
