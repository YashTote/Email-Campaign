# Email-Campaign

  
**Setting up the Project**

 Clone this repository using the link ` https://github.com/YashTote/Email-Campaign.git `. Enter the emailCampaign directory `cd emailCampaign`. You might see this: 
 ```
 emailCampaign
 README.md
 requirements.txt
 ```
 In order to start the development version of the Email Campaign application, we need a virtual environment. Make sure you have [Python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installation/) installed for the Django.
 
 Now in the same directory we need a [virtual environment](https://www.freecodecamp.org/news/how-to-setup-virtual-environments-in-python/) in order to install backend specific dependencies. It is recommended to use the official [Python](https://www.python.org/downloads/) version only instead of using one from third party python version managers ex : pyenv etc. This makes sure that the project runs smoothly.

**RUN following to start the backend server:**
 ```
 pip install virtualenv
 python3 -m venv env
 source env/bin/activate
 ```
 This starts our virtual environment and we are ready to install the necessary dependencies.

 ```
 pip install -r requirements.txt
 ```
**To configure the server side Email Host:**
 1. we need to do the following changes to the code. We need a gmail account and  `app password` credentials. Please see the below video to see how to get one (**The person in this video chooses the Windows Computer as Password, But we need `Others (Custom name)` Password**) . [Link to the youtube video](https://www.youtube.com/watch?v=rpmfDHCyPbo).
 2. Now `cd emailCampaign/emailCampaign/` and open settings.py. Scroll to the bottom and set the `EMAIL_HOST_USER` and `EMAIL_HOST_PASSWORD` to your custom credentials.
 3. A last step `cd emailCampaign/endpoint/` and open `views.py`. Edit the `from_email` (line:14) to your HOST EMAIL (Same as above). Your backend is now ready to perform.


 After the dependencies are installed and Email Host is configured `cd emailCampaign` and run `python3 manage.py createsuperuser`, enter the necessary details in order to access the SQLite database admin panel. Now run `python3 manage.py runserver`. 
 
> **Note**
 > If you face the _sqlite3() error head to [this](https://www.codethebest.com/python-package-errors/modulenotfounderror-no-module-named-sqlite3-solved/)

**How to send the emails ?**

1. These are the various API endpoints to perform CRUD operations on the database. You can also perform these operations from Django admin panel `localhost:8000/admin`.
  
   1. ` send/ ` To start sending Emails to the clients using pub-sub Architecture.
   2. `add_user/ ` To add new user with unique Email ID.
   3. `edit_user_status/` To edit the subscriber status as inactive or active.
2 .This is how Admin Panel looks like
   ![Screenshot of main page admin panel](https://github.com/YashTote/Email-Campaign/blob/main/static/image/Screenshot%20from%202023-09-08%2019-20-05.png)
3. Adding Subscribers. There are two ways to do this:
    Using API clients like PostMan:
     ![Screenshot of add_user call from postman]()
    Or using Admin Panel:
     ![Screenshot of add Subscriber](https://github.com/YashTote/Email-Campaign/blob/main/static/image/Screenshot%20from%202023-09-08%2019-20-50.png)
4. Adding Campaign. Go to the Campaigns table in admin panel
    ![Screenshot of Campaign Table](https://github.com/YashTote/Email-Campaign/blob/main/static/image/Screenshot%20from%202023-09-08%2019-20-27.png)
   Add appropriate title. Title won't be reflected to the final email that is sent to the user. But this is how we will decide which campaign is to be sent to particular group of subscribers. Fill the remainig details compulsarily.

5. Adding Category of Subscribers. Example of category could be like subscribers that use MikeIP-Manager or any other product.
   ![Screenshot of category](https://github.com/YashTote/Email-Campaign/blob/main/static/image/Screenshot%20from%202023-09-08%2019-21-10.png)
   Make sure this category **does not have any spaces** between the words. We will mention this Category in the `GET` request to perform Email Sending operation.

6. Finally we create a link betweeen each `Subscriber` - `Campaign` - `Category`.
   ![Screenshot of CategoryRelationship](https://github.com/YashTote/Email-Campaign/blob/main/static/image/Screenshot%20from%202023-09-08%2019-21-24.png) 

   **When we make the `send/` call by mentioning the `Category`, all the `subscribers` under that `category` get the Email that has `Campaign` contents. Only the active subscribers get this Email.**

7. Making the API `GET` call for sending Email. Perform the call on `http://localhost:8000/endpoint/send/`, with a Parameter Key : `category` and value : `category_name`. 
    ![Screenshot of API get call](https://github.com/YashTote/Email-Campaign/blob/main/static/image/Screenshot%20from%202023-09-08%2020-27-30.png)


    
   

