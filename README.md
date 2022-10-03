# AWS Chalice Client for LocalStack

This project provides `chalice-local`, a small wrapper script to use
[AWS Chalice](https://github.com/aws/chalice) with [LocalStack](https://github.com/localstack/localstack).

## Installing

The `chalice-local` command can be easily installed via `pip`:
```
pip install chalice-local
```

You can then use the `deploy` command to deploy the application against the LocalStack instance running locally:
```
chalice-local deploy
```

For example, using the hello-world Chalice sample app:
```
$ chalice-local deploy
Creating deployment package.
Reusing existing deployment package.
Creating IAM role: test-dev
Creating lambda function: test-dev
Creating Rest API
Resources deployed:
  - Lambda ARN: arn:aws:lambda:us-east-1:000000000000:function:test-dev
  - Rest API URL: https://oc6nvd38ta.execute-api.us-east-1.amazonaws.com/api/
```

We can then slightly adjust the URL to target the local endpoint in LocalStack, and invoke the deployed API directly:

```
$ curl http://oc6nvd38ta.execute-api.localhost.localstack.cloud:4566/api/
{"hello":"world"}
```

## Configuration

Please refer to the LocalStack repository for available configuration options. Details following soon.

## Change Log

* `v0.1.1`: Initialize default region to avoid boto client issues
* `v0.1.0`: Initial release of `chalice-local`

## License

This library is released under the Apache License, Version 2.0 (see LICENSE.txt).
