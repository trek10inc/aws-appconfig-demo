import os
import json
import urllib.request


def lambda_handler(event, context):
    url = f'http://localhost:2772/applications/{os.getenv("APPCONFIG_APPLICATION_NAME")}/environments/{os.getenv("APPCONFIG_ENVIRONMENT_NAME")}/configurations/{os.getenv("APPCONFIG_CONFIG_NAME")}'
    config = urllib.request.urlopen(url).read()
    return {
        'statusCode': 200,
        'body': json.dumps({
            'message': 'lambda executed',
            'config': json.loads(config),
        }, default=str),
    }
