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

 After the dependencies are sucessfully installed `cd emailCampaign` and run `python3 manage.py createsuperuser`, enter the necessary details in order to access the SQLite database admin panel. Now run `python3 manage.py runserver`. 
 
> **Note**
 > [!NOTE]
 > If you face the _sqlite3() error head to [this](https://www.codethebest.com/python-package-errors/modulenotfounderror-no-module-named-sqlite3-solved/)

How to send the emails ?

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
   Add appropriate title. Title won't be reflected to the final email that is sent to the user. But this is how we will decide which campaign is to be sent to particular group of subscribers.

5. Adding Category of Subscribers. Example of category could be like subscribers that use MikeIP-Manager or any other product.
   ![Screenshot of category](https://github.com/YashTote/Email-Campaign/blob/main/static/image/Screenshot%20from%202023-09-08%2019-21-10.png)
   Make sure this category **does not have any spaces** between the words. We will mention this Category in the `GET` request to perform Email Sending operation.

    
  

