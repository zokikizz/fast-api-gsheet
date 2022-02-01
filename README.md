# fast-api-gsheet

Bachelor thesis service for interacting with gsheets

## Requirements:

1. Installed docker to run service 

## Instructions:

1. Need to enable `Google sheet API` in Google Cloud Platform
2. Generate Service Account which will have roles as `Owner` or `Editor` 
3. Create creadentials as json in `KEYS` tab 
4. Download creds put in root of the project folder and name it `creds.json`
5. Run `docker-compose up -d --build`

## For deploy using [Deta](https://docs.deta.sh/docs/home/):

### Note:
1. Deta doesn't support deploying folders that are hiddden ( starts with dot ex. -> .foldername)


## Environments:
    DETA_PROJECT_KEY=<deta_project_id>
    MAIL_USERNAME=<username>
    MAIL_PASSWORD=<pass>
    MAIL_SERVER=<server>
    MAIL_PORT=<port>
    MAIL_FROM=<email>
    MAIN_TITLE=<title>
    SECRET_KEY=<secret>