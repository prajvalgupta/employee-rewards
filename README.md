# employee-rewards
This repo is for the Data Management Course (MIS 284N) as mid-term project. The app is successfully deployed on http://emp-rewards.appspot.com/

## Team Members
Prajval Gupta, Pei-Hsin Ho

## Credentials(user_name, password)
Admin: prajval, Prajval@27
Users: abcd, Prajval@27 <br>
       abhishek, Password@1234 <br>
       betty, Password@123 <br>
       kelly, Password@321 <br>
       wwww, Prajval@27


## ER Diagram
![ER Diagram](https://github.com/prajvalgupta/employee-rewards/blob/master/ERdiagram.png)

## DDL and DML
Since we used Django for this Employee Systems, we do not have the DML and DDL when we developed, but we dumped out the DDL. Here is the DDL.


## Any assumptions you made that you feel important to call out
As we think, 10000 points are hard to reach for a user in a month, so we modify the rules: Users can redeem 10 points for a gift card that has the value $1. For example, if a user redeems 40 points, he or she will get a $4 gift card.


## Our Employee Rewards System
When you enter ​emp-rewards.appspot.com​ in your browser, the first welcome page of our system is below:



Click the Login/Signup button on the right, it will show the login pages. Type the user name and the password to log in. New users can also signup to log into our system.



In the meantime, the password saved on the Admin page will be encrypted using an algorithm, iterations, salt and a hash. We also dumped out the insert SQL to see if the password is encrypted.


After logging in, click the Transfer Points page. You’ll see the form to fill in who you want to give the points to and how many points as long as the thank you message you want to send. Filling all the information and click the Transfer Points button, you’ll see “Points transferred successfully”.


The Points History pages allow Admin to review the history of giving and receiving the points as well as the gift cards from all users.



Under this page of Admin, there is a reset button, which is only visible to Admin, that can reset all points to give out. Click on the button, you’ll see the points be reset.



As for a normal user, the History Points page shows his or her record of giving and receiving points. We also insert the random points transactions and gift card redemption for the previous two months.


This is how we generate random dummy data for the previous two months.


On the Gift Cards page, you are able to input how many points you want to redeem to exchange for gift cards. If you do not have enough points, the system will show “You don’t have enough amount to redeem a gift card.”

