# AWS AppConfig Demo

This repository demonstrates how to use AWS AppConfig in a serverless context. The [`template.yaml`](./template.yaml) defines all of the resources required for this demo including a basic SAM application API, and some AWS AppConfig resources.

## Dependencies

- [An AWS account](https://portal.aws.amazon.com/billing/signup)
- [`aws-sam-cli`](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-sam-cli-install.html)

## Deployment

First make sure you have credentials for an AWS account you'd like to deploy this demo into. Then run the following command:

```sh
$ sam deploy --guided
```

For the parameters, leave everything as the default. The only parameter you must specify a value for is `EnvironmentName`, which you can make anything (like `'dev'`).

When the deployment completes, you'll see the `Endpoint` output, which contains the url you'll want to navigate to in order to test the endpoint. This may take a while as the initial AppConfig deployment takes some time.

## Configuration Change

You'll notice in the template that the initial configuration value is

```json
{
  "message": "Hello, World!"
}
```

Which is what gets returned from the API endpoint. If you go to the AWS AppConfig console, click under your application, and select the `apiconfig` configuration profile. Click "Create" under "Hosted configuration versions" to create a configuration version you'd like to deploy. Update the message to any valid json object, and save.

Then, click the "Start deployment" button at the top, selecting the configuration version you just created, and choosing a deployment strategy. To see some of the capabilities of AppConfig, try out a slower rollout strategy. When you're done, click "Start deployment."

Over time, if you refresh your endpoint, you should notice it's returned value switches back and forth between the old and new values, with the new value gradually becomming more frequent.
