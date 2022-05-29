 # TravelCheck - Face Recognition Web App
## Submission for Microsoft Engage 2022 🌟

[![GitHub code size in bytes](https://img.shields.io/github/languages/code-size/akshi0409/TravelCheck-MicrosoftEngage2022?logo=github&style=for-the-badge)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022) 
[![GitHub last commit](https://img.shields.io/github/last-commit/akshi0409/TravelCheck-MicrosoftEngage2022?style=for-the-badge&logo=git)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022) 
[![GitHub stars](https://img.shields.io/github/stars/akshi0409/TravelCheck-MicrosoftEngage2022?style=for-the-badge)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022stargazers) 
[![My stars](https://img.shields.io/github/stars/akshi0409?affiliations=OWNER%2CCOLLABORATOR&style=for-the-badge&label=My%20stars)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022e/stargazers) 
[![GitHub forks](https://img.shields.io/github/forks/akshi0409/TravelCheck-MicrosoftEngage2022?style=for-the-badge&logo=git)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022/network)
[![Code size](https://img.shields.io/github/languages/code-size/akshi0409/TravelCheck-MicrosoftEngage2022?style=for-the-badge)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022)
[![Languages](https://img.shields.io/github/languages/count/akshi0409/TravelCheck-MicrosoftEngage2022?style=for-the-badge)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022)
[![Top](https://img.shields.io/github/languages/top/akshi0409/TravelCheck-MicrosoftEngage2022?style=for-the-badge&label=Top%20Languages)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022)
[![Issues](https://img.shields.io/github/issues/akshi0409/TravelCheck-MicrosoftEngage2022?style=for-the-badge&label=Issues)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022)
[![Watchers](	https://img.shields.io/github/watchers/akshi0409/TravelCheck-MicrosoftEngage2022?label=Watch&style=for-the-badge)](https://github.com/akshi0409/TravelCheck-MicrosoftEngage2022) 

Travel Safe with `TravelCheck` which uses face recognition to check your identity.
 Face Recognition System  -  Recognition of face 
 using our Identity Card (Aadhar Card)

<p align="center">
<a href="https://drive.google.com/file/d/17eqzx6u1sRmUWyloLy0KRDuxjwKn2XIZ/view?usp=sharing">
<img src="https://user-images.githubusercontent.com/44814671/170883919-5d948bb9-ee22-4921-b84f-5b105b941813.jpeg" alt="TravelCheck-logo"/>
</a>
</p>

[![Generic badge](https://img.shields.io/badge/view-demo-blue?style=for-the-badge&label=View%20Demo%20Video)](https://drive.google.com/file/d/17eqzx6u1sRmUWyloLy0KRDuxjwKn2XIZ/view?usp=sharing) 

Travel Check - Recently when I was travelling, 
 I went to the airport and just at the entrace, 
 I saw a man who stood there to check the aadhar 
 cards of the passengers and to match their faces 
 with it. Just then, a plenty of ideas came to my
 mind, to automate this system of face recognition at the airports.
 When we look closely, this product would have 
 application in many other fields too, let's say 
 for other travel modes.
 
  ## Features and Interfaces

1. Landing Page
   - Seamless landing page with a navigation bar at the top containing the `About Us`,`Register`,`Login` and `Contact Us` buttons for the users. It has the tagline of the product along with a quick one-liner description to provide information of what the website is about.
     ![image](https://user-images.githubusercontent.com/44814671/170825454-5d4f4b12-74df-462e-ab59-cf6638848718.png)
     
   - The home page contains 5 sections :- Landing page, a carousel section, weather details section, feedback section and a footer. 
   - The carousel section contains a list of three images of the scenic beauties from around the world. The carousel automatically changes the picture after a while, also having the options to operate manually. Each image contains a line at the bottom with details about it
     ![image](https://user-images.githubusercontent.com/44814671/170825864-0708891c-3ae7-438c-b0c6-e94cd4aea2ff.png)
     
   - The weather details section contains two options - either to get the data using the users location or to get the data of any other location manually by entering the details. I have used the `X-RapidAPI` for fetching details from the API and displaying the details.
     ![image](https://user-images.githubusercontent.com/44814671/170826039-4493be84-ad56-4fac-86d9-79b2454425e3.png)
     ![image](https://user-images.githubusercontent.com/44814671/170830442-e3438f28-f75d-4b82-b045-7cdb4f4be9f0.png)
     
   - For feedback/contact us section, I have used Microsoft Forms, and embeded it with my application to get details directly from the user.
   - The footer section is betautifully designed using the four colors used in the Microsoft Logo.
     ![image](https://user-images.githubusercontent.com/44814671/170829661-849d9860-1970-47cc-bb1c-79743fc8dc7a.png)
     
2. About Us Page
   - The about us page contains a whole timeline of the work done during the whole duration of 3 weeks and why this idea was chosen.

3. Registration Page
   - As the user clicks on the register button, they are redirected to the registration site. This site collects the basic data from the user including their name, phone number, email address, aadhar card number and the aadhard has to be uploaded in that web page. The web site collects the data from the user and stores it.
     ![image](https://user-images.githubusercontent.com/44814671/170834275-ff6432d3-a7f8-4070-b04b-4c0b0cff7900.png)
   - If the data is succesfully stored, another page appears showing that the registration was successful.
     
4. Login Page
   - To get verified, the user has to click the login button, which redirects the user to the login page.
   - Step 1- Fill in the unique aadhar card number.
     ![image]<img width="946" alt="7" src="https://user-images.githubusercontent.com/44814671/170834782-6a7c1b2c-dbac-4f85-8eb4-75aba0ec2c0b.png">
   - Step 2 - The camera video feed is displayed on their screen. If the image gets detected a square box would appear around their faces with their Aadhar number written on it. They have to click on the verify me button. 
   - ![image](https://user-images.githubusercontent.com/44814671/170835154-dcbf1b0c-c5a1-4c28-bfbd-b3485f914841.png)
   - Step 3 - If the verification is successful, another page appears confirming that they have been verified.
     ![image](https://user-images.githubusercontent.com/44814671/170839522-14a57fb0-8bb5-4c89-b054-b26e91b88239.png)
     
### Tools and Languages: 
<p align="left"> <a href="https://flask.palletsprojects.com/en/2.1.x/" target="_blank"> <img src="https://img.shields.io/badge/Flask-000000?style=for-the-badge&logo=flask&logoColor=white" alt="flask" width="40" height="40"/> </a> <a href="https://www.python.org/" target="_blank"> <img src="https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue" alt="python" width="40" height="40"/> </a> <a href="https://getbootstrap.com" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/bootstrap/bootstrap-plain-wordmark.svg" alt="bootstrap" width="40" height="40"/> </a> <a href="https://www.w3schools.com/css/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/css3/css3-original-wordmark.svg" alt="css3" width="40" height="40"/> </a> <a href="https://git-scm.com/" target="_blank"> <img src="https://www.vectorlogo.zone/logos/git-scm/git-scm-icon.svg" alt="git" width="40" height="40"/> </a> <a href="https://heroku.com" target="_blank"> <img src="https://www.vectorlogo.zone/logos/heroku/heroku-icon.svg" alt="heroku" width="40" height="40"/> </a> <a href="https://www.w3.org/html/" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/html5/html5-original-wordmark.svg" alt="html5" width="40" height="40"/> </a> <a href="https://developer.mozilla.org/en-US/docs/Web/JavaScript" target="_blank"> <img src="https://raw.githubusercontent.com/devicons/devicon/master/icons/javascript/javascript-original.svg" alt="javascript" width="40" height="40"/> </a> </p>


## Points to remember while testing the app

1. Allow **permissions** for the camera.
2. Make sure the **URL** is starting with https
3. If the website is not able to detect the face, make sure your **face is fully visible** in the camera, you can confirm this by seeing the video feed.

## 🚩Installation/Environment Setup 

  #### 1. Clone App
  
  * Make a new folder and open the terminal there.
  * Write the following command and press enter.
  
  ```
    $ git clone
  ```
    
 #### 2. Install flask packages
  * Install flask and add flask to the path variables.
  
#### 3. Run Locally

 * While you are still inside the cloned folder, write the following command to run the website locally. 
 
 ```
   $ flask run
 ```

## 🚩 Future Scopes:-
Feature | Explanation
------------ | -------------
Increasing use cases | We can modify this application to be used in online and offline classrooms for identity verification or as an attendance system, it can be used in offices and hospitals.
Better Accuracy | We can modify the face recognition models and train it to get better results, so the verification would be more accurate.
Added Functionalities | We can also add functionalities through which the application would be more friendly for the specially abled people.

## Need help?

Feel free to contact me on [LinkedIn](https://www.linkedin.com/in/akshita-sah/) 
[![Twitter](https://img.shields.io/badge/Twitter-follow-blue.svg?logo=twitter&logoColor=white)](https://twitter.com/_akshitaSah)

## Thanks for viewing!
