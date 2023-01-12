# Web Scraping Using Django Cron Job



### Web Scraping is done by a cron job. By setting up a corn job the scarping is done here in django. It's an automated scraping task.


#### Quick Start

Steps to follow:
- Download the Files
- Create a virtual env
- activate the env
- install the requirements.txt
- migrate the database
- bash run.sh


#### Details
Step 1: Create a virtual env.

Install venv to your host Python by running this command in your terminal:
```
pip install virtualenv
```
To create a virtual environment following commands might be helpful
```
 python<version> -m venv <virtual-environment-name>
 or 
 virtualenv <environment name>
```

Step 2: Install the requirements.txt 

```
 pip install -r requirements.txt
 or 
 pip install --upgrade -r requirements.txt
```

Step 3: Download a Chrome Driver.

To download a chrome driver, this following link can help. [Google Chrome Driver](https://chromedriver.chromium.org/downloads)
keep the chromedriver in the assets folder and make the right path in driver.py

Step 4: Django App Set Up

After installing everything the apps need to be initialized in the INSTALLED_APS section.


Step 5: Django Models

To store the database, model creation with specific field is important. There is a models.py file where the database needs to be created. the custom database name can be given here.

Step 6: PgAdmin Set Up

Locate on the directory where the .yml file is present. Hit the command prompt with the following command:
```
docker-compose up
```

this will help to intereact with the postgresql database.

Step 7: Run the cron job with this command 
```
bash run.sh
```
<br />

#### Directory Structure:

 * [airbnbscrap](/airbnbscrap/)
   * [asgi.py](/airbnbscrap/asgi.py)
   * [settings.py](/airbnbscrap/settings.py)
   * [urls.py](/airbnbscrap/urls.py)
   * [wsgi.py](/airbnbscrap/wsgi.py)
 * [manage.py](/manage.py)
 * [requirements.txt](requirements.txt)
 * [run.sh](/run.sh)
 * [myapp](/myapp/)
   * [admin.py](/myapp/admin.py)
   * [apps.py](/myapp/apps.py)
   * [cron.py](/myapp/cron.py)
        * [management](/myapp/management/)
        * [App Data](/myapp/management/App%20Data/)
            * [CSVDIR](/myapp/management/App%20Data/CSVDIR/)
            * [XMLDIR](/myapp/management/App%20Data/XMLDIR/)
        *   [commands](/myapp/management/commands/)
            * [different scaping functions]()
        * [migrations](/myapp/migrations/)
        * [models.py](/myapp/models.py)
      * [README.md](/myapp/readme.md)
      * [serializers.py](/myapp/seralizers.py)
      * [service](/myapp/service/)
        * [different helper functions](/myapp/service/convert.py)
     * [tests.py](/myapp/tests.py)
     * [views.py](/myapp/views.py)

